# Defect B: a runtime-added MCP server's tools lose their `<server>_` prefix after restart / resume

Reproduced: YES. Agent-server 3/3 fresh runs (2 map runs + 1 by hand), SDK 2/2 fresh runs.

## Agent-server, map recipe (twice, fresh)
```sh
cd /home/user/sdk-map-wt; export PATH=...; export AGENT_SERVER_VERIFY_HOME=<scratch>/agent-server-repro-mcp; unset AGENT_SERVER_VERIFY_RUN
python3 <scratch>/reaper.py control-agent-server map run --file F19 --only F19.conversation-mcp-add-restart --fresh --record --keep-going
```
- run 1: <scratch>/agent-server-repro-mcp/20261117-085516-aba0-map-f19 -> xfail (bug predicate `matching eq 0 && kinds.AgentErrorEvent ge 1` held)
- run 2: <scratch>/agent-server-repro-mcp/20261117-085723-e3dd-map-f19 -> xfail (same)
- persisted AgentErrorEvent in both: `Tool 'qa-f19-rs_qa_echo' not found. Available: ['finish', ...]`

## Agent-server, by hand with --save (fresh run 20261117-085614-639a-bugB-hand)
```sh
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new --name bugB-hand --print-run)
PY=/home/user/sdk-map-wt/.venv/bin/python
RS_STUB=$(control-agent-server fixture llm-stub --name qa-rs-stub --step 'tool:qa-rs_qa_echo:{"text":"one"}' --step 'tool:finish:{"message":"QA_RS_ONE"}' --step 'tool:qa-rs_qa_echo:{"text":"two"}' --step 'tool:finish:{"message":"QA_RS_TWO"}' --print-path)
RS_AGENT=$(jq -nc --arg b "$RS_STUB/v1" '{llm: {model: "openai/qa-stub", api_key: "qa-stub-key", base_url: $b, num_retries: 0}, tools: []}')
RS_MCP=$(control-agent-server fixture mcp-server --name qa-rs | jq -c .mcp_server)
RCID=$(control-agent-server conversation start --body-json "$(jq -nc --argjson a "$RS_AGENT" '{agent: $a}')" --no-autotitle --prompt 'First.' --no-run --print-id)
control-agent-server api POST "/api/conversations/$RCID/mcp" --json "$(jq -nc --argjson s "$RS_MCP" '{mcp_servers: {"qa-rs": $s}}')" --expect 200 --save bugB/add
control-agent-server api POST "/api/conversations/$RCID/run" --expect 200
control-agent-server conversation wait "$RCID" --until finished --timeout 90
control-agent-server conversation events "$RCID" --kinds ObservationEvent --contains QA_MCP_ECHO:one --expect-kind ObservationEvent --save bugB/first-call   # matching 1
control-agent-server restart
control-agent-server api GET "/api/conversations/$RCID" --check agent.mcp_config.qa-rs.command eq "$PY" --save bugB/after-restart  # ok: server survives
control-agent-server conversation send "$RCID" --text 'Again.' --wait --until finished --timeout 90
control-agent-server conversation events "$RCID" --kinds ObservationEvent --contains QA_MCP_ECHO:two --expect-kind ObservationEvent --save bugB/second-call  # matching 0, AgentErrorEvent 1
control-agent-server conversation events "$RCID" --kinds AgentErrorEvent --save bugB/agent-error
control-agent-server sink read --name qa-rs-stub --show 4 --save bugB/model-requests
control-agent-server stop
```
AgentErrorEvent: `Tool 'qa-rs_qa_echo' not found. Available: ['finish', 'qa_echo']`.
Tools offered to the model (fixtures/qa-rs-stub.jsonl -> hand-llm-stub-requests.jsonl):
requests 0,1 (before restart): `['finish', 'qa-rs_qa_echo']`; requests 2,3 (after restart): `['finish', 'qa_echo']`.

## SDK (twice, fresh)
```sh
export SDK_VERIFY_HOME=<scratch>/sdk-repro-mcp
export SDK_VERIFY_RUN=$(control-sdk new --field run)
control-sdk program S09/runtime --arg resume
```
Runs 20261117-085336-f02630 and 20261117-085403-066e2f (scripted LLM), identical:
`first_texts` has `echo: one` via `verify_echo`; `persisted_mcp_config: ["verify"]`; after reopening,
`resumed_first_call_tools` = bare names (`echo`, `add`, ...), `resumed_second_call_ok: false`,
`resumed_errors: ["Tool 'verify_echo' not found. Available: ['finish', 'echo', ...]"]`. Program exits 0 (it reports facts;
the map's checks decide).
Program review (.agents/skills/verify-sdk/programs/S09/runtime.py, mode `resume`): creates a persisted LocalConversation
(fixed id, delete_on_close=False), send_message (initializes agent), add_mcp_servers({"verify": stdio fixture}), runs a scripted
call to `verify_echo`, closes, then reopens the same id/persistence_dir with an Agent whose mcp_config is the same single
`verify` server (as persisted) and a scripted call to `verify_echo` again; records the tools of the first resumed LLM call and
AgentErrorEvents. It tests what it claims; the reopen passes the agent config explicitly (the normal resume pattern), which
equals the persisted config, so the result is not an artefact of a changed config.

## Cause
openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py:
- `add_mcp_servers` (1811-1857) starts the new server with `prefixed=True` (line 1837) -> tools `<server>_<tool>`.
- On init/resume the tools are rebuilt from `agent.mcp_config` by `_runtime_mcp_tools` (1649-1716) with
  `prefixed = len(mcp_config) > 1` (line 1675); with a single (added) server the tools come back unprefixed, so the event
  history's name no longer resolves. (Same on the agent server: restart re-creates the LocalConversation.)

## Pre-existing?
No. The `len(mcp_config) > 1` rule existed at 922e1ec^ (line 1674), but runtime additions (`add_mcp_servers`, `prefixed=True`)
and the `/mcp` route were added by #6802 (922e1ec); before it there was no way to get a prefixed single-server tool.

## Evidence (copied here; scanned: no DEEPSEEK key value or sk-... strings; only the dummy `qa-stub-key` of the stub LLM)
maprun1.json, maprun2.json (map run summaries), maprun1-transcript.json, maprun2-transcript.json, maprun1-second-call.json,
maprun2-second-call.json, hand-add.json, hand-first-call.json, hand-after-restart.json, hand-second-call.json,
hand-agent-error.json, hand-model-requests.json, hand-llm-stub-requests.jsonl, sink.json,
sdk-S09-runtime-resume-20261117-085336-f02630.json, sdk-S09-runtime-resume-20261117-085403-066e2f.json
