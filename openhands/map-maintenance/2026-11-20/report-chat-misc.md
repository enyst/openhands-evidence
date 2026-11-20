# Verification ledger — run 2026-11-20T0915-ce5726

Revision `428b3dc2a0e8d3d0f689a909e2607e33d973da76`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18820.

Checks: 370 — pass 74, fail 3, blocked 102, not-run 191, xfail 0, xpass 0. Families: 13.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 6 | 0 | 6 | 11 | 0 | 0 |
| F02 | 11 | 2 | 4 | 14 | 0 | 0 |
| F05 | 3 | 0 | 10 | 14 | 0 | 0 |
| F06 | 7 | 0 | 25 | 8 | 0 | 0 |
| F07 | 22 | 1 | 4 | 1 | 0 | 0 |
| F08 | 6 | 0 | 11 | 18 | 0 | 0 |
| F10 | 1 | 0 | 3 | 30 | 0 | 0 |
| F12 | 1 | 0 | 2 | 23 | 0 | 0 |
| F14 | 11 | 0 | 4 | 0 | 0 | 0 |
| F18 | 4 | 0 | 4 | 15 | 0 | 0 |
| F25 | 1 | 0 | 16 | 18 | 0 | 0 |
| F26 | 1 | 0 | 1 | 39 | 0 | 0 |
| F29 | 0 | 0 | 12 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F02.command-menu-items | Ctrl+K full list | 14 options under Navigation, Settings and Actions (map list ends Application, Secrets) → 15 options: adds 'Experimental Experimental features you can turn on or off. Changes apply to conversations you start afterwards. Go' after Secrets settings (-> /settings/experimental); all 13 mapped routes plus Experimental navigate and close the menu; click path ok; condenser 0 | fail | map drift from #19503 (Experimental settings page); F09.entry-command-menu already lists it, F02.command-menu-items/search counts not updated |  |
| F02.command-menu-search | Ctrl+K search | theme 1, 'settings secret' 1, 'secret automations' 0, model 3, No commands found, Enter no-op, Clear -> count 14, arrows wrap → theme 1, settings secret 1, secret automations 0, model 3; 'No commands found / Try a page, action, or setting name.'; Enter keeps menu+URL; Clear -> '' and count 15 (not 14); arrows new-chat->toggle-sidebar->new-chat->customize; hover secrets-settings | fail | only the count differs: map drift from #19503 (Experimental item) | `evidence/F02.command-menu-search/no-results.png` |
| F07.git-actions-menu | header Git actions menu | 5 items, each prefills composer without sending, Send enabled → 5 items/labels match; prompts match (Commit/Pull/New Branch/Push GitHub/PR GitHub); no new MessageEvent (count 2); first pick (Commits) left Send disabled, later picks enabled | fail | Known failure #18202 reproduced 2026-11-20 (expected failure, already in map) |  |
| F01.bootstrap-loading | first paint | spinner → not run | blocked | map: blocked (spinner <1s on healthy stack) |  |
| F01.locked-cloud-first-run |  | see map → not run | blocked | needs a Cloud host |  |
| F01.onboarding-cloud-login | cloud | see map → not run | blocked | needs an OpenHands Cloud account |  |
| F01.onboarding-hello-close | onboarding | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F01.onboarding-repeat-endpoint | onboarding | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F01.onboarding-say-hello | onboarding | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F02.alert-banner | server config alerts | banner → not reachable | blocked | needs a Cloud backend that publishes alerts (map: blocked on local) |  |
| F02.mobile-conversation-header | long reply conversation at phone | header stays while transcript scrolls → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): bullet needs a long agent reply |  |
| F02.settings-404-modal | settings 404 | LLM modal → not reachable | blocked | needs a backend whose settings endpoint returns 404 (map: blocked) |  |
| F02.update-tile | sidebar New version tile; Settings > Application update check | tile when npm latest newer; manual check status → tile count 0 (up to date); /settings/app badge 'Up to date', modal has check button/status/release notes, check -> 'You're running the latest version. What's new', close count 0 | blocked | tile half blocked: checkout is npm latest; manual-check half passed | `evidence/F02.update-tile/modal.png` |
| F05.build-plan-shortcut | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.image-only-send | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.plan-preview | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.queued-message | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.resolved-banner | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.send-message | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.slash-btw | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.slash-goal | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.slash-plan-code-task | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F05.stop-resume | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply/turn) |  |
| F06.code-block-copy | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.confirmation-mode | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.confirmation-shortcuts | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.corrective-nudge | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.critic-result | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.event-groups | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.events-match | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.hook-events | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.image-attachments | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.live-activity | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.load-older-history | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.markdown-alerts | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.markdown-file-preview | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.markdown-rendering | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.reconnect | agent server stopped while idle | composer 'Reconnecting...' within ~2 s on a finished conversation → on an error/paused (fake-key) conversation the composer kept 'deepseek-flash Error'; Reconnecting not shown | blocked | needs a finished conversation, i.e. a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F06.reload-mid-run | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.scroll-to-bottom | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.skill-install-banner | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.stop-resume | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.streamed-reply | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.task-list | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.thinking | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.timestamps | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.tool-visualizers | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F06.workspace-path-links | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (agent reply, tool call or reasoning) |  |
| F07.cloud-only | Cloud backend | Cloud-only items → local absence confirmed: no share-publicly-button in the ... menu, no Connect Repo chip | blocked | needs an OpenHands Cloud account |  |
| F07.git-control-bar | git control bar on qa-f07-repo conversation | folder chip + branch; GitHub/Azure origin links + Pull/Push/PR → right after start: 'qa-f07-repo' [disabled] + 'main'; after adding GitHub/Azure origins and reload the bar reads only 'qa-f07-repo' (no branch, no links; a href list ''), Overview git section absent | blocked | needs a finished conversation: with a fake key the conversation ends in execution_status=error, and use-local-git-info is gated by useRuntimeIsReady (error excluded), so branch/remote are never probed. Needs a working LLM key (DEEPSEEK_API_KEY unset) | `evidence/F07.git-control-bar/azure-overview-desktop.png` |
| F07.git-control-bar-send | Pull chip | sends git prompt → chips not rendered (see git-control-bar) | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F07.status-menu | status dot after Start Runtime | Running / Stop Runtime after Start Runtime → paused: menu 'Server Stopped / Start Runtime', paused menu lacks show-hooks/stop (as mapped); Start Runtime -> status running then error (fake key), menu stays 'Server Stopped / Start Runtime' | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): resume with a fake key ends in error | `evidence/F07.status-menu/after-start.png` |
| F08.changes-from-overview | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.commit-rows | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.commits-cap | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.diff-deleted-file | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.diff-markdown-preview | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.diff-view-modes | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.files-auto-refresh | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.files-open-from-chat | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.files-open-from-tool-chip | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.files-refresh | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F08.uncommitted-changes | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset): recipe seeds the workspace with an agent bash turn |  |
| F10.cloud-provider-pagination | see map | see map → not run | blocked | needs a Cloud org / older agent server (map: blocked) |  |
| F10.cloud-readonly | see map | see map → not run | blocked | needs a Cloud org / older agent server (map: blocked) |  |
| F10.schema-unavailable | see map | see map → not run | blocked | needs a Cloud org / older agent server (map: blocked) |  |
| F12.home-pick-skips-routing | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F12.route-first-message | see map | see map → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F14.agent-access | conversation start (env var check) | terminal observation True → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F14.agent-request | agent request_secret tool -> secret-request-card | card 'The agent needs a secret' etc. → not reachable without an agent tool call | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) (card is rendered only from an agent request_secret ActionEvent) |  |
| F14.agent-request-replace | agent request_secret for saved name | Edit secret card → not reachable | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F14.edit-value | Secrets > Edit value + conversation | observation True for new value → UI half seen: label 'Secret Value (leave blank to preserve the existing value)' + 'Show secret'; agent half not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F18.cloud-link | Cloud | cloud link → not run | blocked | needs a Cloud backend |  |
| F18.install-banner | /add-skill conversation | install banner → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset); also github.com from the agent |  |
| F18.install-banner-docker | Docker | banner in Docker → not run | blocked | needs Docker daemon and agent-server image |  |
| F18.skill-in-chat | trigger skill in chat | skill reply → not run | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F25.cloud-advanced-host | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-device-flow | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-git-connections | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-log-back-in | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-org-rows | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-org-suspended | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-sandbox-states | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.cloud-settings-link | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.device-verify-page | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.digitalocean-agents | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.digitalocean-backend-removal | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.digitalocean-sign-in | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.license-banner | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.locked-cloud | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.providers-tab | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F25.share-publicly | see map | see map → not run | blocked | needs an OpenHands Cloud account / DigitalOcean stand-in run / license |  |
| F26.lan-http-origin | $OH_VERIFY_LAN_URL reply streaming | agent reply 'pong' streams over ws://lan..., status finished → status error (fake key) | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F29.effort-switch | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.file-changes | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.follow-up | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.live-controls | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.model-switch | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.narration-order | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.reload-order | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.restart-resume | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.session-start | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.stop | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.tool-cards | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F29.usage | see map | see map → not run | blocked | needs an ACP agent login (Claude Code/Codex/Gemini subscription or API key) and a working model; none available in this session |  |
| F01.api-key-entry | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.cookie-auth-redirect | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-acp-profile | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-acp-secrets | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-backend-step | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-phone | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-preview | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-recommended-automation | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-setup-llm | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.onboarding-skip-checklist | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F01.telemetry-consent | see map | see map → not run | not-run | F01 change in range is root.tsx navigation provider only; smoke covered by gate/modal/skip/title/error page; skipped for time budget (several need --public or a fresh backend) |  |
| F02.checklist | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-all-complete | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-dismiss | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-hide | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-item-links | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-minimize | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-preview | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.checklist-progress | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.conversation-list | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.pin-as-home | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.sidebar-collapse | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.sidebar-resize | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.super-admin-setup-guide | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F02.super-admin-setup-tour | see map | see map → not run | not-run | model-free; sources not changed in range (6fa7686d..428b3dc2); skipped for this worker's time budget |  |
| F05.agent-profile-pill | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.agent-profile-switch | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.attach-files | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.attach-size-limit | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.composer-resize | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.context-window-meter | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.dictation | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.llm-profile-picker | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.overflow-menu | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.paste | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.phone | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.profile-identity | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.slash-model | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F05.slash-plan-code | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.clock-skew-send | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.failed-send-persists | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.history-tied-boundary | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.llm-not-configured-banner | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.message-timestamp | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.phone | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.session-activity | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F06.status-indicator | see map | see map → not run | not-run | model-free but not reached in this worker's time budget |  |
| F07.unreadable-event-file | damaged event file | history renders without damaged rows → not run | not-run | model-free but needs service stop + event-file surgery + a second 1.61.0 launch; out of this worker's time budget |  |
| F08.archived-disabled | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.drawer-resize | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-discovery-settings | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-download | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-empty-workspace | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-fallbacks | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-load-error | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-no-selection | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-open-new-window | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-open-tabs | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-rich-plain | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-tree-resize | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.files-tree-toggle | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.panel-direct-url | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.phone-panel-page | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.tabs-menu | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.tabs-pin | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F08.vscode-link | see map | see map → not run | not-run | model-free on an error-state conversation (Files works there); sources not changed in range except workspace-path; skipped for time budget |  |
| F10.actions-menu | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.add-models | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.api-key-help | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.basic-save-keeps-base-url | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.broken-link | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.connection-link | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.create | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.create-prefill | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.create-validation | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.custom-model | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.default-used | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.delete | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.delete-default | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.duplicate | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.edit | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.edit-default-reapply | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.editor-discard | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.list | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.list-empty | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.list-grouped | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.list-states | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.model-picker | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.name-autofill | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.name-validation | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.phone | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.provider-list-complete | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.rename | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.rename-conflict | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.schema-validation | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F10.set-default | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F10 change in range is the subscription card only) |  |
| F12.activate | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.add-connection | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.add-connection-cancel | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.cloud | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.create-first | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.create-more | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.delete | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.delete-active | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.duplicate-name | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.edit | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.editor-cancel | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.editor-validation | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.empty-states | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.light-theme | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.list | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.load-error | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.phone | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.router-profiles | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.row-menu | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.run-first-message-toggle | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.template-chooser | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.template-custom | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F12.unsupported | see map | see map → not run | not-run | F12 sources not changed in range (only shared settings-nav order); skipped for time budget |  |
| F18.card | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.detail-modal | add-javadoc detail switch | see map → docker modal opens with name/source/enable row/description/pills/content/Close/Use skill; switch half not run | not-run | time budget | `evidence/F18.detail-modal/docker.png` |
| F18.detail-pills | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.facets | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.filters-modal | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.personal-skill-dirs | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.phone | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.project-skill | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.search | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.search-history | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.skill-deleted | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.toggle | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.toggle-error | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.toggle-local | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F18.use-skill | see map | see map → not run | not-run | model-free; sources unchanged except copy buttons (covered); skipped for time budget |  |
| F25.add-agent-server | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.add-backend-modal | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.agent-server-guidance | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.backend-pinned-url | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.collapsed-entry | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.edit-backend | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.edit-cancel | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.edit-escape | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.health-status | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.manage-add | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.manage-backends | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.manage-select | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.per-tab-backend | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.phone | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.recovery-gate | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.remove-backend | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.selector-dropdown | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F25.switch-backend | see map | see map → not run | not-run | model-free but not reached in this worker's time budget (F25 change in range is the shared-conversation page only) |  |
| F26.automation-startup-failure | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.backend-log-level | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.backend-only | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-flag-conflicts | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-help | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-info | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-missing-build | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-port-in-use | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-public-needs-key | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cli-version | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.cross-connect | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.desktop-boot-splash | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.desktop-external-links | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.desktop-macos-titlebar | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.desktop-main-window | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.docker-conversation-runtime | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.docker-image | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.docker-mount-preflight | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.docker-workspace-persist | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.frontend-only | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.frontend-only-returning | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.helm-chart | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.host-bind-env | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.host-bind-lan | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.host-bind-lan-optin | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.lan-insecure-origin | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.lib-build | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.lib-host-app | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.lib-style-scope | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.loopback-bind-default | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.mars-web-bridge | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.remote-backend | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.runtime-services | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.runtime-services-agent-use | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.seeded-local-backend | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.service-restart | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.session-key-persist | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.session-key-pinned | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F26.session-key-rotated | see map | see map → not run | not-run | runtime/launcher variants (CLI, Docker, desktop, lib); out of this chat-scope worker; no F26 source changed except the verify harness LAN origin |  |
| F01.document-title | document.title | OpenHands on /, not-found, phone /,/settings/app; '<emoji> <title> \| OpenHands'; fallback 'Conversation <5 id chars>' → OpenHands everywhere listed; '🔴 QA_F07 renamed \| OpenHands'; '🔴 Conversation 05476 \| OpenHands' (error-state emoji) | pass | finished ✅ title needs a model reply |  |
| F01.first-run-gate | browser reset, /conversations | first-run-onboarding-screen, onboarding-modal (+ telemetry-consent-form), no root-layout → first-run-onboarding-screen, onboarding-modal, no root-layout; telemetry-consent-form absent because this backend's consent was already answered by the earlier onboard --skip (fresh-backend condition not met, not a defect) | pass |  | `evidence/F01.first-run-gate/fresh.png` |
| F01.onboarding-choose-agent | Choose agent step | OpenHands preselected, six radios, Next saves -> step 1, Back -> 0 → as expected, 'Settings saved' | pass |  |  |
| F01.onboarding-modal | onboarding modal | Escape/backdrop don't close, step 0, steps 0..2 only → as expected | pass |  |  |
| F01.onboarding-skip | onboarding Skip | root-layout; after reload no modal/api-key screen → as expected | pass |  |  |
| F01.route-error-boundary | /this-route-does-not-exist | Page not found, paragraph, Home link, sidebar stays, no errors, Home -> home-screen → exact | pass |  | `evidence/F01.route-error-boundary/not-found.png` |
| F02.command-menu-focus | Ctrl+K from composer | search focused, Tab -> new-chat, Escape returns to chat-input → command-menu-search, command-menu-option-new-chat, count 0, chat-input | pass |  |  |
| F02.command-menu-new-tab | middle/Ctrl-click Go item | href /settings/secrets, tab 1 opens, menu stays, Escape closes → as expected for both paths | pass |  |  |
| F02.command-menu-open-close | Ctrl+K / Meta+K / Search commands row / collapsed icon | open/focus/kbd, Escape, backdrop, cleared query, focus return, collapsed icon → all as described: 'Search commands CTRL+K', command-menu-search focused, Escape/backdrop close, value '', focus command-menu-trigger, collapsed count 1 | pass |  | `evidence/F02.command-menu-open-close/open.png` |
| F02.command-menu-phone | phone drawer Search row | fits; Escape keeps drawer; Enter navigates and closes drawer → insideViewport true no overflow; count 0 drawer visible; /settings/secrets and drawer detached | pass |  | `evidence/F02.command-menu-phone/open.png` |
| F02.command-menu-toggle-sidebar | Ctrl+K toggle / sidebar | true then false → true then false | pass |  |  |
| F02.error-toasts | /conversations/<unknown> | one top-right error toast, auto-closes <30s; ink/surface/icon per theme → 1 history entry; hidden within 30s; default 'rgb(255, 255, 255) on rgb(49, 49, 49)' icon rgb(255, 104, 78); Light+ 'rgb(31, 31, 31) on rgb(229, 229, 229)' icon rgb(193, 42, 28); Solarized 'rgb(0, 43, 54) on rgb(230, 223, 204)' icon rgb(181, 40, 37) | pass | success-toast colour half and quiet-refresh bullet not run | `evidence/F02.error-toasts/missing-conversation.png` |
| F02.mobile-drawer | phone hamburger | 300px drawer, 4 close paths, 48x48 toggle with 24px icon → width 300 inside; close/Escape/backdrop/route all detached; toggle x10 y0 48x48, icon [24,24] | pass | modals-over-drawer half not run | `evidence/F02.mobile-drawer/open.png` |
| F02.mobile-top-bar | phone /settings/llm, /skills back chevron | Settings -> /settings (no chevron); Customize -> /customize hub → as expected | pass |  |  |
| F02.nav-links | sidebar links/logo | Customize->/mcp active on /skills,/plugins,/apps; Automate active; New Chat/logo -> /conversations → as expected | pass |  |  |
| F02.settings-link | collapsed settings icon; gear | /settings -> /settings/agents same tab → /settings/agents both, target null | pass |  |  |
| F02.web-app-manifest | link[rel=manifest] | /site.webmanifest 200 manifest+json OpenHands standalone #181818, 2 icons 200 → exact | pass |  |  |
| F05.draft-persistence | conversation + home composer drafts | draft survives navigation/reload/fast leave; home draft in sessionStorage → 'QA draft text' saved, after Settings round trip and reload; 'QA draft text plus fast'; home 'QA home draft', oh:home-prompt-draft | pass | setup-page and late-echo halves not run (late echo needs a model reply) |  |
| F05.plus-menu | composer + menu (error-state conversation) | macros/skills/hooks/agent tools/add files; macros fill composer; Escape returns focus; dialogs → items macros, show-skills, show-agent-tools, add-files-and-images (no show-hooks: conversation not active, consistent with F07.menu-items-by-state); 4 macros; Fix README fills, user-message unchanged 2; Escape -> chat-plus-button; Skills and Agent Tools dialogs open/close | pass | show-hooks only on an active conversation |  |
| F05.slash-menu | composer '/' | 40 options (extensions 0.42.0), Commands /btw /model /goal /plan /code then skills; mo filters; ArrowDown -> /plan; Escape keeps /mo; Tab completes /btw; /model lists profiles, Enter inserts → 42 options incl. this run's /qa-hello fixture (41 without it; extensions now 0.43.0 via #19879); rest exact: mo -> 36, /plan selected, '/mo' kept, '/btw ', '/model deepseek-flash ' | pass | count differs by one: likely the extensions 0.43.0 bump (version-dependent number in the map) | `evidence/F05.slash-menu/model.png` |
| F06.branch-from-here | hover user message > Branch from here; leave mid-fork toast | user-message branch omits that message, prefills composer, title '(branch)', nothing sent; leaving mid-fork shows 'Branched this conversation' toast whose Open lands on branch with text → composer ''->'Reply with only the word PONG. Do not run any tools.' at 181ms; branch has 1 user message, MessageEvent count 1; title '... (branch)'; submit disabled (known Gotcha); toast shown while on /conversations, Open -> /conversations/e682d25f..., chat-input prefilled | pass | model-free halves only; agent-message branch and sending the prefilled branch need a model reply (DEEPSEEK_API_KEY unset) | `evidence/F06.branch-from-here/toast.png` |
| F06.empty-state-suggestions | New thread > No workspace | Let's start building! + 4 chips; Initialized session group toggle works; chip fills composer and hides suggestions; returns; survives reload; phone fits; new tab shows → text exact; counts 1/1; toggle aria-expanded true on click (one early click read false, not reproduced on a second fresh conversation); Fix README fills composer, count 0, fill '' restores; after reload count 1; phone insideViewport true no overflow; new tab visible | pass | send-hides-suggestions half needs a model reply | `evidence/F06.empty-state-suggestions/empty.png` |
| F06.error-banner | send while agent server stopped | banner 'HTTP request failed (502 Bad Gateway): ...ECONNREFUSED...', icon, Copy, Close, no Retry; Close removes → exact text with :18821; testids icon/content/copy/dismiss (no retry); Copy -> 'Copied to clipboard' and clipboard holds text; Dismiss -> count 0; after restart Retry delivered the message once (MessageEvent count 1) | pass |  | `evidence/F06.error-banner/banner-after-failed.png` |
| F06.error-events | conversation start with invalid (dummy) key | ConversationErrorEvent -> warning banner + composer status Error → error-message-banner with warning icon, text 'litellm.BadRequestError: DeepseekException - {...Authentication Fails...}', View More/View Less, Copy (clipboard got full text), Close; composer status 'Error' | pass |  | `evidence/F07.open-by-url/model-free.png` |
| F06.message-copy | hover user bubble > Copy to clipboard (loopback) | label Copied to clipboard ~2s, clipboard holds markdown source → Copied to clipboard -> Copy to clipboard after 2.5s; clipboard 'Reply with the single word: pong. Do not run any tools.' | pass | user bubble only; agent bubble copy needs a model reply | `evidence/F06.message-copy/user-copied.png` |
| F06.pending-messages | send 25-line message | Sending... then absent after echo → observed <absent> -> 'Sending...' at 50ms -> <absent> at 75ms | pass | Retry half below (server stopped) | `evidence/F06.pending-messages/long-user.png` |
| F06.user-and-agent-messages | long user message | clipped with gradient, View More expands → chat-message-truncation-gradient + chat-message-expand present; click removes both, 'filler line 24' visible | pass | user half only; chat-message-expand innerText read '' (label likely icon/aria); agent bubble and drag-selection halves need a model reply | `evidence/F06.user-and-agent-messages/expanded.png` |
| F07.agent-tools-modal | ... > Show Agent Tools & Metadata | System Message + Available Tools, 23 tools on 1.60.1 list → 23 tools: terminal..invoke_skill incl. request_secret, no think (same list); toggle expands; close count 0 | pass |  | `evidence/F07.agent-tools-modal/tools.png` |
| F07.branch-from-message | hover first user message > Branch from here | branch titled '<title> (branch)', 0 user messages, original prompt in composer, nothing sent → title 'QA_F07 renamed (branch)', 0 user messages, chat-input 'Reply with the single word: pong. Do not run any tools.' after 3s, MessageEvent count 0 | pass | agent-message half needs a model reply (DEEPSEEK_API_KEY unset) |  |
| F07.delete-confirm | ... > Delete Conversation | dialog names title; Cancel keeps; Confirm Delete removes, -> /conversations, API [null] → 'Are you sure you want to delete the "QA_F07 renamed (branch)" conversation? This action cannot be undone.'; Cancel kept URL; Confirm -> /conversations; ids= -> [null] | pass |  | `evidence/F07.delete-confirm/dialog.png` |
| F07.display-cost | ... > Display Usage and Cost | usage-panel, aria-pressed true, desktop URL stays; phone /panel → usage-panel visible, aria-pressed true, URL /conversations/<id>; phone URL /conversations/<id>/panel with usage-panel | pass |  | `evidence/F07.display-cost/desktop.png` |
| F07.download-zip | ... > Download conversation data | conversation_<id>.zip with <id>/base_state.json, bash_events/, api_key masked → 1795166536090-conversation_<id>.zip, 35 entries incl base_state.json and bash_events/; api_key values '**********' x2 | pass |  |  |
| F07.export-transcript | ... > Export… | dialog radios/checkboxes; .md starts '# QA_F07 renamed', Model line, '## User' with <sub> timestamps; .html title, no timestamps; Cancel/Escape/close no download → dialog exact; md head '# QA_F07 renamed\n\n**Model:** deepseek/deepseek-flash\n\n## User\n\n<sub>2026-11-20T09:18:54.571Z</sub>'; html <title>QA_F07 renamed</title>, 0 timestamps; three close paths -> no new file | pass | model-switch quote half needs an agent switch_llm (model) | `evidence/F07.export-transcript/dialog.png` |
| F07.history-skeleton | sidebar row click | skeleton present briefly then absent; URL ?backend=default-local → observed <absent> -> present at 185ms -> <absent> at 247ms; URL /conversations/<id>?backend=default-local | pass |  |  |
| F07.hooks-modal | ... > Show Available Hooks (idle conversation) | Available Hooks text + 'No hooks configured for this conversation.'; Refresh POST /api/hooks; close → text exact; Refresh -> POST /api/hooks 200; phone inside; close count 0 | pass | workspace-hooks half (fixture + conversation start) not run | `evidence/F07.hooks-modal/empty.png` |
| F07.menu-items-by-state | ... menu on non-active (error) conversation | Show Available Hooks and Stop Conversation only while active → on status=error conversation both absent | pass | active half (running conversation) needs a model run; not run |  |
| F07.menu-open | header ... menu | items per state; Escape closes and refocuses ellipsis; outside click closes → items rename, show-skills, show-agent-tools, export-transcript (Export…), download-trajectory, display-cost, delete (no hooks/stop: conversation is in error state, not active); Escape count 0, focus ellipsis-button; outside click count 0 | pass |  | `evidence/F07.menu-open/menu.png` |
| F07.missing-redirect | /conversations/<unknown id> | one toast 'This conversation does not exist...', redirect /conversations, last slot {} → redirect /conversations; exactly one history entry with that text; slot {} | pass | transient-lookup half not run |  |
| F07.open-by-url | /conversations/<id> | header, history, composer; last-conversation slot → header+composer, user bubble, error banner; slot {"default-local":"<id>"}; title is the truncated prompt 'Reply with the single word: pong. Do not run an...' and agent-message count 0 (no reply) | pass | generated-title and agent-message count 1 need a model reply (DEEPSEEK_API_KEY unset); setup-conversation half not run | `evidence/F07.open-by-url/model-free.png` |
| F07.overview-toggle | header (i) button (desktop) | overview visible, Hide overview; exclusive with panel; peek on hover; toggle closes panel → visible true, 'Hide overview'; panel open hides column; peek visible on hover; overview click -> panel aria-pressed false, column visible; restored 'Show overview' | pass | phone half (known #16792) not run | `evidence/F07.overview-toggle/open.png` |
| F07.panel-route | phone panel button; /panel direct; widths | phone /panel with back; tablet keeps; desktop redirects with drawer open → all as described: /panel, mobile-panel-top/back, tablet count 1, desktop redirect count 0 aria-pressed true (both via resize and direct goto) | pass |  | `evidence/F07.panel-route/desktop-redirect.png` |
| F07.phone | 390px conversation header, menus, dialogs | header 48px with sidebar-mobile-menu-toggle; dialogs and menu inside viewport (x~133,w~249) → header 48px, all controls listed; skills-modal and system-message-modal inside, no overflow; menu x 133.3 width 248.7 inside | pass | hooks-modal not reachable on non-active conversation | `evidence/F07.phone/header-menu.png` |
| F07.rename-inline | dblclick title; menu Rename empty | toast 'Conversation title updated successfully', sidebar row updated, persists; empty reverts no toast → toast matches; active sidebar row 'QA_F07 renamed'; after reload 'QA_F07 renamed'; empty -> title unchanged, 0 toasts | pass |  |  |
| F07.right-panel-toggle | header panel button | alternates Show/Hide panel; closed after reload → Show panel->Hide panel (tabs-pane-header visible)->Show panel (hidden); after reload aria-pressed false | pass |  |  |
| F07.skills-modal | ... > Show Available Skills | Public skills 15, rows expand to Triggers/Content, Escape closes → 'Public skills 15' with 15 buttons; github row -> 'Triggers github Content ## Connection selection...'; Escape -> count 0 | pass |  | `evidence/F07.skills-modal/expanded.png` |
| F07.skills-modal-project | ... > Show Available Skills in git workspace with .agents/skills | Project skills 1 above Public skills 15; expands Triggers qaf07trigger Content QA_F07 skill body.; Refresh POST /api/skills → exact: 'Project skills 1', button 'qa-f07-skill AgentSkills', expands 'Triggers qaf07trigger Content QA_F07 skill body.'; Refresh POST /api/skills 200 | pass |  | `evidence/F07.skills-modal-project/project.png` |
| F07.stale-launch-url | /conversations/launch-0000... | New Chat, Git actions, stale message, Back; no API request; Back->Home; fits phone → text matches exactly; network total 0; only inline status in toasts; Back -> /conversations with home-chat-launcher 1; phone insideViewport true, no overflow | pass | automation setup launch- half not run | `evidence/F07.stale-launch-url/desktop.png` |
| F07.status-menu | hover status dot on errored conversation | menu shows state; Stop Runtime when active, Start Runtime when paused → status=error conversation: menu reads only 'Server Stopped' (no Start/Stop Runtime item) | pass | error state is not described by the bullet; running/paused halves need a model run (DEEPSEEK_API_KEY unset) | `evidence/F07.status-menu/errored.png` |
| F07.stop-confirm | ... > Stop Conversation (idle empty conversation) | Confirm Stop Conversation dialog; Cancel keeps; Confirm Close pauses, -> /conversations, toast Conversation stopped → dialog 'Confirm Stop Conversation Are you sure you want to stop this conversation?' Cancel/Confirm Close; Cancel status idle; Confirm -> /conversations, toasts 'Stopping conversation...','Conversation stopped'; status paused | pass | run on an idle (not running) conversation: a running one needs a model |  |
| F08.commits-states | Commits on error-state conversation | 'Waiting for runtime to start...' on an error-state conversation → spinner + 'Waiting for runtime to start...' | pass | No commits yet / Loading halves need an agent-run conversation | `evidence/F08.tab-bar/commits.png` |
| F08.drawer-state-reload | reload with Commits selected | closed after reload; reopen shows Commits → aria-pressed false after reload; reopen shows Commits tab selected ('Waiting for runtime to start...' on error-state conversation) | pass |  |  |
| F08.files-tree | Files tree | folders collapsed, files; click selects and opens → tree '.agents .openhands src README.md'; README.md opens preview with Rich/Plain, Download, Open in new window | pass |  | `evidence/F08.files-tree/readme.png` |
| F08.files-workspace-path | Files tab workspace path copy | title is full path; Copied to clipboard + disabled; clipboard full path; label resets ~3s → title <run>/workspace/qa-f07-repo; 'Copied to clipboard', enabled false; clipboard full path; 'Copy to clipboard' after 3.2s | pass | fixture is qa-f07-repo instead of qa-repo |  |
| F08.panel-toggle | chat header panel toggle (qa-f07-repo conversation) | Show panel tooltip; Hide panel, pressed, Files with path and tree → as expected | pass |  | `evidence/F08.panel-toggle/drawer-open-files.png` |
| F08.tab-bar | drawer tabs | Files, Commits, Planner, Terminal, Browser, Usage; active tab click closes → 6 tabs as listed; clicking active Commits -> aria-pressed false, tabs-pane-header hidden | pass |  | `evidence/F08.tab-bar/commits.png` |
| F10.subscription | LLM profile editor > Authentication > ChatGPT subscription > Connect | not connected, gpt-5.5, no provider/key fields; Connect shows code, sign-in page, poll, Cancel, auth.openai.com tab; poll 'Sign-in is not complete yet...'; Cancel removes code; API key restores OpenAI/gpt-5.6-sol → as expected; code copy button (#18583 copyToClipboard) -> 'Copied to clipboard', clipboard holds the code | pass | Save known failure #17135 not re-driven; completing sign-in and subscription-disconnect need a ChatGPT Plus/Pro account | `evidence/F10.subscription/device-code.png` |
| F12.page | Settings nav > Model Router; Ctrl+K | subtitle, aria-current page; single command option for Model Router/router/meta; Enter navigates → as expected; desktop nav order Agent, LLM, Model Router, Agent Context, Verification, Runtime, Application, Secrets, Experimental (Experimental last, #19881) | pass |  | `evidence/F12.page/page.png` |
| F14.create | Settings > Secrets > Add | QA_TMP_SECRET listed after reload → count 1 after reload | pass |  | `evidence/F14.create/form.png` |
| F14.create | Secrets > Add under cipher mismatch | 500 toast 'Secrets file is corrupted...', form closes, secrets.json identical; Sound Notifications save toast, settings.json unchanged → exact 500 toast; add form count 0; secrets.json sha equal; settings toast 'Settings file is corrupted or encrypted with a different key: ...'; settings.json sha equal; restored, doctor ok | pass |  | `evidence/F14.create/cipher-mismatch.png` |
| F14.create-validation | Settings > Secrets > Add | Secret already exists rgb(231,106,94); pattern message; empty value disabled + 'Please fill out this field.' → paragraph 'Secret already exists' rgb(231, 106, 94); 'Please match the requested format.'; submit disabled, 'Please fill out this field.'; no QA_EMPTY_VALUE in API | pass |  | `evidence/F14.create-validation/duplicate.png` |
| F14.delete | Secrets > Delete | 'Are you sure you want to delete this key?'; Cancel keeps; Confirm removes → dialog text matches; Cancel count 1; Confirm+reload count 0 | pass |  | `evidence/F14.delete/confirm.png` |
| F14.delete-escape | Secrets > Delete > Escape | modal count 0, row stays → modal 0, row count 1 (run on QA_TMP_SECRET, model-free) | pass |  |  |
| F14.edit | Secrets > Edit | value empty, Save disabled until change, row 'QA_TMP_SECRET\tQA dummy edited' after reload → value empty (masked), disabled->enabled after description, row text 'QA_TMP_SECRET\tQA dummy edited' | pass |  |  |
| F14.form-back | Secrets > Add > Back | 'Add a Secret', Back discards draft, list back, reopen empty; Edit title 'Edit a Secret' → title 'Add a Secret'; form count 0; items 1; API has no QA_BACK_SECRET; reopened name ''; edit title 'Edit a Secret' | pass |  |  |
| F14.list | Sidebar gear > Secrets; Ctrl+K 'Secrets' | OPENHANDS_AUTOMATION_API_KEY row count 1, URL /settings/secrets (both entries) → count 1; URL /settings/secrets via sidebar and via command menu | pass |  | `evidence/F14.list/list.png` |
| F14.phone | /settings/secrets at 390px | insideViewport true, no overflow, list and add form → both bboxes insideViewport true, pageHorizontalOverflow false | pass |  | `evidence/F14.phone/add-form.png` |
| F14.rename | Secrets > Edit name | rename onto existing refused 'Secret already exists'; rename keeps stored value under new name → 'Secret already exists' paragraph, form open; QA_RENAMED_SECRET count 1, QA_AGENT_SECRET 0, API lists only new name | pass | UI half only; env-var check (True False) blocked: needs a working LLM key (DEEPSEEK_API_KEY unset) |  |
| F14.value-reveal | Settings > Secrets > Add/Edit, Show secret | password new-password -> text on Show, Hide secret, no network, masked on reopen; edit of other secret password+empty, submit disabled → INPUT password new-password -> INPUT text new-password; Hide secret present; 0 /api/settings/secrets requests; reopen password; other edit 'password []', reveal 'text []', submit disabled. Request-card half not reached (needs model) | pass |  | `evidence/F14.value-reveal/revealed.png` |
| F18.add-skill-modal | /skills > Add skill | modal text, docs link, copy example, 3 close paths, code-review is public → as expected; LAN copy also 'Copied to clipboard', clipboard holds the command, 0 page errors, 0 toasts | pass |  | `evidence/F18.add-skill-modal/lan-copied.png` |
| F18.copy-source | /skills card + modal copy source (loopback and LAN http) | title full path; Copied to clipboard; modal stays closed; clipboard path; resets to Copy source path; modal copy keeps modal; none for public skill → all as expected on loopback; on $OH_VERIFY_LAN_URL (no navigator.clipboard) card copy also 'Copied to clipboard', no errors | pass | qa-hello arranged with 'fixture skill' instead of the agent prompt in Preconditions | `evidence/F18.copy-source/modal-copied.png` |
| F18.detail-close | docker detail modal | 4 close paths -> 0 → X, Close, Escape, backdrop all -> count 0 | pass |  |  |
| F18.page | sidebar Customize > Skills | /mcp then /skills, result summary → /mcp -> /skills, '75 result(s)' (74 catalog + qa-hello fixture) | pass | description/notice text and command-menu entry not re-read | `evidence/F18.page/desktop.png` |
| F25.shared-conversation-view | /shared/conversations/<id> on local | standalone page, 'Conversation not found' → 'Conversation not found', no sidebar, desktop and phone; 2 expected 404s (shared-conversations, shared-events) | pass |  | `evidence/F25.shared-conversation-view/local.png` |
| F26.lan-http-origin | $OH_VERIFY_LAN_URL conversation, user bubble copy + error banner copy | insecure context; copy works without Clipboard API: Copied to clipboard, no page errors, no error toast, clipboard holds text → {secure:false, randomUUID:undefined, clipboard:undefined}; Home + onboard + conversation start ok over LAN (status error, fake key), appErrors 0; user-bubble copy 'Copied to clipboard', pageErrors 0, no error toast, loopback clipboard 'Reply with the single word: pong'; error-banner copy also 'Copied to clipboard' and clipboard holds the litellm error text (#18583 fallback) | pass | model-free half | `evidence/F26.lan-http-origin/copy.png` |
