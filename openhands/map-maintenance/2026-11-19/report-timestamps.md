# Verification ledger — run 2026-11-19T0903-bda48c

Revision `e1b8b60f25084a64412c3a2789a921034fc895c7`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18830.

Checks: 1 — pass 0, fail 1, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F06 | 0 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F06.message-timestamp | Conversation page, user bubble timestamp; stack launched with TZ=America/New_York (desktop 1440x1000) | tooltip shows the local send time (Nov 19, 2026, 4:03 AM EST), relative label 'Just now' → event stamped 2026-11-19T04:03:58 (naive local); tooltip 'Nov 18, 2026, 11:03 PM', label '5 hours ago'; reproduced twice (two conversations). Known issue #19833 | fail | Open issue #19833 (SDK naive local timestamps read as UTC); not a regression in BASE..TARGET | `evidence/F06.message-timestamp/tz-new-york-user-tooltip.png` |
