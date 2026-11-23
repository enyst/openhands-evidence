# Verification ledger — run 2026-11-23T0944-2f9125

Revision `c5e47c4b4dab1d14724e74675c06254957ccbf47`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 2 — pass 0, fail 2, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F06 | 0 | 2 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F06.hook-events | Conversation with .openhands/hooks.json user_prompt_submit hooks; expand the three Hook: UserPromptSubmit rows | Hook detail labels (Command:, Exit code:, Error:, Blocked reason:, Output:, Stderr:) readable (>=4.5:1) in every theme → All 10 label spans are text-text-subtle: rgb(86,86,86) on rgb(24,24,24) = 2.42:1 on OpenHands-Neutral (default) and OpenHands-Neo; 3.71:1 on DeepSea. Light+ 6.19, Solarized Light 5.27, Paper 5.99 pass. | fail | Product defect. src/components/shared/hook-execution-event-message.tsx lines 75,83,90-91,99,106,113,122 use className="text-text-subtle" (--oh-text-subtle = cool-grey-600). Not a regression in 6fa7686d..c5e47c4b: the component and src/themes are byte-identical between BASE and TARGET. LLM: litellm_proxy/deepseek-v4-flash via eval proxy (llm set, not llm preset deepseek). | `evidence/F06.hook-events/labels-neutral-desktop.png` `evidence/F06.hook-events/labels-deepsea-desktop.png` `evidence/F06.hook-events/labels-neo-desktop.png` `evidence/F06.hook-events/labels-lightplus-desktop.png` `evidence/F06.hook-events/labels-solarized-desktop.png` `evidence/F06.hook-events/labels-paper-desktop.png` |
| F06.phone | Open /conversations/<id> with a reply long enough to scroll at desktop (1440x1000), then browser viewport phone (390x844) | The transcript stays pinned to the bottom across the resize: chat-scroll-container scrollHeight - scrollTop - clientHeight = 0, as a fresh load at either size gives → Desktop fresh load 0 px. After viewport phone: scrollTop stays 1074 while clientHeight 814->650 and scrollHeight 1888->1912, leaving 188 px below the fold (list items 56-60 cut off). Fresh load at phone is 0; phone->desktop is 0 (the browser clamps scrollTop to the smaller maximum, which happens to be the bottom). | fail | Product defect, shrinking direction only. No ResizeObserver/resize listener re-pins the chat scroll container: src/components/features/chat/chat-interface.tsx autoscroll effect (line ~647) only runs on renderableEvents.length / hasPendingUserMessages / activeGoalScrollKey, and src/hooks/use-scroll-to-bottom.ts follows content only while followContent (isRevealingStreamedText) is true. NOT caused by #17820 (f6cf44d): the list is plain here (VIRTUALIZATION_THRESHOLD=150 rows, this conversation has 3) and an identical repro on a worktree at f6cf44d^ (5919b0f) gave the same 188 px. LLM: litellm_proxy/deepseek-v4-flash via eval proxy. | `evidence/F06.phone/resize-desktop-to-phone-gap.png` `evidence/F06.phone/fresh-load-phone-at-bottom.png` `evidence/F06.phone/resize-phone-to-desktop.png` |
