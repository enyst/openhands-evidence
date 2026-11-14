"""Does a text reply's thinking block keep its signature, and is it replayed?

A local HTTP server answers Anthropic's POST /v1/messages from a script and
records each request body. No API key or network is needed.

Usage: python repro_thinking_signature.py
Prints one JSON object with three cases:
  text            reply = thinking(sig-1) + text, no secret registered
  reasoning_only  reply = thinking(sig-1) only, no secret registered
  secret_elsewhere  a secret is registered but does not occur in the thinking
  secret_in_thinking  the registered secret occurs in the thinking text
"""

import json
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from pydantic import SecretStr

from openhands.sdk import LLM, Agent, Conversation
from openhands.sdk.event import MessageEvent


def anthropic_reply(blocks):
    return {
        "id": "msg_1",
        "type": "message",
        "role": "assistant",
        "model": "claude-sonnet-4-5-20250929",
        "content": blocks,
        "stop_reason": "end_turn",
        "stop_sequence": None,
        "usage": {"input_tokens": 10, "output_tokens": 5},
    }


def thinking(text):
    return {"type": "thinking", "thinking": text, "signature": "sig-1"}


def text(value):
    return {"type": "text", "text": value}


def run_case(replies, secrets=None):
    requests = []
    script = list(replies)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            requests.append(body)
            payload = json.dumps(anthropic_reply(script.pop(0))).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        llm = LLM(
            model="anthropic/claude-sonnet-4-5-20250929",
            base_url=f"http://127.0.0.1:{server.server_port}",
            api_key=SecretStr("not-a-real-key"),
            usage_id="agent",
            num_retries=0,
            stream=False,
            extended_thinking_budget=2000,
            max_output_tokens=4096,
        )
        conversation = Conversation(
            agent=Agent(llm=llm, tools=[]),
            workspace=tempfile.mkdtemp(),
            visualizer=None,
        )
        if secrets:
            conversation.update_secrets(secrets)
        conversation.send_message("first question")
        conversation.run()
        if script:  # one reply left: ask again so the history is sent back
            conversation.send_message("second question")
            conversation.run()
        stored = [
            {"thinking": block.thinking, "signature": block.signature}
            for event in conversation.state.events
            if isinstance(event, MessageEvent) and event.source == "agent"
            for block in event.llm_message.thinking_blocks
            if block.type == "thinking"
        ]
        last = requests[-1]["messages"]
        return {
            "stored_thinking_blocks": stored,
            "requests_made": len(requests),
            "assistant_turns_in_last_request": [
                m["content"] for m in last if m["role"] == "assistant"
            ],
        }
    finally:
        server.shutdown()


result = {
    "text": run_case(
        [[thinking("The user greets me."), text("first answer")], [text("done")]]
    ),
    "reasoning_only": run_case([[thinking("Only thinking, no text.")], [text("done")]]),
    "secret_elsewhere": run_case(
        [[thinking("The user greets me."), text("first answer")], [text("done")]],
        secrets={"TOKEN": "supersecret"},
    ),
    "secret_in_thinking": run_case(
        [[thinking("Use the token supersecret."), text("first answer")], [text("done")]],
        secrets={"TOKEN": "supersecret"},
    ),
}
print(json.dumps(result, indent=2))
