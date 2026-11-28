import json
from pydantic import SecretStr
from openhands.sdk import LLM
from openhands.sdk.llm.utils.model_features import get_features
out = {}
for m in ["openai/deepseek-v4-1-flash-1017-uncensored", "deepseek-v4-1-flash", "deepseek-v4-1-flash-1017", "deepseek-v4.1-flash", "openai/e2ee-deepseek-v4-1-flash-1017"]:
    f = get_features(m)
    llm = LLM(model=m, api_key=SecretStr("x"), base_url="https://example.invalid/v1", usage_id="c")
    out[m] = {"supports_vision": f.supports_vision, "source": f.sources.get("supports_vision"), "vision_is_active": llm.vision_is_active()}
print(json.dumps(out, indent=1))
