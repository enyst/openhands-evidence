# Verification ledger — run 2026-11-23T0940-6d44e0

Revision `c5e47c4b4dab1d14724e74675c06254957ccbf47`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 2 — pass 1, fail 0, blocked 1, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 1 | 0 | 1 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F01.locked-cloud-first-run | Cloud login completes |  →  | blocked | Needs OpenHands Cloud account |  |
| F01.locked-cloud-first-run |  | only OpenHands Cloud card with Connect, no progress/close; phone inside viewport → body text 'OpenHands Cloud / Connect instantly to OpenHands Cloud to use Agent Canvas / Connect to OpenHands'; add-backend-close 0; progress bar 0; phone insideViewport true, no overflow | pass | Login (device flow) blocked: needs OpenHands Cloud account | `evidence/F01.locked-cloud-first-run/first-run.png` `evidence/F01.locked-cloud-first-run/phone.png` |
