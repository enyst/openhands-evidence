# Verification ledger — run 2026-11-18T0930-c28f27

Revision `ef1e50d9502c334cdb5901b8173a5c79c610f04b`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18810.

Checks: 9 — pass 9, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F04 | 2 | 0 | 0 | 0 | 0 | 0 |
| F17 | 2 | 0 | 0 | 0 | 0 | 0 |
| F21 | 5 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F04.hide-older | View > More options, desktop | toggle false, cutoff Over 1 week; cutoff menu 4 radios; Escape -> cutoff-menu 0, modal 1, aria-checked unchanged, focus on cutoff button; second Escape closes dialog; Over 1 hour + toggle -> true; reload storage showOlderConversations:false, olderConversationCutoff:1h; More options · Custom → all as written; focus on dropdown-trigger inside older-conversation-cutoff; second Escape modal 0; storage and Custom label confirmed; restored Recent + Over 1 week | pass |  | `evidence/F04.hide-older/after-escape-desktop.png` |
| F04.hide-older | View > More options, phone 390 (drawer) | Escape closes cutoff menu, dialog stays, switch unchanged, focus on cutoff; second Escape closes dialog → menu 1->0, modal 1, aria-checked false, focus inside older-conversation-cutoff; second Escape modal 0. Note: at phone the View toggle must be scoped 'testid=sidebar-mobile-drawer >> testid=conversation-layouts-toggle' (two matches) | pass |  | `evidence/F04.hide-older/after-escape-phone-2.png` |
| F17.section-filter | /mcp section filter, desktop | snapshot expanded All/menu with All checked; Library hides Installed h2; Installed -> 0 marketplace sections, trigger Installed; reopen+Escape -> menu count 0, aria-expanded false, focus on trigger (Filter MCP servers) → all as written: h2 [MCP, Library]; count 0; text Installed; Escape: menu 0, aria-expanded false, activeElement aria-label 'Filter MCP servers' (dropdown-trigger in mcp-section-filter); restored All | pass |  | `evidence/F17.section-filter/after-escape-desktop.png` |
| F17.section-filter | /mcp section filter, phone 390 | Escape closes menu and returns focus to trigger → menu 1 -> 0 after Escape, aria-expanded false, focus on 'Filter MCP servers' | pass |  | `evidence/F17.section-filter/after-escape-phone.png` |
| F21.events-validation | /automations/events Add event source, desktop | duplicate -> 'That source identifier is already registered.' in form; 'QA_bad id' patternMismatch [true]; submit -> browser 'Please match the requested format.', form open, focus on field, no POST webhooks, no 'Pattern attribute value' console error; -issues/issues-/Issues same; maxlength stops at 50; listitems stay 2 → all as written: alert shown (409 only error); patternMismatch [true]; validationMessage 'Please match the requested format.', activeElement webhook-source-id, network total 0, errors only the 409; pattern attr [a-z0-9]([a-z0-9\-]{0,48}[a-z0-9])?; -issues, issues-, Issues each patternMismatch true + 0 requests; 59 held 'a' keydowns -> length 50; listitems 2 | pass |  | `evidence/F21.events-validation/rejected.png` |
| F21.filters | /automations Filters popover, desktop | Escape closes open status/trigger/tag/sort menu, focus to that field's trigger, popover stays; with no inner menu Escape does nothing; closes on outside click or Filters button → status/trigger/tag/sort menus 1->0 on Escape, focus on 'Filter by status'/'Filter by trigger'/'Filter by tag'/'Sort automations', popover 1, aria-expanded true; second Escape popover still 1; plain Escape popover 1; Filters button click -> 0; heading click -> 0 | pass |  | `evidence/F21.filters/after-second-escape.png` |
| F21.filters | /automations Filters popover, phone 390 | status menu Escape closes menu only; second Escape nothing → status menu 1->0, popover 1, focus 'Filter by status'; second Escape popover 1 | pass |  | `evidence/F21.filters/phone-after-second-escape.png` |
| F21.group-by | /automations Group by, list view, desktop | outside click closes menu; reopen + Escape -> group-by-menu 0, aria-expanded false, activeElement aria-label 'Group automations' → open 1 -> outside click 0; reopen 1 -> Escape 0, aria-expanded false, focus 'Group automations'. (Unedited: tag sections read nightly-checks (2): Beta,Alpha here because Alpha had no run in this re-verify) | pass |  | `evidence/F21.group-by/escape-after-desktop.png` |
| F21.group-by | /automations Group by, list view, phone 390 | same Escape behaviour at phone → outside click closes; Escape closes, aria-expanded false, focus 'Group automations' | pass |  | `evidence/F21.group-by/escape-after-phone.png` |
