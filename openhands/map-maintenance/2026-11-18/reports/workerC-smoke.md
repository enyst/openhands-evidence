# Verification ledger — run 2026-11-18T0906-5969ae

Revision `6fa7686d37781d8172798231b07b968b9216214a`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18800.

Checks: 31 — pass 30, fail 0, blocked 1, not-run 0, xfail 0, xpass 0. Families: 28.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 1 | 0 | 0 | 0 | 0 | 0 |
| F02 | 3 | 0 | 0 | 0 | 0 | 0 |
| F03 | 1 | 0 | 0 | 0 | 0 | 0 |
| F04 | 1 | 0 | 0 | 0 | 0 | 0 |
| F05 | 1 | 0 | 0 | 0 | 0 | 0 |
| F06 | 1 | 0 | 0 | 0 | 0 | 0 |
| F07 | 1 | 0 | 0 | 0 | 0 | 0 |
| F08 | 1 | 0 | 0 | 0 | 0 | 0 |
| F09 | 1 | 0 | 0 | 0 | 0 | 0 |
| F10 | 1 | 0 | 0 | 0 | 0 | 0 |
| F11 | 1 | 0 | 0 | 0 | 0 | 0 |
| F12 | 1 | 0 | 0 | 0 | 0 | 0 |
| F13 | 1 | 0 | 0 | 0 | 0 | 0 |
| F14 | 1 | 0 | 0 | 0 | 0 | 0 |
| F15 | 1 | 0 | 0 | 0 | 0 | 0 |
| F16 | 1 | 0 | 0 | 0 | 0 | 0 |
| F17 | 1 | 0 | 0 | 0 | 0 | 0 |
| F18 | 1 | 0 | 0 | 0 | 0 | 0 |
| F19 | 1 | 0 | 0 | 0 | 0 | 0 |
| F20 | 1 | 0 | 0 | 0 | 0 | 0 |
| F22 | 2 | 0 | 0 | 0 | 0 | 0 |
| F23 | 1 | 0 | 0 | 0 | 0 | 0 |
| F24 | 1 | 0 | 0 | 0 | 0 | 0 |
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |
| F26 | 1 | 0 | 0 | 0 | 0 | 0 |
| F27 | 1 | 0 | 0 | 0 | 0 | 0 |
| F28 | 1 | 0 | 0 | 0 | 0 | 0 |
| F29 | 0 | 0 | 1 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F29.session-start | Home composer with an ACP (Codex) profile active | ACP conversation starts and narrates → not driven: CODEX_AUTH_JSON (approved Codex login) is not set in this environment | blocked | tier-3 smoke; prerequisite missing |  |
| F01.route-error-boundary | /this-route-does-not-exist, desktop | Page not found + Home link, sidebar stays, no app errors; Home returns to home-screen → heading/paragraph/link Home as mapped, aside count 1, pageErrors 0 appErrors 0, Home -> home-screen 1 | pass | tier-3 smoke after dep bumps | `evidence/F01.route-error-boundary/not-found.png` |
| F02.command-menu-open-close | /conversations, desktop, Control+k | trigger reads Search commands CTRL+K; menu visible, focus command-menu-search; Escape closes → as expected; screenshot shows blurred backdrop and Navigation/Settings groups; errors 0/0 | pass | tier-3 smoke | `evidence/F02.command-menu-open-close/open.png` |
| F02.command-menu-phone | /conversations/<id> phone 390: chat header hamburger -> drawer Search row | menu fits screen; Escape closes menu and leaves drawer open → insideViewport true, no horizontal overflow; Escape: command-menu 0, drawer 1; errors 0/0/0 | pass | tier-3 smoke; framer-motion modal over drawer | `evidence/F02.command-menu-phone/open.png` |
| F02.mobile-drawer | /conversations, phone 390x844 | drawer opens 300px inside viewport no overflow; closes via X, Escape, Automations link (-> /automations), backdrop → width 300, insideViewport true, pageHorizontalOverflow false; all four close paths detached drawer; Automations link landed /automations; errors app-only 0/0 | pass | tier-3 smoke; framer-motion 14.11.1 drawer animation | `evidence/F02.mobile-drawer/open.png` |
| F03.llm-not-configured-banner | / desktop + phone, before llm preset | banner text + Set up LLM; inside viewport at phone; action -> /settings/llm → exact text; phone insideViewport true no overflow; action landed /settings/llm; errors 0/0 | pass | tier-3 smoke | `evidence/F03.llm-not-configured-banner/banner.png` |
| F04.view-menu | /conversations sidebar, desktop, no conversations | empty state 'No conversations found'; View menu radios By workspace/Recent[checked]/Active/Compact, Filter by tags, More options, Delete all [disabled]; tag filters 'No tags yet'; Escape closes → as expected; errors 0/0/0; after one conversation the sidebar shows one conversation-card | pass | tier-3 smoke | `evidence/F04.view-menu/menu-empty.png` |
| F05.send-message | /conversations/bef25a19-4b28-4237-a18f-e59d3d8ca7c2 composer, desktop | Send message label, disabled empty, enabled after typing, Shift+Enter newline, Enter sends and clears, agent replies → as expected; innerText 'Reply with only:\nok2', cleared after Enter; reply 'ok2'; 2 user messages; errors 0/0/0 | pass | tier-3 smoke; second turn in the same conversation | `evidence/F05.send-message/sent.png` |
| F06.user-and-agent-messages | /conversations/bef25a19-4b28-4237-a18f-e59d3d8ca7c2, desktop (conversation start deepseek-flash, 'Reply with only the word OK. Do not run any tools.') | status finished; user-message and agent-message render, reply OK → finished on deepseek/deepseek-flash; user-message + agent-message 'OK'; errors 0/0/0 | pass | tier-3 smoke; model-backed (one conversation) | `evidence/F07.open-by-url/conversation.png` |
| F07.open-by-url | /conversations/bef25a19-4b28-4237-a18f-e59d3d8ca7c2 by URL, desktop | chat-pane-header, generated title, 1 agent-message, last-conversation localStorage {default-local:<id>} → title 'Simple OK Response Request', 1 agent-message, localStorage as expected; errors 0/0/0 | pass | tier-3 smoke | `evidence/F07.open-by-url/conversation.png` |
| F08.panel-toggle | /conversations/bef25a19-4b28-4237-a18f-e59d3d8ca7c2 right-panel-toggle, desktop | aria-pressed false + tooltip Show panel; click -> Hide panel, Files tab visible with workspace path and tree → as expected; Files shows workspace path and 'No files in workspace' (no repo); Commits tab shows 'No commits yet' (commit-list needs the fixture repo, not arranged in smoke); errors 0/0/0 | pass | tier-3 smoke | `evidence/F08.panel-toggle/drawer-open-files.png` |
| F09.entry-gear | / gear (backend-selector-settings-link), desktop | lands /settings/agents, Agent nav aria-current=page, gear data-active=true; back -> /; /settings redirects to /settings/agents → all as expected; settings nav and Agent page render; errors 0/0/0 | pass | tier-3 smoke | `evidence/F09.entry-gear/agents.png` |
| F10.model-picker | /settings/llm Add LLM profile, Basic, desktop | add form opens; downshift provider combobox chooses OpenRouter; model combobox lists and filters options; Escape closes → add-llm-profile 1, profile-row 0 (fresh); choose OpenRouter value OpenRouter; model list 29 options, filter 'claude' -> 6; Escape aria-expanded false; errors 0/0/0 | pass | tier-3 smoke; downshift 9.5.0 consumer; Back without saving | `evidence/F10.model-picker/model-options.png` |
| F11.provider-picker | /settings/llm Add connection modal, desktop | empty state text; modal focuses name; Save disabled; provider combobox shows label OpenAI; 'deep' filters to deepseek/deepgram/DeepInfra; pick deepseek → all as expected (3 options, verified deepseek + other deepgram, DeepInfra); Escape closed modal without saving; errors 0/0/0 | pass | tier-3 smoke; downshift 9.5.0 consumer | `evidence/F11.provider-picker/deep-filter.png` |
| F12.page | gear -> sidebar Model Router, desktop | /settings/meta-llm, subtitle 'Meta-profiles that route each task to the right LLM profile.', aria-current page → as expected; empty meta-profile list + Add Model Router render; errors 0/0/0 | pass | tier-3 smoke | `evidence/F12.page/page.png` |
| F13.list | gear -> /settings/agents, desktop | row default/default/Active; menu Edit, Set as active [disabled], Delete [disabled] with locked title; one active badge → as expected; errors 0/0/0 | pass | tier-3 smoke | `evidence/F13.list/list.png` |
| F14.list | gear -> sidebar Secrets, desktop | OPENHANDS_AUTOMATION_API_KEY row count 1, URL /settings/secrets → count 1, /settings/secrets, table renders; errors 0/0/0 | pass | tier-3 smoke | `evidence/F14.list/list.png` |
| F15.condenser-page | /settings/condenser direct URL on local backend, desktop | redirects to /settings/agents (Agent header), condenser screen 0, back -> /, no sidebar condenser link → as expected; errors 0/0/0 | pass | tier-3 smoke | `evidence/F15.condenser-page/local-redirect-agents.png` |
| F16.language | /settings/app, desktop: Language -> Français, Save, reload; then back to English | 16 options; Save reads 'Enregistrer les modifications' without reload; persists after reload (value Français, api language fr, html fr ltr, trigger aria-label 'Rechercher des commandes'); restore English -> Save Changes, en ltr → all as expected; sidebar/settings nav/form translated in screenshot; restored to English (api language en); errors 0/0/0 | pass | tier-3 smoke; i18next 27.1.0 consumer. Sidebar 'Automate' label stays English in French: it comes from the automation interface manifest (getInterfaceCopy().sidebarLabel), not i18n, so not an i18next regression | `evidence/F16.language/french.png` |
| F17.page-states | /mcp, desktop, fresh run | installed-empty text; 56 marketplace cards; h2s MCP/Installed/Library; no page errors → as expected (56 cards); errors 0/0/0 | pass | tier-3 smoke | `evidence/F17.page-states/empty-desktop.png` |
| F18.page | sidebar Customize -> Skills, desktop | /mcp then /skills; default-list notice; no Cloud notice; result summary → as expected; '74 result(s)'; errors 0/0/0 | pass | tier-3 smoke | `evidence/F18.page/page.png` |
| F19.page | /conversations -> Customize -> Plugins, desktop | h2 Plugins, Add plugin enabled, 9 plugin cards in two columns with Install → as expected (9 cards); errors 0/0/0 | pass | tier-3 smoke | `evidence/F19.page/catalog.png` |
| F20.page | / -> Customize -> Apps, desktop | Apps for Agent Canvas heading, Build an app (_blank), Add app enabled, trust notice, 'No apps are installed on this backend.' → snapshot matches exactly; errors 0/0/0 | pass | tier-3 smoke | `evidence/F20.page/empty.png` |
| F22.setup-action-kind | /automations/new/custom-automation setup dialog, desktop | browser choose Action Plugin -> setup-field-plugins; Upload tarball -> automation-agent-profile 1 with listbox Default [selected]/default; Escape closes listbox keeps dialog and values; second Escape closes dialog → as expected; name QA_F22 Custom kept; nothing created (api lists no QA_F22); errors 0/0/0 | pass | tier-3 smoke; combobox consumer. Open listbox popover has no border and the same dark bg as the dialog (rgb(32,32,32)), so options read as if overlaid on the form; opaque and functional, cosmetic only, not verified as new | `evidence/F22.setup-action-kind/tarball-profile.png` |
| F22.templates-page | sidebar Automate -> Templates tab, desktop | /automations/templates, h1 Templates, 27 cards, 20 in More templates → as expected; errors 0/0/0 | pass | tier-3 smoke | `evidence/F22.templates-page/templates.png` |
| F23.header | /automations card QA_F23 Pong -> /automations/<id>, desktop | banner Back(/automations), h1, Inactive, Run now [disabled], Edit, switch Turn on, Automation actions; sections How it runs/Trigger/Action/Settings/Runs → banner snapshot matches; h3s How it runs, Trigger, Action, Settings, Runs; Every day at 9:00 AM, UTC, 0 9 * * *, Runs 0, Last run Never; errors 0/0/0 | pass | tier-3 smoke; fixture created via api and deleted after | `evidence/F23.header/inactive.png` |
| F24.open | /automations -> Git Sync, desktop | skeleton observed then page h1 Git Sync; Back to Automations; direct URL; unconfigured card text; Sync now disabled → as expected; Sync Status card text matches map exactly; errors 0/0/0 | pass | tier-3 smoke | `evidence/F24.open/page-desktop.png` |
| F25.selector-dropdown | /conversations backend selector, desktop | listbox option Connected Local, separator, Add Backend, Manage Backends; Add Backend opens 'Choose how you want to connect' with Cloud tab selected; Escape does not close, X does → as expected; errors 0/0/0 | pass | tier-3 smoke; also captured /tmp/claude-0/ohv/2026-11-18T0906-5969ae/evidence/F25.add-backend-modal/modal.png | `evidence/F25.selector-dropdown/open.png` |
| F26.cli-info | terminal: node bin/agent-canvas.mjs --version/-v/--info | version equals package.json; info lists stack pins from config/defaults.json, default ports, override vars → 1.41.0 = package.json, exit 0; agent-server 1.62.0, automation 1.32.1, >= 1.59.0 match defaults.json; ports 8000/18000/18001; override vars listed. Launch with vite 8.3.7 built the frontend and doctor was ok (served build matches checkout) | pass | tier-3 smoke; text artifact (terminal family) | `evidence/F26.cli-info/info.txt` |
| F27.usage-metrics | /conversations/bef25a19-4b28-4237-a18f-e59d3d8ca7c2 drawer Terminal/Browser/Usage tabs, desktop | Terminal 'No terminal output yet'; Browser 'No URL loaded', no open-external; Usage shows Context Window, token usage, Total Cost; no balance card on DeepSeek → as expected (1% used, 14,719 / 1,000,000, Total Cost $0.0030); app errors only the expected 2x GET /api/llm/balance 404; pageErrors 0 | pass | tier-3 smoke | `evidence/F27.usage-metrics/usage.png` |
| F28.open-blank | /automations Add Automation -> Create Automation, desktop | /automations/setup blank form: name New Automation, empty prompt, Daily checked, 09:00, Unsaved changes, Test disabled, model 1, no template agent-profile, pill None, back href /automations → all ten values as expected; nothing saved; errors 0/0/0 | pass | tier-3 smoke | `evidence/F28.open-blank/blank.png` |
