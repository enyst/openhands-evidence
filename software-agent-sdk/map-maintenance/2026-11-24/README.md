# Daily feature-map pass, 2026-11-24

AI-generated on behalf of Engel Nyst (@enyst) by the daily map-maintenance automation for OpenHands/software-agent-sdk.

- Source: OpenHands/software-agent-sdk main@0988e976491ff733bc09e976b36a271b0c511530 (TARGET); both maps' BASE main@74f198df3650da6399c6a0a2dff6272a667bbace.
- Machine: Linux container, tmux/git/node/uvx available, no Docker, no `DEEPSEEK_API_KEY` (model-backed recipes ran through a LiteLLM proxy key; recipes that call DeepSeek directly fail for that reason and are environment failures, not product results).
- `agent-server-report.md`: `control-agent-server evidence report` over every agent-server run of the pass (F09, F18, F23, F31, F34, F36).
- `sdk-report.md`: `sdk-map report` over every SDK run of the pass (S01, S02, S03, S06, S07, S12, S13, S14, S19, S20, S21).
- `F09.acp-teardown-and-resume/`, `F23.acp-discovery-antigravity/`, `F36.coordinator-active-llm/`, `F31.search-unreadable-record/`: saved exchanges and ledgers of the changed agent-server bullets (F31 is a known bug, #7079: `map-run-xfail/` is the recipe's xfail, `manual-repro/` the hand-driven repro).
- `sdk-transcripts/`: transcripts of the changed SDK bullets (S01.message-continues-turn, S06.project-prompt-edits known failure, S14.terminal-input-encoding subprocess heredoc, S19/S21 ACP provider, resume and cleanup bullets).
- `ui/`: Agent Canvas (OpenHands/OpenHands main 7a9425ac) driven against this Agent Server checkout: a project with a coordinator created from the UI (#7056), and the ACP preset list / an `antigravity` profile in Settings → Agent (#6633).
- `independent-rerun/`: a second agent re-ran every edited bullet on fresh runs at the map commit: all expected results (passes, xfail for #7079, the documented known failures #7093 and #7094 on S06 and the S14 tmux bullet).
