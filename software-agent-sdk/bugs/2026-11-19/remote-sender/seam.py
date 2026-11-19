"""RemoteConversation.send_message(sender=...) vs LocalConversation, same SDK."""
import json, os, tempfile
from pydantic import SecretStr
from openhands.sdk import LLM, Agent, Conversation
from openhands.sdk.event import MessageEvent
from openhands.sdk.workspace import RemoteWorkspace

def agent():
    # Never called: no run happens. Unreachable endpoint, dummy key.
    return Agent(llm=LLM(model="openai/qa-seam", api_key=SecretStr("sk-qa-seam"),
                         base_url="http://127.0.0.1:9/v1", usage_id="qa-seam"), tools=[])

def senders(events):
    return [(e.sender, e.llm_message.content[0].text) for e in events
            if isinstance(e, MessageEvent) and e.source == "user"]

out = {}
with tempfile.TemporaryDirectory() as d:
    local = Conversation(agent=agent(), workspace=d, persistence_dir=os.path.join(d, "p"))
    local.send_message("QA_SEAM_LOCAL", sender="goal")
    out["local"] = senders(local.state.events)
    local.close()

ws = RemoteWorkspace(host=os.environ["AGENT_SERVER_URL"], api_key=os.environ["SESSION_API_KEY"],
                     working_dir=os.environ["F"])
remote = Conversation(agent=agent(), workspace=ws)
remote.send_message("QA_SEAM_REMOTE", sender="goal")
out["remote_conversation_id"] = str(remote.id)
out["remote"] = senders(list(remote.state.events))
remote.close()
print("SEAM_RESULT " + json.dumps(out))
