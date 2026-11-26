# count?status vs search?status on a damaged store

Script: `repro.sh` (three conversations with an offline model, no run; stop; delete B's
`base_state.json`; make C's `meta.json` invalid; restart). Driven with `control-agent-server`
from `.agents/skills/verify-agent-server/scripts` on a fresh `launch --new` run.

## TARGET main@d7263334 (2026-11-26)

| request | result |
|---|---|
| `GET /api/conversations/search` | 200, `items` 1 (A), `broken_items` [C `metadata`, B `state`] |
| `GET /api/conversations/count` | 3 (= 1 item + 2 broken) |
| `GET /api/conversations/count?status=idle` | **2** |
| `GET /api/conversations/search?status=idle` | **`items` 1, `broken_items` 0** |
| `GET /api/conversations/search?limit=1` | `items` 0, `broken_items` 1, `next_page_id` set |
| `DELETE` B, `DELETE` C | 200, 200; count afterwards 1 |

## BASE main@0988e976

| request | result |
|---|---|
| `GET /api/conversations/count` | 2 |
| `GET /api/conversations/count?status=idle` | **2** |
| `GET /api/conversations/search?status=idle` | **`items` 1** |
| `DELETE` B, `DELETE` C | 500, 404 (#7079, fixed by #7080) |

The filtered mismatch exists on both commits: it is not a regression from #7080.
