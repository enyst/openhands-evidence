import sys, json
sys.path.insert(0, sys.argv[1])
from mockllm import Mock
from openhands.sdk import LLM
from openhands.sdk.llm import Message, TextContent
msgs = [Message(role="system", content=[TextContent(text="You are helpful.")]), Message(role="user", content=[TextContent(text="hi")])]
def body_limit(model):
    m = Mock([{"content": "ok"}])
    llm = LLM(model=model, api_key="test", base_url=m.url, max_output_tokens=1234, num_retries=0, usage_id="repro")
    llm.completion(msgs)
    b = m.bodies[-1]
    return {k: b.get(k) for k in ("model", "max_tokens", "max_completion_tokens")}
for model in ("zai/glm-5.3", "openai/glm-4.6"):
    print(model, "drop_params default ->", json.dumps(body_limit(model)))
llm = LLM(model="zai/glm-5.3", api_key="test", base_url="http://127.0.0.1:9/v1", max_output_tokens=1234, drop_params=False, num_retries=0, usage_id="repro")
try:
    llm.completion(msgs); print("drop_params=False: ok")
except Exception as e:
    print("zai/glm-5.3 drop_params=False ->", type(e).__name__, str(e)[:160])
