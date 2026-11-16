"""Deterministic real-server control, not real-model evidence.

Run with the SDK worktree's Python and an isolated AGENT_SERVER_VERIFY_RUN.
Set CONTROL_AGENT_SERVER to that worktree's control-agent-server executable.
"""

import json
import os
import subprocess
import sys


CLI = os.environ["CONTROL_AGENT_SERVER"]


def command(*args):
    result = subprocess.run(
        [CLI, *args], text=True, capture_output=True
    )
    if result.returncode:
        print(result.stdout, result.stderr)
        result.check_returncode()
    return result.stdout.strip()


command("doctor")
command(
    "api", "PATCH", "/api/settings/experimental/message_edits",
    "--json", '{"enabled":true}', "--expect", "200",
)
steps = [
    "reply:Question A?",
    "reply:Port revision 0.",
    'tool:edit_message:{"old_str":"Question A?","new_str":"~~Question A?~~ [Edit: Answer A.]"}',
]
for revision in range(1, 102):
    steps.append("tool:edit_message:" + json.dumps({
        "old_str": f"Port revision {revision - 1}.",
        "new_str": f"Port revision {revision}.",
    }))
steps.append('tool:finish:{"message":"Done."}')
args = ["fixture", "llm-stub", "--name", f"pagination-{os.getpid()}", "--print-path"]
for step in steps:
    args += ["--step", step]
provider = command(*args)
agent = {"llm": {
    "model": "openai/qa-pagination", "api_key": "qa-stub-key",
    "base_url": provider + "/v1", "num_retries": 0,
}, "tools": []}
cid = command(
    "conversation", "start", "--no-autotitle", "--body-json",
    json.dumps({"agent": agent, "max_iteration_per_run": 200}),
    "--prompt", "first", "--wait", "--timeout", "120", "--print-id",
)
command("conversation", "send", cid, "--text", "second", "--wait")
command("conversation", "send", cid, "--text", "third", "--wait", "--timeout", "300")
command(
    "api", "GET", f"/api/conversations/{cid}/events/search",
    "--query", "kind=MessageEditEvent", "--check", "items", "len-eq", "100",
    "--check", "next_page_id", "exists", "--save", "pagination/edits-first-page",
)
probe = f"""
import os
from openhands.tools.conversation_mentions import ReadConversationAction
from openhands.tools.conversation_mentions.impl import ReadConversationExecutor
result = ReadConversationExecutor(server_url=os.environ['AGENT_SERVER_URL'])(
    ReadConversationAction(conversation={cid!r}, limit=100)
)
print(result.text)
assert not result.is_error
assert '[agent, edited] ~~Question A?~~ [Edit: Answer A.]' in result.text
assert 'Port revision 101.' in result.text
print('PAGINATION_CONTROL_PASS')
"""
print(command("exec", "--", sys.executable, "-c", probe))
