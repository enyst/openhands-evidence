"""Exact tool rejection controls through a real server and scripted provider."""

import json
import logging
import os
import subprocess
import tempfile

import httpx
from openhands.sdk import LLM, Agent, RemoteConversation
from openhands.sdk.agent.acp_agent import ACPAgent
from openhands.sdk.event import MessageEditEvent, ObservationEvent
from openhands.sdk.workspace import RemoteWorkspace
from pydantic import SecretStr

logging.disable(logging.INFO)
steps = [
    "reply:QA_DUP repeated repeated. QA_UNIQUE Port 3001.",
    'tool:edit_message:{"old_str":"","new_str":"replacement"}',
    'tool:edit_message:{"old_str":"Port 3001.","new_str":"Port 3001."}',
    'tool:edit_message:{"old_str":"QA_USER_ONLY_NEVER_AGENT","new_str":"replacement"}',
    'tool:edit_message:{"old_str":"repeated","new_str":"replacement"}',
    'tool:edit_message:{"old_str":"Port 3001.","new_str":"Port 3002."}',
    'tool:edit_message:{"old_str":"Port 3001.","new_str":"Port 9999."}',
    'tool:finish:{"message":"QA_FAILURE_CONTROLS_DONE"}',
]
args = [
    os.environ["CONTROL_AGENT_SERVER"],
    "fixture",
    "llm-stub",
    "--name",
    f"failures-{os.getpid()}",
    "--print-path",
]
for step in steps:
    args += ["--step", step]
provider = subprocess.check_output(args, text=True).strip()
workspace = RemoteWorkspace(
    host=os.environ["AGENT_SERVER_URL"],
    api_key=os.environ["SESSION_API_KEY"],
    working_dir=tempfile.mkdtemp(prefix="qa-edit-failures-"),
)
agent = Agent(
    llm=LLM(
        model="openai/qa-failures",
        api_key=SecretStr("qa-stub-key"),
        base_url=provider + "/v1",
        usage_id="qa-failures",
        num_retries=0,
    ),
    tools=[],
)
conv = RemoteConversation(
    agent=agent,
    workspace=workspace,
    visualizer=None,
    tags={"title": "QA edit rejection controls"},
)
try:
    conv.set_title("QA edit rejection controls")
    conv.send_message("QA_USER_ONLY_NEVER_AGENT")
    conv.run()
    conv.send_message("Exercise the planned fixture controls.")
    conv.run()
    edits = [
        event for event in conv.state.events if isinstance(event, MessageEditEvent)
    ]
    results = [
        event.observation
        for event in conv.state.events
        if isinstance(event, ObservationEvent) and event.tool_name == "edit_message"
    ]
    assert [result.is_error for result in results] == [
        True,
        True,
        True,
        True,
        False,
        True,
    ]
    expected = [
        "empty",
        "nothing to edit",
        "not in any",
        "occurs 2 times",
        "Edited.",
        "not in any",
    ]
    assert all(
        fragment in result.text
        for fragment, result in zip(expected, results, strict=True)
    )
    assert (
        len(edits) == 1
        and edits[0].text == "QA_DUP repeated repeated. QA_UNIQUE Port 3002."
    )
    print(
        json.dumps(
            {
                "check": "empty-unchanged-user-only-ambiguous-stale-controls",
                "pass": True,
                "errors": 5,
                "successful_edits": 1,
                "conversation_id": str(conv.id),
                "provider": "scripted",
            }
        )
    )
    with httpx.Client(
        base_url=os.environ["AGENT_SERVER_URL"],
        headers={"X-Session-API-Key": os.environ["SESSION_API_KEY"]},
    ) as client:
        response = client.post(
            "/api/conversations",
            json={
                "agent": ACPAgent(acp_command=["echo"]).model_dump(
                    mode="json", exclude_none=True
                ),
                "workspace": {"working_dir": workspace.working_dir},
                "tags": {"title": "QA ACP no injected edit tool"},
            },
        )
        response.raise_for_status()
        cid = response.json()["id"]
        response = client.get(f"/api/conversations/{cid}")
        response.raise_for_status()
        data = response.json()
        assert data["agent"]["kind"] == "ACPAgent"
        assert "edit_message" not in [tool["name"] for tool in data["agent"]["tools"]]
        print(
            json.dumps(
                {
                    "check": "acp-not-injected-with-flag-on",
                    "pass": True,
                    "real_acp_model_run": False,
                }
            )
        )
finally:
    conv.close()
    workspace.reset_client()
