# Verification ledger — run 2026-11-23T0927-edb062

Revision `c5e47c4b4dab1d14724e74675c06254957ccbf47`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18850.

Checks: 1 — pass 1, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F25.version-gate | run with --sdk-version 1.62.0: first run + returning user, desktop and phone | first run: Disconnected only until Next, then Could not connect + 'requires agent-server 1.63.1 or newer; this backend is running 1.62.0' inline and toast; returning: recovery gate without Done/X, v1.62.0 Disconnected; phone in viewport → exactly as expected; testids agent-server-onboarding-screen + manage-backends-modal, no done/close; status detail sentence; phone insideViewport true, no overflow | pass | Minimum raised 1.59.0 -> 1.63.1 in this range (b73d79d #19923); doctor warns below-minimum | `evidence/F25.version-gate/first-run.png` `evidence/F25.version-gate/gate.png` `evidence/F25.version-gate/gate-phone.png` |
