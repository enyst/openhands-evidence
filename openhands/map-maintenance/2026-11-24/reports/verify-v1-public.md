# Verification ledger — run 2026-11-24T0952-b0e791

Revision `7a9425ac0b1c1a648414fde7af23136c442204ca`, public mode, Agent Server 1.63.1, base http://127.0.0.1:18840.

Checks: 1 — pass 1, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F01.onboarding-backend-step | public mode first run, Add a backend | prefilled Local, Next disabled, wrong key error, right key -> consent alone -> Choose your agent 3 steps no Back, no toast → toast history []; snapshot matches; error 'Could not connect to http://127.0.0.1:18840 / Invalid API key'; consent alone (onboarding-modal 0) naming Local; then step 0 Choose your agent, progress-step-3 0, agent-back 0 | pass |  | `evidence/F01.onboarding-backend-step/fresh.png` `evidence/F01.onboarding-backend-step/consent-alone.png` `evidence/F01.onboarding-backend-step/choose-agent.png` |
