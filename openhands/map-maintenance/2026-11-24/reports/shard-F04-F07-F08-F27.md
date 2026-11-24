# Verification ledger — run 2026-11-24T0902-6c7bff

Revision `7a9425ac0b1c1a648414fde7af23136c442204ca`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18840.

Checks: 49 — pass 46, fail 3, blocked 0, not-run 0, xfail 0, xpass 0. Families: 4.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F04 | 18 | 1 | 0 | 0 | 0 | 0 |
| F07 | 10 | 0 | 0 | 0 | 0 | 0 |
| F08 | 13 | 1 | 0 | 0 | 0 | 0 |
| F27 | 5 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F04.hover-preview | sidebar row hover, desktop 1440 | preview right of row, top level with row top (269) → preview top 113, bottom 301 = row bottom; opens upward (Known failure #19645, still open) | fail | known open issue #19645; text rows correct (title, Directory, Model, Agent profile default, Created) | `evidence/F04.hover-preview/desktop.png` |
| F08.files-auto-refresh | Files tab open with qa-notes.md previewed, agent bash appends to it, desktop | open preview ends with 'edited by agent' without Refresh → preview still 'QA notes / Hello world'; no request for qa-notes.md after the turn; reload shows the new body | fail | by design in use-auto-refresh-files-on-edit.ts (#19992 keeps file-content queries out for bash); intent gap, TBD-files-preview-bash | `evidence/F08.files-auto-refresh/after-bash.png` |
| F27.launch-child | launch requested while the browser is on /settings (#19841), desktop | a launch with no client attached fails visibly to agent and user, or the child is created → agent's launch_child_conversation observation 'Tool call dispatched to client.', agent replies OK, no QAZULU child exists (search lists only the earlier PONG child), no toast | fail | known open #19841 part 1 reproduced; conversation send <tools-id> then immediate browser goto /settings | `evidence/F27.launch-child/19841-while-away.png` |
| F04.archive | ⋮ > Archive on open conversation | confirm dialog, row hidden after reload, archived tag, leaves conversation → dialog 'Archive conversation'; url /conversations; count 0; archived true | pass |  |  |
| F04.card | sidebar row click, desktop | opens /conversations/<id>?backend=default-local, row active, check mark, transcript pong, no error banner → as expected | pass |  | `evidence/F04.card/reopened.png` |
| F04.collapse-all | Conversations header toggle | all folders collapse then expand → card count 0 then 5 | pass |  |  |
| F04.collapsed-rail | sidebar collapse toggle | no list collapsed; back after expand → count 0 then 1 | pass |  |  |
| F04.delete | ⋮ > Delete | confirm deletes on server → GET /api/conversations/<id> 404 | pass |  |  |
| F04.edit-tags | row ⋮ > Edit tags | validation error for 'Bad Key'; qaenv=one saved; Tags updated; chip persists → error text shown; Tags updated; chip 'Qaenv: one' after reload | pass |  |  |
| F04.empty-state | sidebar, fresh run, desktop | No conversations found → No conversations found | pass |  | `evidence/F04.empty-state/empty.png` |
| F04.folder-collapse | folder heading click | aria-expanded toggles → false then true | pass |  |  |
| F04.folder-new-conversation | folder + in qa-f04-folder | starts and opens a conversation in that folder → /conversations/eff11e61, folder count 0 -> 1 | pass |  |  |
| F04.grouped-folders | View > By workspace, desktop | folder per workspace plus No workspace → folders for qa-f04-repo, qa-f04-folder, qa-repo, No workspace, plus a folder for the child's tagged scratch dir holding parent+child | pass |  | `evidence/F04.sub-conversations/by-workspace.png` |
| F04.hover-preview | phone drawer row hover, 390 and 320 px | preview stays inside the viewport (closed #19147) → preview opens below the row (row 285-333, preview y 336 x 12 w 282), insideViewport true, no page overflow; 320 px: y 317, inside | pass | #19147 fixed by #19150 | `evidence/F04.hover-preview/phone-drawer.png` |
| F04.new-conversation-in-sandbox | local row ⋮ menu | no New Conversation in Sandbox item → Rename, Edit tags, Stop, Download, Archive, Delete only | pass |  |  |
| F04.new-thread-picker | folder-plus picker, desktop | No workspace, qa-f04-folder, qa-f04-repo, + Add Workspace, Manage Workspaces; picking qa-f04-repo starts and opens a conversation there → same list; /conversations/d1a60c81 with workspace .../workspace/qa-f04-repo; launch-no-workspace opened bdef4f30 | pass |  |  |
| F04.phone | 390 px drawer | panel fits, rows 48 px, row pick closes drawer → inside, no overflow; 48 px rows; pick -> conversation, drawer hidden | pass |  | `evidence/F04.phone/drawer.png` |
| F04.show-archived-unarchive | More options > Show archived; ⋮ > Unarchive | Archived chip; unarchive without dialog → chip 1; no dialog; chip 0 | pass |  |  |
| F04.sub-conversations | sidebar Recent, desktop | child with parent_conversation_id nests under its parent behind a collapsed 'Child conversations (N)' toggle; expanding shows it indented, it opens the child; manual collapse; opening the child (reload) auto-expands its parent; nesting in By workspace → toggle aria-expanded false -> true, group 'Child conversations (1)' with PONG Only Reply link; click opens /conversations/<child>; collapse hides row; reload on child: expanded true, row active; By workspace: child nested under parent in its folder | pass | also collapsed.png, child-open-autoexpand.png, by-workspace.png; #20010 | `evidence/F04.sub-conversations/expanded.png` |
| F04.sub-conversations | phone drawer 390 px | toggle and child row inside the drawer; picking the child opens it and closes the drawer → group bbox x26 w263 inside viewport, no overflow; child click -> /conversations/8add4dda, drawer hidden | pass |  | `evidence/F04.sub-conversations/phone-drawer.png` |
| F04.view-menu | View menu, desktop, no conversations | presets with Recent checked, Filter by tags (No tags yet), More options, Delete all disabled; Escape closes → as expected: Recent [checked], Delete all [disabled], No tags yet, menu count 0 after Escape | pass |  |  |
| F07.display-cost | menu Display Usage and Cost, desktop | drawer opens on Usage, URL unchanged → usage-panel, aria-pressed true, /conversations/<id> | pass |  |  |
| F07.download-zip | menu Download conversation data | zip with base_state.json and bash_events/ → zip downloaded with base_state.json, bash_events | pass |  |  |
| F07.menu-open | header ... menu, desktop | items rename..delete; Escape closes with focus on ...; outside click closes → rename, skills, hooks, agent-tools, export, download, display-cost, stop, delete; Escape -> count 0, focus ellipsis-button; outside click -> 0 | pass |  |  |
| F07.missing-redirect | unknown id URL, desktop | one 'does not exist' toast, redirect to /conversations → redirected; history has exactly 1 entry | pass |  |  |
| F07.open-by-url | /conversations/<id>, desktop | header, generated title, 1 agent message, last-conversation slot → Pong Command, count 1, {"default-local":"1f1f491a…"} | pass |  |  |
| F07.phone | header at 390 px | header 48 px; ... menu inside viewport → header 390x48; menu x133 w249 inside, no overflow | pass |  | `evidence/F07.phone/header-menu.png` |
| F07.rename-inline | header dblclick + Enter, desktop | toast, sidebar row and header read new title after reload → Conversation title updated successfully; QA_F07 renamed in header and row after reload | pass |  |  |
| F07.rename-inline | menu Rename + Escape, desktop and phone (closed #19986) | Escape cancels: input gone, title restored, More options back with focus, no save → input count 0, title QA_F07 renamed, ellipsis-button focused, 0 toasts, server title unchanged; phone dblclick+Escape same; empty value reverted without toast | pass | video evidence/F07.rename-inline/escape-cancels.mp4; phone evidence/F07.rename-inline/phone-escape.png; fixed by #19997 | `evidence/F07.rename-inline/escape-restored.png` |
| F07.skills-modal | menu Show Available Skills | Public skills list; Escape closes → Public skills 15; closed on Escape | pass |  |  |
| F07.stale-launch-url | /conversations/launch-0000… | New Chat header, unavailable message, Back → New Chat, Git actions, 'This start is no longer available in this tab…', Back | pass |  |  |
| F08.changes-from-overview | Overview Changes row, desktop | counts +N/-N as the smallest set of changed lines (a line moved from the end to the top counts +1 -1); click opens Commits with Uncommitted expanded, overview hidden → +7 -0 before; after moving 'line 10' to the top of committed qa-lines.txt: +8 -1 (git numstat 1/1); click: aria-pressed true, commit-list visible, Uncommitted expanded, overview hidden | pass | #19580 LCS counting; pre-#19580 greedy walk would give +9 -9 for this move | `evidence/F08.changes-from-overview/lcs-moved-line.png` |
| F08.drawer-state-reload | reload with Commits selected | drawer closed after reload, reopens on Commits → aria-pressed false; reopen shows commit-list | pass |  |  |
| F08.files-auto-refresh | Files tab open, agent bash creates files, desktop (closed #19985) | qa-nul.bin, qa-real.docx, qa-dot.png listed without Refresh → all three listed without Refresh | pass | fixed by #19992 | `evidence/F08.files-auto-refresh/after-bash.png` |
| F08.files-auto-refresh | file_editor create + bash rm, desktop | qa-editor.txt appears, qa-blob.bin gone without Refresh → counts 1 / 0 | pass |  | `evidence/F08.files-load-error/deleted-open-file.png` |
| F08.files-load-error | open file deleted by agent | Failed to read qa-blob.bin: 404 → Failed to read qa-blob.bin: 404; network 404 | pass |  | `evidence/F08.files-load-error/deleted-open-file.png` |
| F08.files-refresh | Files Refresh, local, desktop | re-reads list and open file → preview gained the arranged 'refresh marker 2' line after one click | pass |  | `evidence/F08.files-refresh/preview-after-refresh-2.png` |
| F08.files-tree | Files tree, desktop, no manual Refresh | src collapsed then expanded; calc.py 4 lines; quick-row item → as expected without clicking Refresh | pass |  | `evidence/F08.files-tree/calc.png` |
| F08.panel-direct-url | /conversations/<id>/panel at desktop | redirect to /conversations/<id> with drawer open → url replaced, back count 0, aria-pressed true | pass |  | `evidence/F08.panel-direct-url/desktop-redirect.png` |
| F08.panel-toggle | chat header toggle, desktop | Show panel -> Hide panel, aria-pressed true, Files with tree → as expected | pass |  | `evidence/F08.panel-toggle/drawer-open-files.png` |
| F08.phone-panel-page | toggle at 390 px | navigates to /panel; Files fits; Back returns → /panel; files-tab inside viewport, no overflow; Back -> /conversations/<id> | pass |  | `evidence/F08.phone-panel-page/panel.png` |
| F08.tab-bar | drawer tab bar, desktop | Commits switches body; clicking active tab closes drawer → commit-list visible; second click -> aria-pressed false, tabs hidden | pass |  |  |
| F08.tabs-menu | tab bar ellipsis menu | open+pin row per tab; choosing Usage opens it and closes menu → 12 rows for 6 tabs; usage-panel shown; menu count 0 | pass |  |  |
| F08.uncommitted-changes | Commits tab, desktop | - Uncommitted N files, then commits newest first with authors → - Uncommitted 8 files; QA agent commit (QA-Agent), Initial fixture commit (QA Fixture) | pass |  |  |
| F27.canvas-ui-open-tab | agent canvas_ui_control open_tab terminal, desktop | drawer opened by the agent on Terminal → aria-pressed true, tabs-pane-header starts Terminal | pass |  |  |
| F27.launch-child | agent launch_child_conversation on <tools-id>, desktop | toast Launched a local child conversation Open; [child-conversation] launched message; child finishes with PONG → toast seen; child 8add4dda finished with PONG; parent_conversation_id = parent id; child row nested under parent (count of top-level PONG card 0 until expanded) | pass | recipe's 'browser count conversation-card has-text=PONG is 1' needs the parent's Child conversations toggle expanded first (#20010) |  |
| F27.launch-child | reopen parent after the lost launch: sidebar click, reload, browser reset + onboard (#19841 part 2) | reopening starts no child from history → no new child after 20 s each way (6 conversations, children only 8add4dda), no toast | pass | late/duplicate launch on reopen not reproduced on 7a9425a, Agent Server 1.63.1 | `evidence/F27.launch-child/19841-fresh-browser.png` |
| F27.overview-peek | hover (i) with drawer open on <tools-id> | peek Overview/Changes/Workspace; click opens column, closes drawer → peek 'Changes +4 -0 Workspace None'; overview pressed, panel not pressed | pass |  |  |
| F27.phone | /conversations/<tools-id>/panel at 390 px, tabs menu > Usage | Usage hidden from the 390 px row while Commits is active; picking it from the menu shows the Usage panel and puts the selected Usage tab in the row → before: row files..browser, no conversation-tab-usage; after: conversation-tab-usage selected at x 262 y 5.5 inside viewport; usage-panel 390 wide, no overflow | pass | #19995 | `evidence/F27.phone/usage.png` |
