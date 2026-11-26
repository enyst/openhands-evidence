# Map maintenance pass, 2026-11-26 (AI-generated on behalf of Engel Nyst)

Daily delta pass of the verify-agent-server and verify-sdk feature maps of
OpenHands/software-agent-sdk, BASE main@0988e976 .. TARGET main@d7263334 (28 commits).
Machine: Linux, tmux, git, node, uvx, Chromium; no Docker; no direct DeepSeek key (model-backed
recipes went through a LiteLLM proxy, so recipes that need `deepseek/deepseek-flash` literally or
`$DEEPSEEK_API_KEY` fail for that environment reason).

- `agent-server-report.md`: `control-agent-server evidence report` over every recorded run of the
  pass (F01, F04-F15, F31-F34, F40 and the re-checks). Rows count each feature's latest attempt.
- `sdk-report.md`: `sdk-map report` over every SDK run (S01-S07, S14, S18, S20 and re-checks).
- `<feature ID>/target`, `<feature ID>/base`: saved exchanges / program output of each changed
  bullet on TARGET (independent re-run) and on BASE (where the bullet is expected to fail).
- `F01.idle-time-active-run/idle-*.log`: manual `/server_info` sampling during a hung run, TARGET vs BASE.
- `sdk-transcripts/`: `sdk-map run` transcripts of the changed SDK bullets (`-target`, `-base`).
- `ui/`: Agent Canvas (OpenHands/OpenHands main@6deb332) on this Agent Server checkout, conversation
  list with two unreadable conversations (#7080): broken rows, delete confirm, after delete.
- `triage/<issue>/`: reproductions of the open `bug` issues filed since BASE (#7099-#7130).
