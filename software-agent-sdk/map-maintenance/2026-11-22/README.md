# Map maintenance 2026-11-22 (daily delta pass)

Both maps: BASE main@3a893a1b → TARGET main@74f198df (4 commits: #7059, #6978, #7044, #7043).
No `DEEPSEEK_API_KEY` on this machine: model-backed recipes were not run (blocked).

## Files

- `agent-server-report.md`: `control-agent-server evidence report` over the F23, F32 and F36 runs.
  Every F23 and F32 fail comes from the missing DeepSeek key: F32's Preconditions
  (`llm preset deepseek`) and F23's first connection create fail, and the later
  bullets cascade from that. No product defect is behind them.
- `sdk-report.md`: `sdk-map report` over the S14 runs. The S14 fails are the documented
  known failures #6652, #6653, #6991 and #6972, plus the new `S14.glob` recipe for #7052.
  The "conflicting attempts" row for `S14.glob` is the first full replay, which ran
  before the #7052 recipe was added.
- `F36.coordinator-active-llm/`: the new known-bug recipe for #7061.
  - `main-74f198d-transcript.txt` and `main-74f198d-post-projects.json`: on TARGET, `POST /api/projects`
    answers 422 `LLM profile 'default' not found`, and `project-coordinator` keeps `llm_profile_ref: default`.
  - `pr7056-08af087-transcript.txt`: the same recipe on fix PR #7056 passes (201, coordinator on `qa-f36-stub`).
- `S14.glob/`: the new recipe for #7052.
  - `main-74f198d-glob-dir.log`: with ripgrep, `pkg/*.py` under `path` `{ws}/src` finds nothing (`files.0` null),
    while the Python fallback finds `src/pkg/new.py`.
  - `pr7053-9762a24-glob-dir.log`: the same recipe on fix PR #7053 passes.
  - `repro-7052.py`: a direct `GlobExecutor` repro (run from the repo root, outside the search path).
- `S14.terminal-input-encoding/main-74f198d-tmux-pane-pool.log`: the tmux pane-pool bullet with
  the new checks that no `__OH_COMMAND_FINISHED_` marker shows after the 400-line heredoc (from #6978's
  `terminal_session.py` change). Pass.
