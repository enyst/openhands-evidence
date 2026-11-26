"""Tiny OpenAI-compatible chat-completions stub: records request bodies, answers from a queue."""
import json, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Mock:
    def __init__(self, replies):
        self.replies = list(replies)  # list of message dicts {"content":..., "tool_calls":...}
        self.bodies = []
        mock = self
        class H(BaseHTTPRequestHandler):
            def log_message(self, *a): pass
            def do_POST(self):
                n = int(self.headers.get("content-length", 0))
                body = json.loads(self.rfile.read(n) or b"{}")
                mock.bodies.append(body)
                msg = mock.replies.pop(0) if mock.replies else {"content": "done"}
                msg = {"role": "assistant", **msg}
                out = {"id": "r%d" % len(mock.bodies), "object": "chat.completion", "created": 0,
                       "model": body.get("model", "m"),
                       "choices": [{"index": 0, "finish_reason": "tool_calls" if msg.get("tool_calls") else "stop", "message": msg}],
                       "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
                data = json.dumps(out).encode()
                self.send_response(200); self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(data))); self.end_headers(); self.wfile.write(data)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.url = "http://127.0.0.1:%d/v1" % self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
