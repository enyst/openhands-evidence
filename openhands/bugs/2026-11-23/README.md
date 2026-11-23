# OpenHands bug evidence, 2026-11-23

AI-generated on behalf of Engel Nyst by the daily verify-openhands routine. Source: OpenHands/OpenHands main c5e47c4b, Agent Server 1.63.1, driven with control-openhands; each defect was reproduced by two independent agents on separate stacks.

- `hook-label-contrast/`: hook event detail labels (`Command:`, `Exit code:`, `Error:`, `Blocked reason:`, `Output:`, `Stderr:`) at 2.42:1 on OpenHands-Neutral (the default) and 3.71:1 on DeepSea; Light+ for comparison (6.19:1).
- `transcript-resize-bottom/`: a finished conversation that is at the bottom on desktop stops 188 px above the bottom after the viewport shrinks to 390x844 (`resize-desktop-to-phone-gap.png`); a fresh load at phone size is at the bottom (`fresh-load-phone-at-bottom.png`); the same gap before #17820 (`pre17820-resize-desktop-to-phone.png`, main 5919b0f, Agent Server 1.62.0).
