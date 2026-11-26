"""One transient 502 on the automation completion callback: is it retried?"""
import json, os, threading, logging
from http.server import BaseHTTPRequestHandler, HTTPServer
received = []
class FlakyGateway(BaseHTTPRequestHandler):
    def do_POST(self):
        received.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
        self.send_response(502 if len(received) == 1 else 200); self.end_headers()
    def log_message(self, *a): pass
server = HTTPServer(("127.0.0.1", 0), FlakyGateway)
threading.Thread(target=server.serve_forever, daemon=True).start()
os.environ["AUTOMATION_CALLBACK_URL"] = f"http://127.0.0.1:{server.server_port}/api/automation/v1/runs/qa-run/complete"
os.environ["AUTOMATION_RUN_ID"] = "qa-run"; os.environ["SANDBOX_ID"] = "sbx"; os.environ["SESSION_API_KEY"] = "qa-sess"
from openhands.workspace import OpenHandsCloudWorkspace
logs = []
class H(logging.Handler):
    def emit(self, r): logs.append(r.getMessage())
logging.getLogger().addHandler(H()); logging.getLogger().setLevel(logging.INFO)
ws = OpenHandsCloudWorkspace(local_agent_server_mode=True, cloud_api_url="http://127.0.0.1:1", cloud_api_key="qa-user-key", keep_alive=True)
with ws as w:
    w.register_conversation("conv-123"); w.register_cost(0.42)
server.shutdown()
print("callback POSTs received:", len(received))
print("first body:", json.dumps({k: received[0].get(k) for k in ("status", "conversation_id", "cost")}) if received else None)
print("callback log lines:", [l for l in logs if "allback" in l])
