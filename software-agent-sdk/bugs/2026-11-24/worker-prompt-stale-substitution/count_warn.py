import logging, sys, re
records = []
class H(logging.Handler):
    def emit(self, r):
        m = r.getMessage()
        if "Default prompt text changed" in m: records.append(m)
logging.getLogger().addHandler(H()); logging.getLogger().setLevel(logging.DEBUG)
import openhands.sdk, openhands.sdk.context.prompts.sections.project as P
print("sdk:", openhands.sdk.__file__); print("project:", P.__file__)
print("warnings at import:", len(records)); [print("  ", m[:150]) for m in records]
from openhands.sdk import Agent
from openhands.sdk.testing import TestLLM
for f in ["system_prompt.j2","system_prompt_planning.j2","system_prompt_project_coordinator.j2","system_prompt_project_worker.j2"]:
    n=len(records)
    a=Agent(llm=TestLLM.from_messages([], model="test-model"), tools=[], system_prompt_filename=f)
    sp=a.static_system_message if hasattr(a,"static_system_message") else a.system_message
    print(f"{f}: new warnings={len(records)-n} prompt_len={len(sp)}")
    if f.endswith("worker.j2"):
        m=re.search(r"<TROUBLESHOOTING>.*?</TROUBLESHOOTING>", sp, re.S)
        open(sys.argv[1],"w").write(m.group(0) if m else "NO BLOCK\n")
print("total warnings:", len(records))
