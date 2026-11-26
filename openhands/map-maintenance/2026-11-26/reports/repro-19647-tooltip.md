# Verification ledger — run 2026-11-26T0911-3dd82e

Revision `6deb332c3602329306180fd7a99b3534753909df`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18800.

Checks: 2 — pass 0, fail 2, blocked 0, not-run 0, xfail 0, xpass 0. Families: 2.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F02 | 0 | 1 | 0 | 0 | 0 | 0 |
| F03 | 0 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F02.checklist | Home sidebar > Getting started > hover 'Schedule a task' (preview tooltip) | preview text wraps between words → word-break: break-all on [role=tooltip]; 'Create' split 'Cr/eate', 'work' split 'wor/k' | fail | same @heroui/styles tooltip.css break-all as F03.feedback info tooltip | `evidence/F02.checklist/tooltip-word-split.png` |
| F03.feedback | Home > Feedback button > info icon next to dialog title (hover) | 320px tooltip wraps between words → word-break: break-all (from @heroui/styles tooltip.css); 'analytics' split as 'anal/ytics' | fail | getComputedStyle wordBreak=break-all overflowWrap=normal maxWidth=320px | `evidence/F03.feedback/tooltip-word-split.png` |
