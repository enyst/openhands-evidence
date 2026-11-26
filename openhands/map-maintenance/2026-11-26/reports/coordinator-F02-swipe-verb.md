# Verification ledger — run 2026-11-26T0906-a28259

Revision `6deb332c3602329306180fd7a99b3534753909df`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18820.

Checks: 3 — pass 3, fail 0, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F02 | 3 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F02.mobile-drawer | Conversation page, 390x844, browser swipe on conversation-chat-panel | swipe from 24..130px (left third) right >=56px opens the drawer, URL unchanged → starts at 24, 48, 130 opened sidebar-mobile-drawer; URL unchanged | pass |  | `evidence/F02.mobile-drawer/swipe-open.png` |
| F02.mobile-drawer | Conversation page, 390x844, browser swipe | outer 24px, past left third, vertical, short and on chat-input swipes do nothing → starts 10, 23, 150, vertical 48->54,182, short 48->88, on chat-input y=726: drawer count 0 | pass |  | `evidence/F02.mobile-drawer/swipe-rejected-closed.png` |
| F02.mobile-drawer | Conversation page, desktop viewport, browser swipe | no drawer at desktop → drawer count 0, URL unchanged | pass | proves new browser swipe verb (CDP Input.dispatchTouchEvent) | `evidence/F02.mobile-drawer/swipe-desktop-no-effect.png` |
