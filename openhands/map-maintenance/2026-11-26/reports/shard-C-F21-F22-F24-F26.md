# Verification ledger — run 2026-11-26T0900-8def37

Revision `6deb332c3602329306180fd7a99b3534753909df`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18810.

Checks: 6 — pass 6, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F21 | 1 | 0 | 0 | 0 | 0 | 0 |
| F22 | 1 | 0 | 0 | 0 | 0 | 0 |
| F24 | 4 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F21.sidebar-entry | Sidebar Automate | /automations, heading Dashboard, nav list/templates → URL /automations, h1 Dashboard, automations-navigation-list/-events/-templates listed, one QA_F24 Sync card | pass |  | `evidence/F21.sidebar-entry/dashboard.png` |
| F22.setup-review-confirm | Templates > Custom automation > Continue > fill > Review > Confirm and create | Review lists fields; Confirm creates enabled automation, URL replaced by detail → Review: Action Prompt, Schedule 0 0 1 1 *, UTC, QA_F22 Custom, LLM profile Not set, 60, Prompt, Repository/Branch Not set; detail /automations/5702268f..., h1 QA_F22 Custom, Active; API enabled true schedule 0 0 1 1 * timeout 60 model null | pass | No DEEPSEEK_API_KEY in env: LLM profile combobox disabled ('No saved profiles'), so model step skipped | `evidence/F22.setup-review-confirm/review.png` |
| F24.keep-activation-local | Automate > Git Sync > Configuration (end of form) | switch 'Keep automation activation status local' + help text shown when status reports keep_activation_local; follows stored value; Save enabled only when differs → switch present, unchecked (status false), help text 'Git records what each automation does, not whether it is on. ...'; Save false->true on flip, false again on flip back | pass |  | `evidence/F24.keep-activation-local/off-desktop.png` |
| F24.keep-activation-local | Flip switch, Save Changes, reload | PUT git-sync/config body only {keep_activation_local:true}, no check; persists across reload → network --bodies: one PUT /api/automation/v1/git-sync/config body {"keep_activation_local":true} status 200, toast saved; after reload checked=true, Save disabled, status keep_activation_local:true; turning off sends {"keep_activation_local":false} | pass |  | `evidence/F24.keep-activation-local/on-after-reload.png` |
| F24.keep-activation-local | Turn synced automation on/off with option on, Sync now | Pending 0, no commit; description edit commit has no enabled/state lines → control (off): toggle gave dirty 1 and commit 65c9d87 enabled/state diff. With option on: PATCH enabled:true -> Pending 0, Sync now -> Sync complete, qa-sync head unchanged 65c9d87; description PATCH -> Pending 1, commit 7c67709 adds description and removes enabled:/state: lines; DB enabled stays true | pass | PATCH is arrange; git log in fixture repo is proof | `evidence/F24.keep-activation-local/pending-zero-after-toggle.png` |
| F24.keep-activation-local | Same at browser viewport phone | switch and help text fit 390px → bbox insideViewport true, pageHorizontalOverflow false; label wraps to two lines | pass |  | `evidence/F24.keep-activation-local/phone.png` |
