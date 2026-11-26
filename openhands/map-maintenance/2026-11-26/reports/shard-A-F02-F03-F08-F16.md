# Verification ledger — run 2026-11-26T0900-42039b

Revision `6deb332c3602329306180fd7a99b3534753909df`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18820.

Checks: 12 — pass 12, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 4.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F02 | 4 | 0 | 0 | 0 | 0 | 0 |
| F03 | 6 | 0 | 0 | 0 | 0 | 0 |
| F08 | 1 | 0 | 0 | 0 | 0 | 0 |
| F16 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F02.mobile-drawer | phone 390x844, conversation page, swipe right from chat panel x=48 to 260 | drawer opens (aria-expanded true, sidebar-mobile-drawer 300px), URL unchanged → drawer opened, expanded=true, URL unchanged | pass | Touch synthesized with browser eval (new Touch/TouchEvent dispatched on elementFromPoint, 8 moves) because control-openhands has no touch/swipe verb (harness gap); eval is documented read-only, so this is a stopgap, not CLI-recipe proof. Conversation on a dummy-key LLM profile (no DEEPSEEK_API_KEY in env). | `evidence/F02.mobile-drawer/swipe-open.png` |
| F02.mobile-drawer | phone: swipes from x=10 (gutter), x=23, x=150 (past third 130), vertical, 40px short, on chat-input | no drawer → drawer count 0, aria-expanded false each time; x=25 opens | pass | Touch synthesized with browser eval (new Touch/TouchEvent dispatched on elementFromPoint, 8 moves) because control-openhands has no touch/swipe verb (harness gap); eval is documented read-only, so this is a stopgap, not CLI-recipe proof. Conversation on a dummy-key LLM profile (no DEEPSEEK_API_KEY in env). | `evidence/F02.mobile-drawer/swipe-rejected-closed.png` |
| F02.mobile-drawer | phone: chat header hamburger after swipe close | drawer opens → drawer opens | pass |  | `evidence/F02.mobile-drawer/hamburger-after-swipe.png` |
| F02.mobile-drawer | desktop 1440x1000 and 800x900: same swipe | nothing happens → no drawer, rail unchanged, URL unchanged | pass | Touch synthesized with browser eval (new Touch/TouchEvent dispatched on elementFromPoint, 8 moves) because control-openhands has no touch/swipe verb (harness gap); eval is documented read-only, so this is a stopgap, not CLI-recipe proof. Conversation on a dummy-key LLM profile (no DEEPSEEK_API_KEY in env). | `evidence/F02.mobile-drawer/swipe-desktop-no-effect.png` |
| F03.feedback | desktop Home, top-right Feedback button | button top right at md+, opens Feedback dialog with info, message, optional email, privacy, hint, disabled Send → button at x=1285,y=12; dialog matches; Send feedback disabled when empty | pass |  | `evidence/F03.feedback/modal-empty.png` |
| F03.feedback | hover info button | role=tooltip privacy disclosure → Your feedback and any email you provide are sent to PostHog when you submit. This does not enable analytics. | pass | Cosmetic: tooltip wraps mid-word ('anal ytics') | `evidence/F03.feedback/info-tooltip.png` |
| F03.feedback | message filled, email 'qa@' then cleared then qa@example.invalid; whitespace-only message | Send disabled for malformed email and whitespace message; enabled when cleared/valid → as expected | pass |  | `evidence/F03.feedback/bad-email-disabled.png` |
| F03.feedback | Send feedback in local build (no VITE_POSTHOG_SURVEY_ID) | localized error alert, draft kept, no PostHog request → role=alert 'Could not send feedback. Please try again.'; message+email kept; browser network total 0 requests | pass |  | `evidence/F03.feedback/send-error-draft-kept.png` |
| F03.feedback | Escape, Close X, backdrop click; phone 390 and 767 widths | each closes; draft survives reopen; button hidden below md → dialog count 0 after each; reopen keeps message (and the error alert); hidden at 390/767, visible at 768 | pass |  | `evidence/F03.feedback/phone-hidden.png` |
| F03.home-entry-points | / desktop | launcher with heading, toggle, composer placeholder What do you want to build? → as expected, plus new Feedback button top right | pass |  | `evidence/F03.feedback/home-button.png` |
| F08.panel-toggle | conversation page desktop, right-panel-toggle | aria-pressed true, label Hide panel, Files with workspace path → as expected (empty workspace: No files in workspace) | pass |  | `evidence/F08.panel-toggle/drawer-open-files.png` |
| F16.open | Settings gear > Application | /settings/app renders, Save Changes disabled → URL /settings/app, sections render, Save disabled, analytics switch off, 0 app errors | pass |  | `evidence/F16.open/desktop.png` |
