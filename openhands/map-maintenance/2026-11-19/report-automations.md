# Verification ledger — run 2026-11-19T0902-bc66ce

Revision `e1b8b60f25084a64412c3a2789a921034fc895c7`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18800.

Checks: 18 — pass 15, fail 0, blocked 3, not-run 0, xfail 0, xpass 0. Families: 7.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F02 | 0 | 0 | 1 | 0 | 0 | 0 |
| F09 | 3 | 0 | 0 | 0 | 0 | 0 |
| F21 | 1 | 0 | 0 | 0 | 0 | 0 |
| F22 | 1 | 0 | 1 | 0 | 0 | 0 |
| F23 | 1 | 0 | 0 | 0 | 0 | 0 |
| F26 | 2 | 0 | 0 | 0 | 0 | 0 |
| F28 | 7 | 0 | 1 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F02.update-tile | sidebar New version tile | tile when npm latest newer → tile count 0; client 1.42.0 is up to date | blocked | prerequisite: an installed version older than npm latest |  |
| F22.agent-assisted-setup | Agent fills a prompt form (desktop) | agent fills the form → not driven | blocked | prerequisite: a working LLM key (DEEPSEEK_API_KEY empty in this session) |  |
| F28.form-return | agent fills form via automation_form_update, then switch and return | agent-filled values and ✦ marks kept → not driven | blocked | prerequisite: a working LLM key (DEEPSEEK_API_KEY empty in this session) |  |
| F09.update-card | /settings/app version card (desktop) | Agent Canvas / Version 1.42.0 + badge → 'Agent Canvas / Up to date / Version / 1.42.0', badge count 1 | pass |  | `evidence/F09.update-modal/version-1-42.png` |
| F09.update-modal | version card > dialog | dialog shows 1.42.0 and check status → 'Version 1.42.0', status 'You're running the latest version. What's new' | pass |  | `evidence/F09.update-modal/version-1-42.png` |
| F09.update-up-to-date | version dialog | Up to date when client = npm latest → badge Up to date; status latest version | pass |  | `evidence/F09.update-modal/version-1-42.png` |
| F21.sidebar-entry | Home > sidebar Automate (desktop) | /automations, heading Dashboard, Automate aside, 0 app errors → Dashboard h1, navbar aside, Drafts 1 + Active 1, pageErrors 0 appErrors 0 | pass |  | `evidence/F21.sidebar-entry/smoke-dashboard.png` |
| F22.agent-assisted-setup | Add Automation > Create Automation > fill > Save draft > reload (desktop) | Draft saved / Ready to test, draftId URL, values survive reload → as expected, draft 5a974eec... | pass |  | `evidence/F22.agent-assisted-setup/saved-draft.png` |
| F23.open-detail | Dashboard card heading click (desktop) | /automations/<id> detail, 0 app errors → header 'QA_F28 AgentProfile / Active / Run now / Edit', trigger/action/settings/activity sections, pageErrors 0 appErrors 0 | pass |  | `evidence/F23.open-detail/smoke-detail-from-card.png` |
| F26.cli-info | node bin/agent-canvas.mjs --info | pins match config/defaults.json; pin meets minimum → @openhands/agent-canvas 1.42.0; agent-server 1.62.0, automation 1.32.1, >= 1.59.0; match; pin-meets-minimum | pass |  | `evidence/F09.update-modal/version-1-42.png` |
| F26.cli-version | node bin/agent-canvas.mjs --version | package version → 1.42.0 (package.json 1.42.0, defaults.json versions.agentCanvas 1.42.0, Chart appVersion 1.42.0) | pass |  | `evidence/F09.update-modal/version-1-42.png` |
| F28.custom-agent-profile | /automations/setup > Custom kind > Agent profile pill > default > Save draft > Create; desktop | options None/default; pill default; model locked with tooltip; POST drafts 201 with agent_profile_id; Saved just now; reload keeps default; Create 201, toast, agent_profile_id set, model null → all as expected; drafts POST 201 (not 422, #19474 not reproduced); Create POST /v1 201; GET has agent_profile_id eb042e41..., model null, enabled true. Model pill read 'default' not 'deepseek-flash' (seed agent profile llm_profile_ref is 'default' after onboard --skip + preset; preset did not repoint) | pass |  | `evidence/F28.custom-agent-profile/save-draft.png` |
| F28.form-return | setup conversation (/automations/setup docked composer, dummy-key) > edit Name/Prompt/Custom cron > sidebar other conversation > sidebar back; desktop | form keeps the user's unsaved edits on return → Name 'QA_W2 Return Name', Prompt kept, Custom '0 0 1 1 *' aria-checked true, save state 'Unsaved changes'; other conversation showed no setup form | pass |  | `evidence/F28.form-return/3-returned-desktop.png` |
| F28.form-return | Automate > Add Automation > Create Automation (in-app, after editing a setup conversation and after editing /automations/setup itself) | New Automation page starts clean → Name 'New Automation', empty Prompt, Daily 09:00, 'Unsaved changes' | pass |  | `evidence/F28.form-return/4-new-automation-clean.png` |
| F28.form-return | setup conversation: Save draft, edit Name, sidebar other conversation and back; desktop | newer unsaved edit kept over the saved draft; save state stays Unsaved changes, Test disabled → Name 'QA_W2 Saved Name edited' (draft has 'QA_W2 Saved Name'), 'Unsaved changes', Test disabled; after a second save and switch: 'Saved just now', Test enabled | pass |  | `evidence/F28.form-return/6-saved-draft-edit-returned.png` |
| F28.form-return | phone 390px: setup conversation, edit Prompt + Weekly, menu > other conversation > menu > back | Form view keeps edits, no horizontal overflow → Form view pressed, Name 'QA_W2 Phone', prompt kept, Weekly checked, pageHorizontalOverflow false | pass |  | `evidence/F28.form-return/10-phone-returned.png` |
| F28.form-return | browser goto /conversations/<setup-id> (full page load) with unsaved edits | (boundary) unsaved form is in-page memory only → form reset to New Automation, empty prompt, Daily | pass | full load discards unsaved in-memory form; only in-app navigation keeps it | `evidence/F28.form-return/5-after-full-load.png` |
| F28.open-blank | Automate > Add Automation > Create Automation (desktop) | New Automation, empty prompt, Daily 09:00, Unsaved changes → as expected | pass |  | `evidence/F28.form-return/4-new-automation-clean.png` |
