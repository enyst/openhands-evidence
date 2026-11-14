"""SDK twin: is ask_agent usage in base_state.json after the call, and after a reload?

Key-free: the provider call (litellm completion) is replaced by a scripted reply
that reports 100 prompt tokens per call.
"""
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

from litellm.types.utils import Choices, Message as LiteLLMMessage, ModelResponse, Usage
from pydantic import SecretStr

from openhands.sdk import LLM, Agent
from openhands.sdk.conversation.impl.local_conversation import LocalConversation


def respond(*args, **kwargs):
    return ModelResponse(
        id="resp",
        choices=[Choices(index=0, finish_reason="stop",
                         message=LiteLLMMessage(role="assistant", content="done"))],
        model="gpt-4o",
        usage=Usage(prompt_tokens=100, completion_tokens=1, total_tokens=101),
    )


def tokens(stats: dict) -> dict:
    return {k: v["accumulated_token_usage"]["prompt_tokens"]
            for k, v in stats["usage_to_metrics"].items()}


def on_disk(conv) -> dict:
    path = Path(conv.state.persistence_dir) / "base_state.json"
    return tokens(json.loads(path.read_text())["stats"])


def in_memory(conv) -> dict:
    return tokens(conv.conversation_stats.model_dump())


def make(root: Path, conversation_id=None):
    return LocalConversation(
        agent=Agent(llm=LLM(model="gpt-4o", api_key=SecretStr("k"), usage_id="agent"), tools=[]),
        workspace=root / "ws", persistence_dir=root / "persist",
        conversation_id=conversation_id, visualizer=None,
    )


with patch("openhands.sdk.llm.llm.litellm_completion", side_effect=respond):
    root = Path(tempfile.mkdtemp())
    conv = make(root)
    conv.send_message("hi")
    conv.run()
    print("after run       memory", in_memory(conv), "disk", on_disk(conv))
    conv.ask_agent("what are you doing?")
    mem, disk = in_memory(conv), on_disk(conv)
    print("after ask       memory", mem, "disk", disk)
    # Reload from what is on disk now (no close(), as after a crash or a second reader).
    resumed = make(root, conv.id)
    reloaded = in_memory(resumed)
    print("after reload    memory", reloaded)
    ok = disk.get("ask-agent-llm") == 100 and reloaded.get("ask-agent-llm") == 100
    print("VERDICT:", "ask usage is durable" if ok else "ask usage is NOT in base_state.json / lost on reload")
    sys.exit(0 if ok else 1)
