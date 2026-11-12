# Map maintenance pass, 2026-11-12

AI-generated on Engel Nyst's behalf. Both maps of OpenHands/software-agent-sdk were replayed live on
main@9bf835c, on the map PR branch (OpenHands/software-agent-sdk#6753): agent-server 5ff99f1..9bf835c,
SDK 4db1ad7..9bf835c, as full passes.

- `agent-server-report.md`, `sdk-report.md`: rendered from every run of the pass (shards, independent
  re-checks and fix checks), so a bullet can show an early fail and a later pass after its map fix.
- `evidence/<family>-ledger.jsonl`: the final run of each edited family (independent re-check where
  one ran); `evidence/F05.restart-hard-tool-call-*.json` and `evidence/F37.rest-response-parent-*.json`:
  saved exchanges for the new bullets (main and the fix branch of #6783).
- `ui/`: Agent Canvas `F06.reconnect` on this checkout, a restart mid tool call (#6778).
