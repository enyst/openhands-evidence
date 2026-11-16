"""Same-response edit conflict through real HTTP/agent execution; scripted LLM."""

import json
import logging
import os
import subprocess
import tempfile

from openhands.sdk import LLM, Agent, RemoteConversation
from openhands.sdk.event import MessageEditEvent, ObservationEvent
from openhands.sdk.workspace import RemoteWorkspace
from pydantic import SecretStr

logging.disable(logging.INFO)
calls = []
for i, (old, new) in enumerate(
    [
        ("3000", "8080"),
        ("alpha", "beta"),
        ("Tests pass.", "~~Tests pass.~~"),
    ]
):
    calls.append(
        {
            "id": f"call_qa_batch_{i}",
            "type": "function",
            "function": {
                "name": "edit_message",
                "arguments": json.dumps({"old_str": old, "new_str": new}),
            },
        }
    )
completion = {
    "id": "chatcmpl-qa-batch",
    "object": "chat.completion",
    "created": 1,
    "model": "qa-batch",
    "choices": [
        {
            "index": 0,
            "finish_reason": "tool_calls",
            "message": {"role": "assistant", "content": None, "tool_calls": calls},
        }
    ],
    "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
}
steps = [
    "reply:Port is 3000. Host is alpha.",
    "reply:Tests pass.",
    "status:200:" + json.dumps(completion),
    'tool:edit_message:{"old_str":"alpha","new_str":"beta"}',
    'tool:finish:{"message":"QA_BATCH_DONE"}',
]
args = [
    os.environ["CONTROL_AGENT_SERVER"],
    "fixture",
    "llm-stub",
    "--name",
    f"batch-{os.getpid()}",
    "--print-path",
]
for step in steps:
    args += ["--step", step]
provider = subprocess.check_output(args, text=True).strip()
workspace = RemoteWorkspace(
    host=os.environ["AGENT_SERVER_URL"],
    api_key=os.environ["SESSION_API_KEY"],
    working_dir=tempfile.mkdtemp(prefix="qa-edit-batch-"),
)
agent = Agent(
    llm=LLM(
        model="openai/qa-batch",
        api_key=SecretStr("qa-stub-key"),
        base_url=provider + "/v1",
        usage_id="qa-batch",
        num_retries=0,
        stream=False,
    ),
    tools=[],
)
conv = RemoteConversation(agent=agent, workspace=workspace, visualizer=None)
try:
    conv.set_title("QA same-response edit conflict")
    for prompt in ["First message", "Second message", "Apply the scripted batch"]:
        conv.send_message(prompt)
        conv.run()
    edits = [
        event for event in conv.state.events if isinstance(event, MessageEditEvent)
    ]
    results = [
        event.observation
        for event in conv.state.events
        if isinstance(event, ObservationEvent) and event.tool_name == "edit_message"
    ]
    assert [result.is_error for result in results] == [False, True, False, False]
    assert "already edits this message" in results[1].text
    assert [event.text for event in edits] == [
        "Port is 8080. Host is alpha.",
        "~~Tests pass.~~",
        "Port is 8080. Host is beta.",
    ]
    assert (
        edits[0].target_event_id == edits[2].target_event_id != edits[1].target_event_id
    )
    print(
        json.dumps(
            {
                "check": "same-response-conflict-distinct-target-and-next-response-retry",
                "pass": True,
                "successful_edits": 3,
                "conflict_errors": 1,
                "conversation_id": str(conv.id),
                "provider": "scripted",
            }
        )
    )
finally:
    conv.close()
    workspace.reset_client()
