# Verification ledger — run 2026-11-26T0908-53a24d

Revision `6deb332c3602329306180fd7a99b3534753909df`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18810.

Checks: 16 — pass 15, fail 1, blocked 0, not-run 0, xfail 0, xpass 0. Families: 9.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F02 | 1 | 0 | 0 | 0 | 0 | 0 |
| F05 | 2 | 0 | 0 | 0 | 0 | 0 |
| F07 | 1 | 0 | 0 | 0 | 0 | 0 |
| F10 | 1 | 0 | 0 | 0 | 0 | 0 |
| F20 | 0 | 1 | 0 | 0 | 0 | 0 |
| F25 | 1 | 0 | 0 | 0 | 0 | 0 |
| F30 | 3 | 0 | 0 | 0 | 0 | 0 |
| F31 | 1 | 0 | 0 | 0 | 0 | 0 |
| F32 | 5 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F20.rail-label | demo-page rail entry | Extension demo (nav_label) → Hello from an extension; installed manifest pages have only id,title,path on 1.64.1 | fail | software-agent-sdk#5501 still reproduces on Agent Server 1.64.1 | `evidence/F20.rail-label/rail-1641.png` |
| F02.nav-links | rail with Projects and Factories on | Projects (with +) between Automate and Factories → Automate, Projects, New project, Factories, then extension row; Projects aria-current=page on /projects | pass |  | `evidence/F02.nav-links/projects-factories-rows.png` |
| F05.resolved-banner | real project member, resolved=auto | notice with auto note; send clears tag; Reopen via project route → notice + 'Resolved automatically: 100% sure nothing is left for you.'; after send server removed resolved+resolvenote and banner count 0 without reload; resolved=user Reopen POST 204, tags lose resolved, focus chat-input, no toast; phone bbox inside; resolved=yes no notice | pass | model litellm_proxy/deepseek/deepseek-chat via eval proxy | `evidence/F05.resolved-banner/real-member-auto.png` |
| F05.resolved-banner | fake project=qa tag | refused reopen toasts → PATCH with real project hex refused 422 'A conversation joins a project only when the project's coordinator starts it'; project=qa shows notice, Reopen POST 422 toasts Couldn't reopen this thread. Please try again. | pass |  | `evidence/F05.resolved-banner/qa-tag-projects-on.png` |
| F07.unreadable-event-file | damaged conversation | opens, damaged events skipped, no banner → 9 user messages (qa tall 11 missing), banner 0, socket open, 60 events from search; same at phone | pass |  | `evidence/F07.unreadable-event-file/cut-short-message-event-desktop.png` |
| F10.subscription | ChatGPT subscription Connect, backend offline | device/start 502 or 504 → 502, status 'Unable to connect your ChatGPT subscription... 502: OpenAI is unreachable' | pass | no screenshot in block; network assertion output | `../wD-f10c.out` |
| F25.manage-backends | Manage backends | row shows v<version> → Connected Local v1.64.1 http://127.0.0.1:18810 | pass |  | `evidence/F25.manage-backends/version-1641.png` |
| F30.conversation-mentions | experimental-switch-conversation_mentions | third switch; enabled after click and reload → body.2.enabled true; checked after reload; order conversation_reactions,ask_user,conversation_mentions,message_edits,factories,projects | pass |  | `evidence/F30.conversation-mentions/on.png` |
| F30.open | /settings/experimental | one switch per server feature in API order → six switches: Conversation reactions, Decision cards, Conversation mentions, Message edits, Factories, Projects; notice below (Agent Server 1.64.1) | pass |  | `evidence/F30.open/desktop-six.png` |
| F30.toggle | experimental-switch-projects | PATCH saves, survives reload → body.5 projects enabled true; checked after reload | pass |  | `evidence/F30.toggle/projects-on.png` |
| F31.list | /factories | factories page with automation 1.36.0 + AS 1.64.1 → capabilities include factories; factories-empty and factories-new present | pass |  | `evidence/F31.list/factories-1641.png` |
| F32.coordinator | project-open-coordinator | opens coordinator chat; message reaches it → opened /conversations/abddd991...; coordinator called start_child_conversation; worker appeared resolved=auto | pass |  | `evidence/F32.coordinator/opened.png` |
| F32.create | New project modal | POST creates project + idle coordinator tagged project=<id> → URL /projects/86f9757f...; coordinator abddd991 idle, tags {project:<id>}, 0 events | pass |  | `evidence/F32.create/project-page.png` |
| F32.entry | rail Projects + New project | rail item and + on default 1.64.1 launch → sidebar-projects-link and sidebar-new-project 1 each; + opens /projects?new=1 | pass |  | `evidence/F32.list/empty.png` |
| F32.list | /projects | No projects yet, then newest first → projects-empty 'No projects yet.'; rows QA F32 second above QA F32 | pass |  | `evidence/F32.list/two-rows.png` |
| F32.off | /projects with projects off | projects-off notice, no rail item → sidebar-projects-link 0; projects-off text + link /settings/experimental | pass |  | `evidence/F32.off/projects-off.png` |
