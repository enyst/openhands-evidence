# Verification ledger — run 2026-11-19T0931-62124c

Revision `e1b8b60f25084a64412c3a2789a921034fc895c7`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18820.

Checks: 1 — pass 0, fail 1, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F06 | 0 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F06.message-timestamp | TZ=America/New_York stack, conversation start (dummy key), hover user-message label | label 'Just now', tooltip = local send time Nov 19, 2026, 4:32 AM → label '5 hours ago'; tooltip/aria-label 'Nov 18, 2026, 11:32 PM'; browser local time Thu Nov 19 2026 04:32:08 GMT-0500; MessageEvent timestamp 2026-11-19T04:32:00.141054 (naive local); sidebar row '3s'. Reproduced on 2nd conversation a3c0786e after reload (5 hours ago, Nov 18, 2026, 11:32 PM, ts 2026-11-19T04:32:24.77) | fail | known bug #19833 (same mechanism as #19543) | `evidence/F06.message-timestamp/ny-user-tooltip.png` |
