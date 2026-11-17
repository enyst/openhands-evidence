# #6927 evidence: tools of an MCP server added at runtime keep their `<server>_` prefix across restart and resume

Branch `claude/fix-6927-mcp` (worktree /home/user/sdk-fix-6927). "main" means 0275e714 (the /home/user/sdk-map-wt checkout, whose SDK and agent-server sources are identical to main).
Files were scanned for API keys: none found. The only key is the stub LLM's dummy `qa-stub-key`.

## Agent server: `F19.conversation-mcp-add-restart`
`control-agent-server map run --file F19 --only F19.conversation-mcp-add-restart --fresh --repeat 2 --checkout <tree>`, run under reaper.py.

| tree | run | result | tools offered to the model (4 stub requests: 2 before restart, 2 after) |
|---|---|---|---|
| main | 20261117-092237-731f | xfail | `qa-f19-rs_qa_echo` x2, then `qa_echo` x2 |
| main | 20261117-092343-03cc | xfail | same |
| fix  | 20261117-092449-4839 | xpass | `qa-f19-rs_qa_echo` x4 |
| fix  | 20261117-092546-a42e | xpass | same |

- Map summaries: `agent-server-map-main.json` and `agent-server-map-fix.json`.
- Per run:
  - `*-llm-stub-requests.jsonl`: the requests the model received.
  - `*-after-restart.json`: the server is still in `agent.mcp_config` after the restart.
  - `*-second-call.json`: on main there is no `QA_MCP_ECHO:two` observation. On the fix, `qa-f19-rs_qa_echo` returns `QA_MCP_ECHO:two` with `is_error: false`.

## SDK: `S09.runtime-add-resume`
`control-sdk program S09/runtime --arg resume` with the map's checks, run with each tree's python.
- `sdk-S09-runtime-main-{1,2}.json`: the checks `resumed_first_call_tools contains verify_echo` and `resumed_second_call_ok eq true` fail. The tools come back as bare `echo`, `add`, ..., and `resumed_errors` = `Tool 'verify_echo' not found`.
- `sdk-S09-runtime-fix-{1,2}.json`: all checks pass. The tools are `verify_*`, `resumed_second_call_ok: true`, and `resumed_errors: []`.
- `sdk-S09-runtime-fix-add.json`: `S09.runtime-add-servers` passes all of its checks on the fix. This includes a server added before the first message still getting bare names (`early_first_call_tools` has `echo`, not `solo_echo`).
