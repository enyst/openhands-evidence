# Verification ledger — run 2026-11-21T1331-1f00d2

Revision `ccf54d45c6fa5fe72fba9c5f507f693dee22af3f`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 11 — pass 7, fail 3, blocked 0, not-run 0, xfail 1, xpass 0. Families: 5.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F22 | 1 | 0 | 0 | 0 | 0 | 0 |
| F23 | 3 | 2 | 0 | 0 | 0 | 0 |
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |
| F26 | 2 | 0 | 0 | 0 | 0 | 0 |
| F28 | 0 | 1 | 0 | 0 | 1 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F23.phone | 390x844 QA_F23 Pong detail, Runs list row (cost+phase) | time one line (~20px), not intersecting run-cost → Known failure #19935 reproduces: time [41,72,751,791] (40px, two lines), run-cost [41,91,773,789] overlaps; summary <p> width 0; screenshot shows PM over $0.0000 | fail | map Known failure #19935 confirmed; map says time x 41-81, observed 41-72 (approximate) | `evidence/F23.phone/runs.png` |
| F23.run-no-conversation | QA_F23 Fail (timeout 1) Run now -> FAILED; detail Runs list | No Conversation label beside the time (prompt automation) → Known failure #17948 reproduces: row '1:33 PM / Timed out: command timed out or was killed / Installing dependencies / Failed', no 'No Conversation' text; run has bash_command_id 82f5be95... and conversation_id null; run-conversation-indicator count 0 (desktop and phone), so nothing on the row says no conversation started | fail |  | `evidence/F23.run-no-conversation/timeout-no-indicator.png` |
| F28.draft-save | /automations/setup Weekly Wed 10:30 Save draft, reload, Drafts row resume; control-openhands bug run F28.draft-save --attempts 2 | reopened draft restores Weekly with weekday 3 and time 10:30 → Known failure #19812 reproduces: POST body schedule 30 10 * * 3, weekly aria-checked true before reload; after reload and after Drafts row resume: custom checked, custom-schedule '30 10 * * 3', 'Every Wednesday at 10:30 AM', weekday count 0, save state 'Saved just now'. bug run: summary xfail 2 / xpass 0 / fail 0 | fail | known-bug block leaves its draft behind each attempt (2 drafts), no cleanup line | `evidence/F28.draft-save/weekly-resumed-custom.png` |
| F28.draft-save | known bug: weekly-resume | true → false | xfail | known bug reproduced at its marked assertion | `evidence/known-bugs/F28.draft-save-weekly-resume-1795268086898-2.json` |
| F22.setup-repository-list | source/version check: run's automation worker .venv (automation-runs/c4e637bd.../.venv) | workers install SDK 1.63.1, PROVIDER_TOKEN_NAMES names GITHUB_TOKEN → openhands_sdk-1.63.1.dist-info; repo.py:49-55 GITHUB: GITHUB_TOKEN, GITLAB_TOKEN, BITBUCKET_TOKEN, azure_devops_token, bitbucket_data_center_token | pass | source check only; clone not re-driven |  |
| F23.activity-log | QA_F23 Pong (dummy key) Run now; detail Runs list | run with conversation_id shows run-conversation-indicator img 'Conversation started' (title) left of logs icon, ~987-1011 vs 1019-1043 desktop → run FAILED with conversation_id b394b8b2 + LLMBadRequestError Authentication Fails; snapshot: $0.0000, img "Conversation started", button View logs..., phase, Failed; title=Conversation started; indicator 986.7-1010.7, logs 1018.7-1042.7; phone count 1, indicator 99-123 left of logs 131-155, pageHorizontalOverflow false | pass |  | `evidence/F23.activity-log/conversation-indicator-desktop.png` `evidence/F23.activity-log/conversation-indicator-phone.png` |
| F23.activity-log | QA_F23 Fail timeout run (conversation_id null), desktop + phone | run without conversation has no run-conversation-indicator → browser count 'testid=automation-activity-log >> testid=run-conversation-indicator' = 0 at desktop and phone; phone pageHorizontalOverflow false | pass |  | `evidence/F23.run-no-conversation/timeout-no-indicator.png` |
| F23.edit-open | Gotcha: plugin configuration editor on local run; QA_F23 Event (preset/plugin) -> Edit | automation 1.34.1 capabilities list pluginConfigUpdate; plugin_spec null; browser count automation-setup-plugin-config 0; ordinary prompt form → capabilities.features includes pluginConfigUpdate; GET automation plugin_spec null; edit page count plugin-config 0, prompt 1 | pass |  | `evidence/F23.edit-open/event-plugin-no-editor.png` |
| F25.manage-backends | default launch; backend-selector > Manage backends | row version v1.63.1 on a default launch → manage-backends-version-Local 'v1.63.1'; /server_info version 1.63.1; doctor agent-server 1.63.1 | pass |  | `evidence/F25.manage-backends/list-version.png` |
| F26.cli-info | node bin/agent-canvas.mjs --info | agent-server pin 1.63.1, automation 1.34.1, >= 1.63.1 → @openhands/agent-canvas 1.43.0; agent-server 1.63.1; automation 1.34.1; Compatibility agent-server >= 1.63.1; ports 8000/18000/18001 | pass |  |  |
| F26.runtime-services | source check ACP gotcha: openhands/sdk/agent/acp_agent.py in SDK 1.63.1 (worker .venv, same version as agent server 1.63.1) | _shutdown_runtime terminate() then kill(), no process-group teardown → _shutdown_runtime (line 4979) calls process.terminate(), on exception process.kill(); no killpg/setsid/start_new_session in file | pass | source only; live ACP check blocked (no provider) |  |
