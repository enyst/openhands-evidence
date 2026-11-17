# Defect A: POST /api/conversations/{id}/mcp answers 500 when the added stdio server cannot start

Reproduced: YES, 2/2 fresh agent-server runs (TARGET 0275e714 in /home/user/sdk-map-wt), plus SDK 2/2.

## Agent-server commands (each run on a fresh `launch --new`)
```sh
cd /home/user/sdk-map-wt
export PATH=$PWD/.agents/skills/verify-agent-server/scripts:$PWD/.agents/skills/verify-sdk/scripts:$PATH
export AGENT_SERVER_VERIFY_HOME=<scratch>/agent-server-repro-mcp
export AGENT_SERVER_VERIFY_RUN=$(control-agent-server launch --new --name bugA1 --print-run)
control-agent-server llm preset deepseek
CID=$(control-agent-server conversation start --prompt 'Reply with just: ok' --wait --print-id)
control-agent-server api POST /api/conversations/$CID/mcp --json '{"mcp_servers":{"x":{"command":"/bin/true"}}}' --save bugA/start-failure
control-agent-server api POST /api/conversations/$CID/mcp --json '{"mcp_servers":{"y":{"command":"/nonexistent/qa-missing-bin"}}}' --save bugA/missing-exe
# run 2 only, contrast: the route's own refusal is 400
control-agent-server api POST /api/conversations/$CID/mcp --json '{"mcp_servers":{"z":{"url":"http://127.0.0.1:9/sse","transport":"sse"}}}' --save bugA/contrast-sse-400
control-agent-server api GET /api/conversations/$CID --check agent.mcp_config.x missing --check agent.mcp_config.y missing --save bugA/get-after
control-agent-server stop
```

## Results
| run | /bin/true | missing executable | SSE (contrast) | GET after |
|---|---|---|---|---|
| bugA1 (20261117-085215-5c1c-bugA1) | 500 `{"detail":"Internal Server Error","exception":"Connection closed"}` | 500 `exception: "MCP Connection Failure"` | - | x, y absent from agent.mcp_config (checks pass) |
| bugA2 (20261117-085301-348a-bugA2) | 500 `Connection closed` | 500 `MCP Connection Failure` | 400 `Runtime MCP additions do not support SSE transport: z` | x, y absent |

Server log: `Unhandled exception on POST /api/conversations/<id>/mcp ... [MCPError ...]`.
The server is NOT added (only the status is wrong); the stdio child is not left in mcp_config.

## SDK (LocalConversation.add_mcp_servers), same inputs
Helper `sdk_add_failure.py` (repro helper only, not a map proof) run with
`control-sdk exec --run <sdk run> -- python <scratch>/bugs/A/sdk_add_failure.py` on both SDK runs
(sdk-repro-mcp/runs/20261117-085336-f02630, .../20261117-085403-066e2f), identical results:
- `/bin/true` -> `mcp.shared.exceptions.MCPError: Connection closed` (not a ValueError)
- missing exe -> `openhands.sdk.mcp.exceptions.MCPError: MCP Connection Failure` (cause `RuntimeError("Client failed to connect: [Errno 2] No such file or directory ...")`), not a ValueError
- agent.mcp_config stays `[]` after both.
`control-sdk program S09/runtime --arg add` (both runs, exit 0): `start_failure_error = "MCPError: Connection closed"`
(the program's `--fail-start` server), vs `duplicate_error`/`sse_error` = `ValueError: ...`.

## Cause
- openhands-agent-server/openhands/agent_server/conversation_router.py:529-553 (`add_conversation_mcp_servers`): only
  `except ValueError -> Invalid (400)`; any other exception is a 500.
- event_service.py:2305-2311 `add_mcp_servers` passes exceptions through from the executor.
- openhands-sdk/openhands/sdk/conversation/impl/local_conversation.py:1830-1842 (`add_mcp_servers`): `_start_runtime_mcp_server`
  errors (`MCPError` from the mcp library / openhands.sdk.mcp.client:85) are re-raised as-is, not as ValueError.

## Pre-existing?
No. Introduced by #6802 (922e1ec): at 922e1ec^ none of conversation_router.py, event_service.py, local_conversation.py contain
`add_mcp_servers` or the `/mcp` route (`git show 922e1ec^:<file> | grep -c 'add_mcp_servers\|/mcp"'` = 0; at 922e1ec = 2/2/1).

## Evidence (copied here; redacted, scanned: DEEPSEEK_API_KEY value not present, no sk-... strings; llm.api_key is null)
run1-start-failure.json, run1-missing-exe.json, run1-get-after.json, run2-start-failure.json, run2-missing-exe.json,
run2-contrast-sse-400.json, run2-get-after.json, sdk-S09-runtime-add-<run>.json (2)
Originals: <scratch>/agent-server-repro-mcp/20261117-085215-5c1c-bugA1/evidence/bugA/, .../20261117-085301-348a-bugA2/evidence/bugA/
