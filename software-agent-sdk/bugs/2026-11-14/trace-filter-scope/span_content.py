"""Which spans of one traced conversation carry reply reasoning, a quoted
credential, the LLM api key, or a registered conversation secret.

Usage: span_content.py content|secret     (optional env: LMNR_INSTRUMENTS)
No provider key, no tracing backend: a local HTTP server plays the
OpenAI-compatible provider and the OTLP sink; spans are read in-process.
"""

import json
import os
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REASONING = "private chain of thought"
CREDENTIAL = "tok-span-123"
API_KEY = "sk-span-key"
SECRET = "regsecret-7f3a9c1e55"
mode = sys.argv[1]

if mode == "content":
    replies = [
        {"content": "One.", "reasoning_content": REASONING,
         "tool": ("terminal", {"command": "echo one"})},
        {"tool": ("finish", {"message": "done"})},
    ]
else:
    replies = [
        {"content": "Printing it.",
         "tool": ("terminal", {"command": "echo deploy=$DEPLOY_TOKEN"})},
        {"tool": ("finish", {"message": "done"})},
    ]
calls = []


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if "chat/completions" not in self.path:  # OTLP export: accept, discard
            self.send_response(200)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        calls.append(json.loads(body))
        r = replies[min(len(calls), len(replies)) - 1]
        msg = {"role": "assistant", "content": r.get("content")}
        if "reasoning_content" in r:
            msg["reasoning_content"] = r["reasoning_content"]
        name, args = r["tool"]
        msg["tool_calls"] = [{
            "id": f"call_{len(calls)}", "type": "function",
            "function": {"name": name, "arguments": json.dumps(args)},
        }]
        out = json.dumps({
            "id": f"chatcmpl-{len(calls)}", "object": "chat.completion",
            "created": 1, "model": "gpt-4o-mini",
            "choices": [{"index": 0, "message": msg, "finish_reason": "tool_calls"}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 20,
                      "total_tokens": 120},
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{server.server_port}"

# Tracing on, the documented way: an OTLP endpoint in the environment.
os.environ["OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"] = f"{url}/v1/traces"
os.environ["OTEL_EXPORTER_OTLP_TRACES_PROTOCOL"] = "http/protobuf"
os.environ["OTEL_EXPORTER"] = "otlp_http"

from pydantic import SecretStr  # noqa: E402

from openhands.sdk import LLM, Agent, Conversation, Tool  # noqa: E402
from openhands.sdk.observability.laminar import maybe_init_laminar  # noqa: E402
from openhands.tools.terminal import TerminalTool  # noqa: E402

maybe_init_laminar()
from lmnr import Laminar  # noqa: E402
from lmnr.opentelemetry_lib.tracing import TracerWrapper  # noqa: E402
from opentelemetry.sdk.trace.export import SimpleSpanProcessor  # noqa: E402
from opentelemetry.sdk.trace.export.in_memory_span_exporter import (  # noqa: E402
    InMemorySpanExporter,
)

assert Laminar.is_initialized()
exporter = InMemorySpanExporter()
# Every span Laminar's tracer provider ends is also copied here.
TracerWrapper()._tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))

llm = LLM(model="openai/gpt-4o-mini", base_url=f"{url}/v1",
          api_key=SecretStr(API_KEY), usage_id="agent", num_retries=1)
agent = Agent(llm=llm, tools=[Tool(name=TerminalTool.name)])
conversation = Conversation(agent=agent, workspace=tempfile.mkdtemp(),
                            visualizer=None)
if mode == "content":
    conversation.send_message('trace this with {"api_token": "%s"}' % CREDENTIAL)
else:
    conversation.update_secrets({"DEPLOY_TOKEN": SECRET})
    conversation.send_message("Print the deploy token variable.")
conversation.run()
status = conversation.state.execution_status.value
events_text = json.dumps(
    [e.model_dump(mode="json") for e in conversation.state.events], default=str)
conversation.close()
Laminar.flush()

spans = exporter.get_finished_spans()


def where(needle):
    """{span name: sorted attribute keys whose value contains needle}"""
    found = {}
    for s in spans:
        keys = sorted(k for k, v in (s.attributes or {}).items() if needle in str(v))
        if keys:
            found.setdefault(s.name, set()).update(keys)
    return {n: sorted(k) for n, k in sorted(found.items())}


names = {}
for s in spans:
    names[s.name] = names.get(s.name, 0) + 1
llm_inputs = [str(s.attributes.get("gen_ai.input.messages") or "")
              for s in spans if s.name.startswith("llm.")]
result = {
    "mode": mode,
    "LMNR_INSTRUMENTS": os.environ.get("LMNR_INSTRUMENTS"),
    "status": status,
    "provider_calls": len(calls),
    "span_names": names,
    "llm_spans_with_gen_ai_input": sum(1 for i in llm_inputs if i),
    "llm_span_has_redacted_marker": any("<redacted>" in i for i in llm_inputs),
    "api_key": where(API_KEY),
}
if mode == "content":
    result["reasoning"] = where(REASONING)
    result["credential"] = where(CREDENTIAL)
else:
    result["secret"] = where(SECRET)
    result["secret_in_conversation_events"] = SECRET in events_text
    result["secret_in_requests_to_provider"] = SECRET in json.dumps(calls)
    result["mask_in_conversation_events"] = "<secret-hidden>" in events_text
print(json.dumps(result, indent=2))
server.shutdown()
