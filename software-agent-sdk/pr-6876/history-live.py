"""Seed paged history through real server runs, using a scripted provider.

This is a deterministic browser-history control, not real-model evidence.
Run through control-agent-server exec; CONTROL_AGENT_SERVER is its executable.
"""

import json
import logging
import os
import subprocess
import tempfile

from openhands.sdk import LLM, Agent, RemoteConversation
from openhands.sdk.event import MessageEditEvent
from openhands.sdk.workspace import RemoteWorkspace
from pydantic import SecretStr

logging.disable(logging.INFO)
steps = ["reply:QA_HISTORY Which port should the history demo use?"]
steps.extend(
    f"reply:History checkpoint {i:03d}.\n\nThe stable control remains unchanged."
    for i in range(60)
)
steps += [
    'tool:edit_message:{"old_str":"Which port should the history demo use?","new_str":"~~Which port should the history demo use?~~ [Edit: Use port 6060.]"}',
    'tool:finish:{"message":"QA_HISTORY_READY"}',
    'tool:edit_message:{"old_str":"[Edit: Use port 6060.]","new_str":"[Edit: Port 6060 was taken; use 7070.]"}',
    'tool:finish:{"message":"QA_HISTORY_RECONNECTED"}',
]
args = [
    os.environ["CONTROL_AGENT_SERVER"],
    "fixture",
    "llm-stub",
    "--name",
    f"history-{os.getpid()}",
    "--print-path",
]
for step in steps:
    args += ["--step", step]
provider = subprocess.check_output(args, text=True).strip()
workspace = RemoteWorkspace(
    host=os.environ["AGENT_SERVER_URL"],
    api_key=os.environ["SESSION_API_KEY"],
    working_dir=tempfile.mkdtemp(prefix="qa-edit-history-"),
)
agent = Agent(
    llm=LLM(
        model="openai/qa-history",
        api_key=SecretStr("qa-stub-key"),
        base_url=provider + "/v1",
        usage_id="qa-history",
        num_retries=0,
    ),
    tools=[],
)
conv = RemoteConversation(
    agent=agent,
    workspace=workspace,
    visualizer=None,
    tags={"title": "QA paged edit history"},
)
try:
    conv.set_title("QA paged edit history")
    conv.send_message("QA history initial question")
    conv.run()
    for i in range(60):
        conv.send_message(f"Continue checkpoint {i:03d}.")
        conv.run()
    conv.send_message("Use 6060 and annotate the original question.")
    conv.run()
    edits = [
        event for event in conv.state.events if isinstance(event, MessageEditEvent)
    ]
    assert len(edits) == 1 and "6060" in edits[0].text
    print(
        json.dumps(
            {
                "conversation_id": str(conv.id),
                "events": len(conv.state.events),
                "edit_target": edits[0].target_event_id,
                "provider": "scripted",
                "ready": True,
            }
        ),
        flush=True,
    )
finally:
    conv.close()
    workspace.reset_client()
