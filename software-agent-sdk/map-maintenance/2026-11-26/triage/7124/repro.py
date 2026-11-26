import os, sys, tempfile
sys.path.insert(0, sys.argv[1])
from mockllm import Mock
from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.terminal import TerminalTool
DSML = ('<｜DSML｜tool_calls>\n<｜DSML｜invoke name="terminal">\n'
        '<｜DSML｜parameter name="command" string="true">echo 42 > answer.txt</｜DSML｜parameter>\n'
        '<｜DSML｜parameter name="security_risk" string="true">LOW</｜DSML｜parameter>\n'
        '</｜DSML｜invoke>\n</｜DSML｜tool_calls>')
m = Mock([{"content": DSML}, {"content": "done"}])
ws = tempfile.mkdtemp(prefix="qa7124-")
llm = LLM(model="openai/deepseek-v4-flash", api_key="test", base_url=m.url, num_retries=0, usage_id="agent")
agent = Agent(llm=llm, tools=[Tool(name=TerminalTool.name)])
conv = Conversation(agent=agent, workspace=ws, visualizer=None)
conv.send_message("Run echo 42 > answer.txt and say done.")
conv.run()
print("status:", conv.state.execution_status.value)
print("llm calls:", len(m.bodies))
print("answer.txt exists:", os.path.exists(os.path.join(ws, "answer.txt")))
print("events:", [type(e).__name__ for e in conv.state.events])
last = [e for e in conv.state.events if type(e).__name__ == "MessageEvent" and e.source == "agent"]
print("agent message starts with:", repr(last[-1].llm_message.content[0].text[:40]) if last else None)
conv.close()
