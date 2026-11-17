"""Repro helper (not a map proof): exception type of LocalConversation.add_mcp_servers
for a stdio server that cannot start, on an initialized agent."""
import json, os, tempfile
from pydantic import SecretStr
from openhands.sdk import Agent, LLM
from openhands.sdk.conversation.impl.local_conversation import LocalConversation
from openhands.sdk.mcp import MCPServer

out = {}
for label, srv in {"bin_true": MCPServer(command="/bin/true"),
                   "missing_exe": MCPServer(command="/nonexistent/qa-missing-bin")}.items():
    d = tempfile.mkdtemp()
    agent = Agent(llm=LLM(model="openai/qa-offline", api_key=SecretStr("x"), base_url="http://127.0.0.1:9/v1"), tools=[])
    conv = LocalConversation(agent=agent, workspace=d, persistence_dir=os.path.join(d, "c"), visualizer=None)
    conv.send_message("hi")  # initializes the agent, no LLM call
    try:
        conv.add_mcp_servers({"x": srv})
        out[label] = None
    except Exception as exc:
        t = type(exc)
        out[label] = {"type": f"{t.__module__}.{t.__qualname__}", "msg": str(exc)[:200],
                      "is_ValueError": isinstance(exc, ValueError),
                      "cause": repr(exc.__cause__)[:200] if exc.__cause__ else None}
    out[label + "_mcp_config_after"] = sorted(conv.agent.mcp_config)
    conv.close()
print(json.dumps(out))
