# #6926 evidence: POST /api/conversations/{id}/mcp start failure, 500 -> 400

Fix commit: 73c0e178f on claude/fix-6926-mcp (base main 0275e714d).
Before = /home/user/software-agent-sdk at 0275e714d; after = /home/user/sdk-fix-6926.

## Agent-server map bullet `F19.conversation-mcp-add-start-failure` (2 fresh runs each)
`control-agent-server map run --file F19 --only F19.conversation-mcp-add-start-failure --fresh --repeat 2 --checkout <tree>`

| tree | run | result | response |
|---|---|---|---|
| main | 20261117-091154-a12b | xfail | 500 `{"detail":"Internal Server Error","exception":"Connection closed"}` (main-run1-add.json) |
| main | 20261117-091212-553a | xfail | 500, same (main-run2-add.json) |
| fix | 20261117-091230-3b5d | xpass | 400 `{"detail":"Could not start MCP server qa-f19-dies: Connection closed"}` (fix-run1-add.json) |
| fix | 20261117-091250-8669 | xpass | 400, same (fix-run2-add.json) |

Summaries: map-run-main.json, map-run-fix.json.
Server log: main has `Unhandled exception on POST ...` (main-run1-server-log-unhandled.txt); the fixed
runs have none (fix-server-log-unhandled-counts.txt: 0, 0, 0).

## Manual, fixed server (run 20261117-091325-7633-fix6926-manual)
- missing executable -> 400 `Could not start MCP server y: Client failed to connect: [Errno 2] No such file or directory: '/nonexistent/qa-missing-bin'` (fix-manual-missing-exe.json)
- GET afterwards: `agent.mcp_config` is `{}` (y and qa-f19-dies absent; fix-manual-get-after.json)

## SDK, verify-sdk program S09/runtime add (2 runs each, the tree's own python)
- main: `start_failure_error = "MCPError: Connection closed"` (sdk-S09-runtime-add-main-{1,2}.json)
- fix: `start_failure_error = "MCPServerStartError: Could not start MCP server broken: Connection closed"` (sdk-S09-runtime-add-fix-{1,2}.json)

Scanned: no DEEPSEEK_API_KEY value, no sk-... strings (the agent in the map recipe uses the fake `qa-offline-key`).
