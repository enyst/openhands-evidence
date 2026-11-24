# Verification ledger — run 2026-11-24T0901-8c172a

Revision `7a9425ac0b1c1a648414fde7af23136c442204ca`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18820.

Checks: 20 — pass 18, fail 0, blocked 2, not-run 0, xfail 0, xpass 0. Families: 2.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F31 | 16 | 0 | 2 | 0 | 0 | 0 |
| F32 | 2 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F31.turn-on | Cloud/Enterprise enable_factories flag, member without manage_automations | flag shows Factories; member sees no New factory/Rename/Delete/Change factory → not reachable locally | blocked | Prerequisite: Cloud account or Enterprise backend |  |
| F31.worklogs-unavailable | Factory page > Worklogs (Enterprise) | Worklogs nav item and worklog panel, newest first → local backend has no license status | blocked | Prerequisite: OpenHands Enterprise backend whose license grants worklogs plus worklog routes (OpenHands/enterprise#1392) |  |
| F31.change-factory | Automation actions > Change factory (desktop) | options No factory + factory, current selected; toast; factory_id null; count 0; ?factory dropped; factory empty → options [No factory, QA Factory Renamed], value=958e9a26-d183-445e-af2c-6f7a8fe6ab44; toast 'QA_F31 In Factory is no longer in a factory.'; url w/o ?factory; factory_id null; automation_count 0; factory page empty | pass |  | `evidence/F31.change-factory/after-toast.png` `evidence/F31.change-factory/after.png` |
| F31.create | /factories > New factory (desktop) | dialog; Create opens /factories/<id>; API lists it with count 0; row shows name and 0 → URL /factories/958e9a26-d183-445e-af2c-6f7a8fe6ab44; API QA Factory One automation_count 0; row 'QA Factory One / 0' | pass |  | `evidence/F31.create/list-with-factory.png` |
| F31.create | /factories > New factory (phone 390x844) | dialog fits; Create opens /factories/<id> → dialog visible; opened /factories/aab7271e-...; no horizontal scroll (scrollWidth 390) | pass |  | `evidence/F31.create/phone-dialog.png` |
| F31.delete | Factory page kebab > Delete (desktop) | confirm dialog names factory; with a live automation: dialog closes, error toast, factory kept; empty: navigates to /factories, factory gone → dialog 'Delete the factory "QA Factory Renamed"? This can't be undone.'; 409 toast 'Factory has 1 live automation; remove them from it first'; after removing it: /factories empty, API total 0, GET factory 404 | pass |  | `evidence/F31.delete/confirm.png` `evidence/F31.delete/blocked-409.png` `evidence/F31.delete/after-delete.png` |
| F31.delete | Factory page kebab > Delete (phone 390x844) | confirm dialog fits; delete returns to /factories → dialog fits; /factories empty state | pass |  | `evidence/F31.delete/phone-confirm.png` `evidence/F31.list-empty/phone-empty.png` |
| F31.hidden-when-off | Sidebar + direct URL /factories (desktop) | no sidebar-factories-link; /factories shows unsupported message → count 0; 'This automation service does not support factories.' | pass |  | `evidence/F31.hidden-when-off/direct-url.png` |
| F31.keep-factories | Factory page > automation card (desktop) | ?factory=<id>; Factories aria-current=page; Back href factory page → url ...?factory=958e9a26-d183-445e-af2c-6f7a8fe6ab44; aria-current page; Back href /factories/958e9a26-d183-445e-af2c-6f7a8fe6ab44 | pass |  | `evidence/F31.keep-factories/detail.png` |
| F31.list-empty | Sidebar Factories (desktop) | /factories empty state + New factory → No factories yet / A factory is a group of automations. This organization has none yet.; New factory | pass |  | `evidence/F31.list-empty/empty.png` |
| F31.not-found | Direct URL /factories/<zero uuid> (desktop) | API 404; Factory not found + Back to factories → 404; 'Factory not found'; 'Back to factories' | pass |  | `evidence/F31.not-found/not-found.png` |
| F31.open | /factories row link (desktop) | factory page: nav titled with name, Automations, Back to factories, empty state → url /factories/958e9a26-d183-445e-af2c-6f7a8fe6ab44; 'No automations in this factory yet'; navbar 'QA Factory One / Automations'; 'Back to factories' | pass |  | `evidence/F31.open/factory-page.png` |
| F31.open | Factory page (phone 390x844) | factory page with Automations nav strip, Back to factories, kebab, empty state → factory-navbar-mobile 'Automations', back link, kebab, empty state; factory name not shown on phone (heading is desktop-only) | pass | On phone the layout's heading (factory name) is hidden; only dialogs name the factory | `evidence/F31.open/phone-factory-page.png` |
| F31.rename | Factory page kebab > Rename (desktop) | dialog prefilled; new name in API and nav title → prefilled 'QA Factory One'; API + navbar 'QA Factory Renamed' | pass |  | `evidence/F31.rename/renamed.png` |
| F31.scoped-dashboard | /factories/<id> and /automations (desktop) | factory page shows only its automation; /automations shows both → factory: in=1 out=0; /automations: in=1 out=1 | pass |  | `evidence/F31.scoped-dashboard/factory-dashboard.png` `evidence/F31.scoped-dashboard/automations-all.png` |
| F31.turn-off | Settings > Experimental > Factories off (desktop) | API false; no sidebar entry after reload; /factories unsupported → enabled false; count 0; factories-unsupported shown | pass |  | `evidence/F31.turn-off/unsupported.png` |
| F31.turn-on | Settings > Experimental > Factories (desktop) | saves; API enabled true; sidebar Factories after reload → API enabled true; sidebar-factories-link text Factories | pass |  | `evidence/F31.turn-on/sidebar-entry.png` |
| F31.worklogs-unavailable | Direct URL /factories/<id>/worklogs (local backend, desktop) | no Worklogs nav item; worklogs-unsupported message → factory-navigation-worklogs count 0; 'Worklogs are not available on this deployment.' | pass |  | `evidence/F31.worklogs-unavailable/direct-url.png` |
| F32.off | Rail + /projects + /projects/<id> (desktop, Agent Server 1.63.1 without projects) | no Projects rail item; off notice linking /settings/experimental; no /api/projects call → sidebar-projects-link 0; projects-off 'Projects is turned off on this Agent Server. Turn it on in Settings › Experimental.' href /settings/experimental on both routes; 0 /api/projects in network log | pass |  | `evidence/F32.off/projects-off.png` `evidence/F32.off/project-off.png` |
| F32.off | Conversation tagged project=<hex> (desktop, projects unavailable) | no project badge, no project sidebar/tab, no Project file in + menu → conversation-project-badge 0; project-sidebar 0; Project tab 0; add-project-file-button 0 | pass |  | `evidence/F32.off/tagged-conversation.png` `evidence/F32.off/plus-menu.png` |
