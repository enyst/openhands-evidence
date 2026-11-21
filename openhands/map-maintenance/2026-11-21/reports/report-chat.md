# Verification ledger — run 2026-11-21T1245-46e2a3

Revision `0f4cb6af95915fee776913c4aa8694e7c4b76033`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18820.

Checks: 54 — pass 19, fail 3, blocked 28, not-run 4, xfail 0, xpass 0. Families: 4.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F05 | 2 | 0 | 1 | 0 | 0 | 0 |
| F06 | 12 | 2 | 27 | 4 | 0 | 0 |
| F09 | 2 | 0 | 0 | 0 | 0 | 0 |
| F30 | 3 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F06.conversation-mention-link | click a mention / goto /conversations/<32-hex id> | conversation opens like from the sidebar (row marked current) → conversation opens and connects, but no sidebar row has aria-current/bg (conversation.id === currentConversationId compares dashed vs dashless id) and the 'Initialized session' row is missing; reproduced via click and via goto | fail | candidate defect, #19921 mention href uses dashless id | `evidence/F06.conversation-mention-link/dashless-route-6s.png` |
| F06.markdown-rendering | user message with an 8,000-row markdown table (paste + Enter), then browser reload | rendering time grows in proportion to the table → 8,000 rows: last row in DOM after 12.5 s / 13.1 s, longest main-thread task 10.1 s / 11.9 s; 2,000 rows: 2.7 s / 1.9 s, longest task 1.3 s / 0.9 s (4x rows -> ~10x longest task); lockfile micromark-extension-gfm-table 2.1.1 | fail | Known failure #19929 reproduced twice | `evidence/F06.markdown-rendering/long-table-8000.png` |
| F30.toggle | stop agent-server, click experimental-switch-conversation_reactions --force | one error toast per failed switch → PATCH /api/settings/experimental/conversation_reactions 502; toasts 'An error occurred' then ~5 s later 'Could not change the feature. Please try again.' (two runs: 12:53:51/12:53:57 and 12:55:32/12:55:37) | fail | Known failure #19933 reproduced | `evidence/F30.toggle/failed-first-toast-run2.png` |
| F05.image-only-send | SDK 1.63.1 vision_is_active | openhands/deepseek-v4.1-flash vision detected → agent-server venv: vision_is_active() True for openhands/deepseek-v4.1-flash and deepseek/deepseek-flash (read-only python check); live image turn needs OpenHands-provider key | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.branch-from-here | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.code-block-copy | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.confirmation-mode | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.confirmation-shortcuts | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.conversation-mention-agent | agent reply linking a conversation | agent links render as mentions → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.corrective-nudge | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.critic-result | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.event-groups | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.events-match | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.hook-events | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.live-activity | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.markdown-alerts | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.markdown-file-preview | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.message-copy | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.message-timestamp | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.reload-mid-run | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.scroll-to-bottom | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.session-activity | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.skill-install-banner | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.status-indicator | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.stop-resume | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.streamed-reply | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.task-list | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.thinking | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.timestamps | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.tool-visualizers | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.workspace-path-links | F06 recipe | per map → not run | blocked | no model key in this session (DEEPSEEK_API_KEY unset) |  |
| F06.history-tied-boundary | F06 recipe | per map → not run | not-run | model-free half (30 refused messages / tied boundary) not run this pass for time; automatic-fetch half needs a model (DEEPSEEK_API_KEY unset) |  |
| F06.llm-not-configured-banner | second no-LLM launch | banner → not run this pass (time; needs a second stack) | not-run |  |  |
| F06.load-older-history | F06 recipe | per map → not run | not-run | model-free half (30 refused messages / tied boundary) not run this pass for time; automatic-fetch half needs a model (DEEPSEEK_API_KEY unset) |  |
| F06.markdown-inline-code | #19857 markdownInlineCode | n/a → only caller is ACP diff path formatting (get-acp-tool-call-content.ts); not reachable from a user message; needs an ACP agent producing a diff path with edge spaces | not-run | not reproduced live |  |
| F05.conversation-mention-picker | composer # on Home and in a conversation, flag off and on | flag off: no picker, no fetch; flag on: picker lists matching conversations newest activity first, current excluded, max 8; Enter/Tab inserts mention, Escape closes, no matches hides the menu; mid-word # does not open; fits 390px → flag off: #export on Home and 'see #kitchen' in a conversation -> menu count 0, network search total 0. flag on: '#export' fetched /api/conversations/search?limit=100 once, listed Safari then Quarterly (updated_at desc); in Safari conversation '#' listed the others but not Safari; 9 candidates -> 8 options, oldest dropped, list scrolls at 300px; ArrowUp/Down wrap; Enter inserted '[Quarterly billing export audit. Do not run any ...](conversation:5531c2979fe24873a04bc5233dafeffb) ' (caret after the trailing space, focus stays in composer); Tab inserted Kitchen; '#zzqq' no menu; Escape closes leaving '#', next char reopens; 'abc#export' no menu; long title cut to 80 chars without []()"; title '[ ] ( )' inserts '[untitled conversation](conversation:...)'; phone 390: menu 326x300 inside viewport, no overflow | pass |  | `evidence/F05.conversation-mention-picker/home-export-2.png` |
| F05.resolved-banner | PATCH tags resolved=user, send a message (Agent Server 1.63.1) | server neither sets nor clears resolved; notice stays after send → banner count 1 after send; tags still clientsource/resolved:user/project:qa | pass | version check for coordinator; tags restored | `evidence/F05.resolved-banner/after-send-1631.png` |
| F06.clock-skew-send | browser clock +300000, send | Sending... then absent, no retry, server ts → browser 13:11:57 vs date -u 13:06:57; Sending... -> absent; sending/retry 0; event ts 13:06:57.95 (server) | pass |  |  |
| F06.conversation-mention-link | user message containing [Title](conversation:<hex>) | flag off: plain title text; flag on: link to /conversations/<id> opening in same tab, Back returns → flag off: conversation-mention-text 'Kitchen timer widget sketch', not inside <a>; flag on: conversation-mention link href /conversations/<32 hex>, title attr = id, underlined; click navigated same tab (tabs=1), Back returned; also rendered on the first message of a conversation started from Home; phone: inside viewport | pass |  | `evidence/F06.conversation-mention-link/link-desktop.png` |
| F06.empty-state-suggestions | New thread picker > launch-no-workspace | Let's start building! + 4 chips, Initialized session group, chip fills composer and hides suggestions, reload/phone/new tab keep them → as expected: 4 chips, event-group 1 toggles aria-expanded true, Fix README fills composer and count 0, cleared -> back, reload 1, phone inside viewport no overflow, new tab shows them; pong reply blocked (no model key in this session (DEEPSEEK_API_KEY unset)) | pass |  | `evidence/F06.empty-state-suggestions/same-tab.png` |
| F06.error-banner | send while agent-server stopped | banner with message, icon, Copy, Close; Close removes → 'HTTP request failed (502 Bad Gateway): "Bad Gateway: connect ECONNREFUSED 127.0.0.1:18821"' with icon/copy/dismiss, no Retry; dismiss -> count 0 | pass |  | `evidence/F06.error-banner/banner-after-failed-send.png` |
| F06.error-events | message to a dummy-key conversation | warning banner with error text, composer Error → error-message-banner + warning-message-banner-icon, litellm.BadRequestError text, composer Error; events LLMBadRequestError ConversationErrorEvent. Note: banner is live-only; after reload or reopening, count 0 (status Error stays) | pass |  | `evidence/F06.error-events/banner.png` |
| F06.failed-send-persists | failed send, restart, leave via New Chat and reopen | Retry row survives; resend works; Retry delivers once → retry 1 after restart and after reopen; resend Sending...->settled, retry still 1, 1 user row; Retry -> detached, 2 user rows | pass |  | `evidence/F06.failed-send-persists/retry-after-reopen.png` |
| F06.image-attachments | upload image, send | thumbnail in bubble; lightbox closes with Escape and X → image-preview 1 in bubble; lightbox 1 -> Escape 0; X 0; SEEN reply blocked (no model key in this session (DEEPSEEK_API_KEY unset)) | pass |  | `evidence/F06.image-attachments/bubble.png` |
| F06.markdown-rendering | Paper user-message syntax (after map fix) | palette #615448 italic / #241c17 bold / #45572f → rgb(97, 84, 72) italic, rgb(36, 28, 23) 700, rgb(69, 87, 47) | pass |  | `evidence/F06.markdown-rendering/paper-user-code.png` |
| F06.pending-messages | submit with --observe chat-message-sending; send while agent-server stopped | Sending... then absent; failed send shows Failed to send Retry Dismiss, Retry once → Sending... 63ms -> absent 86ms; down: Sending... -> 'Failed to send Retry Dismiss', retry while down fails again, Dismiss removes it, Retry after restart delivered PONG once (1 user row) | pass |  |  |
| F06.phone | 390x844, user message with wide table | chat fits; table scrolls inside → chat-interface insideViewport true, no page overflow; markdown-table-scroll scrollWidth 891 > clientWidth 326 (user-message table, agent table blocked) | pass |  | `evidence/F06.phone/conversation.png` |
| F06.reconnect | idle (Ready) conversation, service stop agent-server | Reconnecting... within ~2s, no banner/toast for 70s, reconnects without reload → Reconnecting... after 0.1 s; no error-message-banner in 70 s, no status region, 0 toasts; after restart 'Reconnecting' hidden without reload. On a conversation in Error status the composer keeps 'Error' and never shows Reconnecting (model-free conversations end in error; use an idle API-created one) | pass |  | `evidence/F06.reconnect/idle-70s-after-stop.png` |
| F06.user-and-agent-messages | 25-line user message | clipped with gradient, View More expands → truncation-gradient + chat-message-expand listed; click expands, both gone, 'filler line 24' shown; agent OK reply blocked (no model key in this session (DEEPSEEK_API_KEY unset)) | pass |  | `evidence/F06.user-and-agent-messages/expanded.png` |
| F09.desktop-nav | settings-navbar-desktop on /settings/experimental | nine links, Experimental last, one aria-current → Agent, LLM, Model Router, Agent Context, Verification, Runtime, Application, Secrets, Experimental; 1 aria-current; header 'Experimental' + subline 'Experimental features you can turn on or off. Changes apply to conversations you start afterwards.' | pass |  |  |
| F09.entry-command-menu | command menu 'Experimental' + Enter | opens /settings/experimental → 1 option, Enter -> /settings/experimental | pass |  |  |
| F30.conversation-mentions | Settings > Experimental > Conversation mentions | switch listed with description, persists, gates # picker and links → third of five switches; body.2.enabled true after click, checked after reload; flag off: no picker/no fetch, mention plain text; flag on: picker + links, an earlier mention became a link without a new conversation | pass |  | `evidence/F30.toggle/mentions-on.png` |
| F30.open | /settings/experimental | heading, one switch per server feature in API order, notice → 5 switches: Conversation reactions, Decision cards, Conversation mentions, Message edits, Factories (API order); conversation_mentions label 'Conversation mentions' with description 'The agent can find your other conversations by title, read one you point it at, and link to them in its answers. Applies to conversations started after you turn it on.'; notice text matches | pass |  | `evidence/F30.open/desktop.png` |
| F30.toggle | click experimental-switch-conversation_mentions --force | API enabled true, survives reload → GET /api/settings/experimental body.2.enabled true; after reload checkbox checked true | pass |  | `evidence/F30.toggle/mentions-on.png` |
