"""Real-model create/attach/fork and on-disk immutability checks.

Run with control-agent-server exec and DEEPSEEK_API_KEY set privately.
CANVAS_CONVERSATIONS_DIR points at this isolated run's dev_conversations.
The script prints only synthetic fixture observations, never credentials.
"""

import hashlib
import json
import os
import sys
import tempfile
import time
from pathlib import Path

import httpx
from openhands.sdk import LLM, Agent, RemoteConversation
from openhands.sdk.event import ActionEvent, MessageEditEvent, MessageEvent
from openhands.sdk.workspace import RemoteWorkspace
from pydantic import SecretStr

url = os.environ["AGENT_SERVER_URL"]
key = os.environ["SESSION_API_KEY"]
client = httpx.Client(base_url=url, headers={"X-Session-API-Key": key}, timeout=60)


def request(method, path, **kwargs):
    response = client.request(method, path, **kwargs)
    response.raise_for_status()
    return response.json()


def toggle(enabled):
    request(
        "PATCH", "/api/settings/experimental/message_edits", json={"enabled": enabled}
    )


def tools(cid):
    return [
        tool["name"]
        for tool in request("GET", f"/api/conversations/{cid}")["agent"]["tools"]
    ]


original_flags = request("GET", "/api/settings/experimental")
agent = Agent(
    llm=LLM(
        model="deepseek/deepseek-flash",
        api_key=SecretStr(os.environ["DEEPSEEK_API_KEY"]),
        usage_id="qa-remote-message-edits",
        num_retries=1,
    ),
    tools=[],
)
workspace = RemoteWorkspace(
    host=url, api_key=key, working_dir=tempfile.mkdtemp(prefix="qa-edit-remote-")
)
conversations = []
try:
    request(
        "PATCH",
        "/api/settings/experimental/conversation_reactions",
        json={"enabled": False},
    )
    toggle(True)
    assert "openhands.tools.message_edit" not in sys.modules
    conv = RemoteConversation(
        agent=agent,
        workspace=workspace,
        visualizer=None,
        tags={"title": "QA remote edits while disabled"},
    )
    conversations.append(conv)
    assert "edit_message" in tools(conv.id)
    assert "openhands.tools.message_edit" in sys.modules
    conv.send_message(
        "Reply using only finish with exactly: Release uses port 4141. Do not use any other tools."
    )
    conv.run()
    target = next(
        event
        for event in conv.state.events
        if isinstance(event, ActionEvent)
        and event.tool_name == "finish"
        and "4141" in event.action.message
    )
    directory = Path(os.environ["CANVAS_CONVERSATIONS_DIR"]) / conv.id.hex / "events"
    original_file = next(directory.glob(f"*-{target.id}.json"))
    original_bytes = original_file.read_bytes()
    toggle(False)
    conv.send_message(
        "4141 was wrong; use 5151. Call edit_message once to strike your earlier finish answer and add an Edit note with 5151. Then finish with OK. Use no other tools."
    )
    conv.run()
    edits = [
        event for event in conv.state.events if isinstance(event, MessageEditEvent)
    ]
    assert len(edits) == 1 and edits[0].target_event_id == target.id
    assert "5151" in edits[0].text
    assert original_file.read_bytes() == original_bytes
    edit_file = next(directory.glob(f"*-{edits[0].id}.json"))
    assert json.loads(edit_file.read_text())["target_event_id"] == target.id
    print(
        json.dumps(
            {
                "check": "create-auto-registration-and-edit-while-off",
                "pass": True,
                "original_file_sha256": hashlib.sha256(original_bytes).hexdigest(),
                "original_file_unchanged": True,
                "separate_edit_file": True,
                "conversation_id": str(conv.id),
            },
            sort_keys=True,
        )
    )
    cid = conv.id
    conv.close()
    attached = RemoteConversation(
        agent=agent, workspace=workspace, conversation_id=cid, visualizer=None
    )
    conversations.append(attached)
    assert "edit_message" in tools(cid)
    assert any(isinstance(event, MessageEditEvent) for event in attached.state.events)
    fork = attached.fork(title="QA remote edit fork")
    conversations.append(fork)
    assert "edit_message" in tools(fork.id)
    assert any(
        isinstance(event, MessageEditEvent) and "5151" in event.text
        for event in fork.state.events
    )
    off = RemoteConversation(
        agent=agent,
        workspace=workspace,
        visualizer=None,
        tags={"title": "QA fresh off control"},
    )
    conversations.append(off)
    assert "edit_message" not in tools(off.id)
    off.send_message("Reply with exactly QA_OFF_CONTROL. Do not use any tools.")
    off.run()
    assert not any(isinstance(event, MessageEditEvent) for event in off.state.events)
    assert any(
        isinstance(event, MessageEvent)
        and "QA_OFF_CONTROL" in str(event.llm_message.content)
        for event in off.state.events
    )
    print(
        json.dumps(
            {
                "check": "attach-fork-new-off-control",
                "pass": True,
                "fork_id": str(fork.id),
                "off_id": str(off.id),
            },
            sort_keys=True,
        )
    )
    child_data = request(
        "POST",
        f"/api/conversations/{cid}/children",
        json={
            "task": "Reply using only finish with exactly: Child uses port 6161. Do not use any other tools.",
            "title": "QA inherited message edits",
            "isolation": "shared",
        },
    )
    child_id = child_data["conversation_id"]
    deadline = time.monotonic() + 120
    while (
        request("GET", f"/api/conversations/{child_id}")["execution_status"]
        != "finished"
    ):
        assert time.monotonic() < deadline, "child did not finish"
        time.sleep(0.5)
    assert "edit_message" in tools(child_id)
    child = RemoteConversation(
        agent=agent, workspace=workspace, conversation_id=child_id, visualizer=None
    )
    conversations.append(child)
    child.send_message(
        "6161 was wrong; use 7171. Call edit_message once to strike your earlier finish answer and add an Edit note with 7171. Then finish with OK. Use no other tools."
    )
    child.run()
    assert any(
        isinstance(event, MessageEditEvent) and "7171" in event.text
        for event in child.state.events
    )
    print(
        json.dumps(
            {
                "check": "child-inherits-tool-while-global-off",
                "pass": True,
                "child_id": child_id,
            },
            sort_keys=True,
        )
    )
    from openhands.tools.preset.planning import get_planning_agent

    toggle(True)
    planner = RemoteConversation(
        agent=get_planning_agent(agent.llm),
        workspace=workspace,
        visualizer=None,
        tags={"title": "QA planning message edits"},
    )
    conversations.append(planner)
    assert "edit_message" in tools(planner.id)
    planner.send_message(
        "Reply using only finish with exactly: Plan uses port 8181. Do not use any other tools."
    )
    planner.run()
    planner.send_message(
        "8181 was wrong; use 9191. Call edit_message once to strike your earlier finish answer and add an Edit note with 9191. Then finish with OK. Use no other tools."
    )
    planner.run()
    assert any(
        isinstance(event, MessageEditEvent) and "9191" in event.text
        for event in planner.state.events
    )
    print(
        json.dumps(
            {
                "check": "planning-agent-edits-finish",
                "pass": True,
                "planner_id": str(planner.id),
            },
            sort_keys=True,
        )
    )
finally:
    for conversation in conversations:
        conversation.close()
    workspace.reset_client()
    for feature in original_flags:
        request(
            "PATCH",
            f"/api/settings/experimental/{feature['key']}",
            json={"enabled": feature["enabled"]},
        )
    client.close()
