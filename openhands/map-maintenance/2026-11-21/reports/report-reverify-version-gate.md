# Verification ledger — run 2026-11-21T1335-cd5545

Revision `ccf54d45c6fa5fe72fba9c5f507f693dee22af3f`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18820.

Checks: 1 — pass 1, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F25.version-gate | launch --new --sdk-version 1.62.0; first run / then onboard --skip + /conversations | doctor warns below 1.63.1; first-run Disconnected only until Next, then 'Could not connect to <host>' + 'requires agent-server 1.63.1 ... running 1.62.0' inline and toast; returning-user gate agent-server-onboarding-screen + manage-backends-modal without Done/X, row v1.62.0 Disconnected + sentence; phone inside viewport → doctor warning text exact; before Next text has no version; after Next 'Could not connect to http://127.0.0.1:18820' + sentence inline, toasts hold both lines (plus Disconnected inline alert); gate testids present, done/close count 0; status-detail-Local is the sentence; modal text Local v1.62.0 ... Disconnected; phone bbox insideViewport true, pageHorizontalOverflow false | pass |  | `evidence/F25.version-gate/gate.png` `evidence/F25.version-gate/first-run-after-next.png` `evidence/F25.version-gate/gate-phone.png` |
