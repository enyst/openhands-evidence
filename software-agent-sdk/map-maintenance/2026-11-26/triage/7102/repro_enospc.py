"""Repro: a conversation run on a full disk (real ENOSPC from a small tmpfs).

Usage (needs a tiny tmpfs so the disk really fills up):
    sudo mkdir -p /mnt/ohfull && sudo mount -t tmpfs -o size=2m tmpfs /mnt/ohfull
    sudo chown "$USER" /mnt/ohfull
    uv run python repro_enospc.py /mnt/ohfull [sync|async]

Only the LLM provider boundary (litellm completion) is stubbed.
"""

import asyncio
import errno
import json
import os
import sys
import traceback
import uuid

from litellm.types.utils import Choices, Message as LiteLLMMessage, ModelResponse
from pydantic import SecretStr

import openhands.sdk.llm.llm as llm_mod
from openhands.sdk import LLM, Agent, Conversation
from openhands.sdk.conversation.exceptions import ConversationRunError


ROOT = sys.argv[1]
MODE = sys.argv[2] if len(sys.argv) > 2 else "sync"
FILLER = os.path.join(ROOT, "filler.bin")
conv_id = uuid.uuid4()
persist = os.path.join(ROOT, "convs")


def fill_disk():
    with open(FILLER, "wb") as f:
        try:
            while True:
                f.write(b"\0" * 4096)
                f.flush()
        except OSError as e:
            assert e.errno == errno.ENOSPC


def reply(**_):
    msg = LiteLLMMessage(content="all done", role="assistant")
    return ModelResponse(
        id="r1", choices=[Choices(finish_reason="stop", index=0, message=msg)]
    )


def completion(*a, **kw):
    fill_disk()  # disk fills up while the agent is mid-step
    return reply()


async def acompletion(*a, **kw):
    fill_disk()
    return reply()


llm_mod.litellm_completion = completion
llm_mod.litellm_acompletion = acompletion


def make_conv():
    llm = LLM(model="gpt-4o", api_key=SecretStr("k"), usage_id="agent", num_retries=0)
    return Conversation(
        agent=Agent(llm=llm, tools=[]),
        workspace=ROOT,
        persistence_dir=persist,
        conversation_id=conv_id,
        visualizer=None,
    )


def persisted_status():
    d = os.path.join(persist, conv_id.hex)
    with open(os.path.join(d, "base_state.json")) as f:
        status = json.load(f)["execution_status"]
    names = os.listdir(os.path.join(d, "events"))
    return status, sum(n.startswith("event-") for n in names)


conv = make_conv()
conv.send_message("hello")
print("before run: persisted status / event files =", persisted_status())

try:
    if MODE == "sync":
        conv.run()
    else:
        asyncio.run(conv.arun())
    print("run returned normally")
except ConversationRunError as e:
    print("run raised ConversationRunError:", repr(e.__cause__))
except Exception as e:
    print(f"run raised {type(e).__name__} (not ConversationRunError): {e}")
    chain, ctx = [], e
    while ctx is not None:
        frames = traceback.extract_tb(ctx.__traceback__)
        path = " > ".join(
            f"{os.path.basename(f.filename)}:{f.lineno}({f.name})"
            for f in frames
            if "openhands/sdk/conversation" in f.filename
            or "openhands/sdk/agent" in f.filename
        )
        if path:
            chain.append(f"{type(ctx).__name__}: {path}")
        ctx = ctx.__context__
    print("  exception chain (first raised -> last raised):")
    for c in reversed(chain):
        print("   ", c)

print("in-memory status:", conv.state.execution_status.value)
print("persisted status / event files:", persisted_status())
print("ConversationErrorEvent recorded:",
      any(type(e).__name__ == "ConversationErrorEvent" for e in conv.state.events))

try:
    with conv.state:
        _ = conv.state.execution_status  # read-only use of the state lock
    print("read-only `with state:` ok")
except OSError as e:
    print("read-only `with state:` raised:", e)

# Space comes back; reopen the conversation from disk and continue.
os.remove(FILLER)
with conv.state:
    pass
print("same object after space restored: `with state:` ok; persisted =",
      persisted_status()[0])
llm_mod.litellm_completion = lambda *a, **k: reply()


async def _ar(*a, **k):
    return reply()


llm_mod.litellm_acompletion = _ar
conv2 = make_conv()
print("after reopen: status =", conv2.state.execution_status.value)
conv2.send_message("continue")
conv2.run()
print("after rerun: status =", conv2.state.execution_status.value)
print("event types:", [type(e).__name__ for e in conv2.state.events])
