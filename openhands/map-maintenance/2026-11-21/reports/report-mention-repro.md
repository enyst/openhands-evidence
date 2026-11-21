# Verification ledger — run 2026-11-21T1318-d4bdc6

Revision `455cc3ad3ea45b0bafaffca490476ee5fbeb7f73`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 1 — pass 0, fail 1, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F00 | 0 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F00.mention-dashless | click testid=conversation-mention in B -> /conversations/f5532466b7fd44a7beb3fe3d928143fa | same as /conversations/<dashed>: sidebar row aria-current/highlight, Initialized session group → x2: no sidebar row aria-current/data-active, no Initialized session group; dashed route shows both | fail | repro for candidate defect; live user message on dashless route does render | `evidence/F00.mention-dashless/run1-dashless.png` |
