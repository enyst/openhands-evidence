import os, sys, tempfile
from pydantic import SecretStr
from openhands.sdk import LLM, Agent, Conversation
d = tempfile.mkdtemp(prefix="qa7103-")
tpl = os.path.join(d, "qa_system_prompt.j2"); open(tpl, "w").write("You are helpful. {% if %}\n")
agent = Agent(llm=LLM(model="gpt-4o", api_key=SecretStr("k"), usage_id="a"), tools=[], system_prompt_filename=tpl)
conv = Conversation(agent=agent, workspace=d, visualizer=None)
print("constructed ok")
try:
    conv.send_message("hi"); print("send ok")
except Exception as e:
    print("file exists:", os.path.isfile(tpl)); print(f"raised {type(e).__name__}: {e}"); print("context:", repr(e.__context__))
