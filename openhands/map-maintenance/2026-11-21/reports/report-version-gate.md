# Verification ledger — run 2026-11-21T1245-eb9bfb

Revision `0f4cb6af95915fee776913c4aa8694e7c4b76033`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18830.

Checks: 3 — pass 3, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 1 | 0 | 0 | 0 | 0 | 0 |
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |
| F26 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F01.onboarding-backend-step | fresh browser on launch --new --sdk-version 1.62.0, goto /, click Next on Check your backend | first run on an old server explains the refusal → step 0 'Check your backend' shows Disconnected / 'Update the connection details below and save to retry.' (no version text); after Next: inline 'Could not connect to http://127.0.0.1:18830' / 'Agent Canvas requires agent-server 1.63.1 or newer; this backend is running 1.62.0. Please upgrade the agent-server backend.' plus the same as alert toast | pass |  | `evidence/F01.onboarding-backend/old-server-desktop.png` `evidence/F01.onboarding-backend/old-server-next.png` |
| F25.version-gate | launch --new --sdk-version 1.62.0; onboard --skip; goto /conversations (desktop + phone 390x844) | Backend below compatibility.minimumAgentServer (1.63.1) is refused with 'Agent Canvas requires agent-server 1.63.1 or newer; this backend is running 1.62.0.' → agent-server-onboarding-screen + Manage backends in recovery mode (no Done/X); row Local v1.62.0 Disconnected, status detail 'Agent Canvas requires agent-server 1.63.1 or newer; this backend is running 1.62.0. Please upgrade the agent-server backend.'; phone: modal inside viewport, no horizontal overflow; 0 app errors | pass |  | `evidence/F01.onboarding-backend/old-server-returning.png` `evidence/F25.version-gate/phone.png` |
| F26.doctor-minimum | control-openhands doctor on the 1.62.0 run | doctor reports the minimum → warning: 'agent-server meets the UI minimum: server=1.62.0 is below 1.63.1: every page shows the backend-compatibility gate instead of the app'; agent-server 1.62.0 started fine (no litellm import failure) | pass |  |  |
