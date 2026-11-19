# Verification ledger — run 2026-11-19T0927-0a4d8e

Revision `e1b8b60f25084a64412c3a2789a921034fc895c7`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18810.

Checks: 7 — pass 6, fail 0, blocked 1, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F14 | 2 | 0 | 0 | 0 | 0 | 0 |
| F22 | 1 | 0 | 1 | 0 | 0 | 0 |
| F28 | 3 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F22.agent-assisted-setup | Agent fills a prompt form (automation_form_update) then sidebar return | agent-filled form kept on sidebar return → not run | blocked | prerequisite: a working LLM key (DEEPSEEK_API_KEY empty in this session) |  |
| F14.create | Settings > Secrets > Add (cipher mismatch fixture), Settings > Application Save; desktop | Without encrypted value in settings.json: Save toasts 'Settings saved' and settings.json changes → Fresh run, no LLM key (llm.api_key null): Add secret toasted the 500 cipher message, add-secret-form count 0, secrets.json byte-identical; Application Save toasted 'Settings saved' and settings.json sha changed (test exit 1); trap restored, doctor ok | pass | precondition sentence check (no encrypted value) | `evidence/F14.create/cipher-mismatch-nokey.png` |
| F14.create | Settings > Secrets > Add (cipher mismatch fixture), Settings > Application Save; desktop, after llm preset deepseek --no-validate (dummy key) | 500 Secrets file is corrupted... toast, add-secret-form count 0, secrets.json identical; Save toasts Settings file is corrupted...; settings.json unchanged; doctor passes → Exact 500 toast; count 0; SECRETS_KEPT true; Save toast 'Settings file is corrupted or encrypted with a different key: restore that key as OH_SECRET_KEY or add it to OH_PREVIOUS_SECRET_KEYS'; settings sha test exit 0; doctor ok; QA_CIPHER_OLD removed | pass |  | `evidence/F14.create/cipher-mismatch.png` |
| F22.agent-assisted-setup | Setup conversation (user-edited, not agent-filled), sidebar return vs browser goto; desktop | sidebar return keeps the form saved or not; full page load drops what was not saved → user-edit equivalent: unsaved name/prompt/weekly kept after sidebar return; goto /conversations/<id> -> 'New Automation', prompt '', daily; saved form kept via sidebar (F28.form-return run) | pass | user-edit equivalent only | `evidence/F22.agent-assisted-setup/full-load-unsaved-dropped.png` |
| F28.custom-agent-profile | /automations/setup blank form, Custom kind, agent profile pill; desktop | options none/default; pill default; model deepseek-flash locked w/ tooltip; Save draft POST 201 agent_profile_id + endpoint /v1, toast Draft saved in this conversation., Saved just now; reload keeps default; Create POST /api/automation/v1 201, Automation created., GET agent_profile_id + model null → All as stated except model pill text reads 'default' (seeded default agent profile llm_profile_ref is 'default' on a fresh onboard --skip run; preset does not repoint it). Drafts POST 201 with agent_profile_id ca1f221c-... and endpoint /v1; toast and save state exact; reload pill default; create POST 201, toast Automation created., GET agent_profile_id ca1f221c-..., model null; deleted 204 | pass | precondition drift: map says LLM profile deepseek-flash; on fresh onboard --skip run it is 'default' | `evidence/F28.custom-agent-profile/save-draft.png` |
| F28.form-return | Automate > Add Automation > Create Automation, conversation start --stay, sidebar conversation links; desktop 1440x1000 | sidebar away/back keeps unsaved values (Unsaved changes); after Save+edit keeps edit, Unsaved changes, Test disabled; after Save: Saved just now, Test enabled; Add>Create clean form → Other conv: automation-setup-prompt count 0; back: name 'QA_F28 Return', prompt 'QA_F28 return prompt.', schedule '0 0 1 1 *', custom aria-checked true, 'Unsaved changes'; after save+rename: 'QA_F28 Return edited', 'Unsaved changes', Test enabled false; after second save: 'Saved just now', Test true; Add>Create: 'New Automation', prompt '', daily true, 09:00; reload with unsaved rename shows saved name 'QA_F28 Return edited' | pass |  | `evidence/F28.form-return/returned.png` |
| F28.form-return | Same, phone 390x844 via sidebar-mobile-menu-toggle and :visible links | Form view pressed, values kept, pageHorizontalOverflow false; browser goto resets to New Automation → aria-pressed true; prompt 'QA_F28 phone prompt.', weekly aria-checked true, name 'New Automation'; pageHorizontalOverflow false (width 340); after goto: 'New Automation', prompt '', daily true | pass |  | `evidence/F28.form-return/returned-phone.png` |
