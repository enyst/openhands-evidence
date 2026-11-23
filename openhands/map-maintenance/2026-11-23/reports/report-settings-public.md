# Verification ledger — run 2026-11-23T0908-af809a

Revision `c5e47c4b4dab1d14724e74675c06254957ccbf47`, public mode, Agent Server 1.63.1, base http://127.0.0.1:18850.

Checks: 7 — pass 7, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 7 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F01.api-key-entry | public run: last backend removed; skip; wrong key; connect; stale key; phone | screen shows, no error toast, Host disabled origin, Connect needs name+key, wrong key line, connect reveals app, rotate key re-prompts, no duplicate → remove Local -> screen; toasts [] twice (incl. reload first paint), 'No backend is configured' 0; host http://127.0.0.1:18850; submit false/false/true; 'Invalid API key. Please check the key and try again.'; phone insideViewport true, no overflow; connect -> root-layout, selector 'QA Public'; rotate -> screen, reconnect, backends length 1 | pass | Run A and run B steps driven on one public stack (browser reset between); consent was already answered so 'consent names QA Public' not observable | `evidence/F01.api-key-entry/after-remove.png` `evidence/F01.api-key-entry/wrong-key.png` `evidence/F01.api-key-entry/phone.png` |
| F01.onboarding-acp-secrets | public run, Claude Code / OpenCode / Pi tiles | Add your API keys with provider fields; no write; Pi blocked line colours → Claude Code: CLAUDE_CODE_OAUTH_TOKEN, ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL (host signed-in banner shown); agent_kind openhands; OpenCode: OPENCODE_AUTH_CONTENT/OPENCODE_API_KEY Optional, Next enabled; Pi: 'This backend has no host login...', PI_AUTH_JSON/ANTHROPIC_API_KEY, Next disabled, blocked text exact, rgb(201,185,116) Neutral, rgb(125,93,8) Light+; OpenHands Next -> Settings saved | pass |  |  |
| F01.onboarding-backend-step | public run, fresh browser | no toast; Add a backend, Local + origin, Next disabled; wrong key inline error; right key -> Choose your agent 3 steps no Back; consent names Local → toast history []; snapshot matches (http://127.0.0.1:18850, Next [disabled], OpenHands Cloud column); 'Could not connect to http://127.0.0.1:18850 / Invalid API key', step 0; right key -> consent 'Local', step 0, progress-step-3 0, agent-back 0 | pass |  | `evidence/F01.onboarding-backend-step/fresh.png` |
| F01.onboarding-cloud-login | public run, backend step Advanced | aria-expanded true, Cloud Host placeholder, self-hosted text; login itself blocked → aria-expanded true; placeholder https://app.all-hands.dev; 'Works with OpenHands Cloud or your self-hosted OpenHands Cloud deployment.' | pass | Device-flow login not clicked: needs OpenHands Cloud account | `evidence/F01.onboarding-cloud-login/advanced.png` |
| F01.onboarding-hello-close | public run, last step Close | Close dismisses without conversation, flag set, URL / → conversation count 0 before/after; modal detached; root-layout 1; URL /; onboarded '1'; reload modal 0 | pass | LLM step filled with litellm_proxy/deepseek-v4-flash via eval proxy |  |
| F01.onboarding-recommended-automation | public run, last step Suggested news-digest card | navigates /automations/new/news-digest, modal closed, setup-dialog open; close creates nothing → URL matched; modal 0; onboarded '1'; setup-dialog 1; close -> URL /; automations total 0 | pass |  | `evidence/F01.onboarding-recommended-automation/setup-dialog.png` |
| F01.onboarding-skip | public run: skip after backend step; skip before key | after backend: lands in app; before key: API-key screen → root-layout, after reload modal 0 api-key screen 0; fresh browser skip -> api-key-entry-screen | pass |  |  |
