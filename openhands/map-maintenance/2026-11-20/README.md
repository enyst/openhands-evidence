# Map maintenance 2026-11-20 (delta pass, OpenHands/OpenHands)

BASE main@6fa7686d37781d8172798231b07b968b9216214a .. TARGET main@428b3dc2a0e8d3d0f689a909e2607e33d973da76.
Verdict: partial (model-backed checks blocked: DEEPSEEK_API_KEY unset in the session). Baseline not moved.

All runs used `control-openhands launch --new --sdk-version 1.63.1`: the pinned Agent Server 1.63.0
does not start on a fresh install since litellm 1.109.3 (2026-11-20 03:58 UTC) removed
`litellm.llms.openai.chat.gpt_5_transformation` (OpenHands/software-agent-sdk#7014, fixed in 1.63.1).

Reports:
- report-settings-experimental.md: F09, F30, F05 slash count (coordinator run)
- report-automations.md: F21, F22, F23, F28 (worker run)
- report-chat-misc.md: F01 F02 F05 F06 F07 F08 F10 F12 F14 F18 F25 F26 F29 credential-free (worker run)
- report-reverify-F09.md: independent re-run of the F09 edit
- report-reverify-F28-F22-F02-F05.md: independent re-run of the F28/F22/F02/F05 edits
