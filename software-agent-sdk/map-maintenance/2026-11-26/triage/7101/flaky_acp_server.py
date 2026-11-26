"""Minimal stdio ACP server. Stalls (never answers) the method named in
FLAKY_STALL_METHOD on the first launch only (every launch if FLAKY_STALL_ALWAYS
is set); other launches behave normally.
Every request method it receives is appended to FLAKY_LOG."""
import json, os, sys, time

marker, log = os.environ["FLAKY_MARKER"], os.environ["FLAKY_LOG"]
stall = os.environ.get("FLAKY_STALL_METHOD", "initialize")
first_launch = not os.path.exists(marker) or bool(os.environ.get("FLAKY_STALL_ALWAYS"))
open(marker, "a").close()

def send(msg):
    sys.stdout.write(json.dumps(msg) + "\n"); sys.stdout.flush()

for line in sys.stdin:
    msg = json.loads(line)
    if "id" not in msg:
        continue
    method, rid = msg["method"], msg["id"]
    with open(log, "a") as f:
        f.write(f"launch={'first' if first_launch else 'later'} {method}\n")
    if first_launch and method == stall:
        time.sleep(3600)
    if method == "initialize":
        send({"jsonrpc": "2.0", "id": rid, "result": {"protocolVersion": 1,
              "agentInfo": {"name": "flaky-acp", "version": "0.0.1"}}})
    elif method == "session/new":
        send({"jsonrpc": "2.0", "id": rid, "result": {"sessionId": "s1"}})
    elif method == "session/prompt":
        send({"jsonrpc": "2.0", "method": "session/update", "params": {
              "sessionId": "s1", "update": {"sessionUpdate": "agent_message_chunk",
              "content": {"type": "text", "text": "hello from the agent"}}}})
        send({"jsonrpc": "2.0", "id": rid, "result": {"stopReason": "end_turn"}})
    else:
        send({"jsonrpc": "2.0", "id": rid, "result": {}})
