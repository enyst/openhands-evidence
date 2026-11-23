# Fix: hook event detail labels contrast (OpenHands/OpenHands#20003)

AI-generated evidence (Claude Code) on behalf of Engel Nyst.

- Source commit: OpenHands/OpenHands `8feda4a8c1131f5b8f8191e167beff2eeca96a28` (branch `claude/fix-hook-label-contrast`, base main `c5e47c4`)
- Agent Server 1.63.1, model litellm_proxy/deepseek-v4-flash

## Steps

Stack launched from the fix worktree with `control-openhands launch --new`, then the
hook fixture recipe from the issue (`qa-hooks` workspace with three `user_prompt_submit`
hooks: stderr / timeout / deny). Opened the conversation, expanded the event group and
the three hook rows, switched the theme in Settings -> Application, and measured each
label's computed color against its nearest opaque background (WCAG relative luminance).

## Results (after fix)

| Theme | Label color on background | Ratio (before) |
|---|---|---|
| OpenHands-Neutral | rgb(151,151,151) on rgb(24,24,24) | 6.08 (2.42) |
| OpenHands-Neo | rgb(151,151,151) on rgb(24,24,24) | 6.08 (2.42) |
| OpenHands-DeepSea | rgb(163,176,196) on rgb(11,14,20) | 8.80 (3.71) |
| Light+ | rgb(89,89,89) on rgb(255,255,255) | 7.00 (6.19) |
| Solarized Light | rgb(76,96,102) on rgb(253,246,227) | 6.14 (5.27) |
| Paper | rgb(97,84,72) on rgb(243,231,211) | 5.99 (5.99) |

Screenshots: `after-labels-neutral-desktop.png`, `after-labels-deepsea-desktop.png`,
`after-labels-lightplus-desktop.png`.
