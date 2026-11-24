# tmux terminal: output lost after a slow prompt hook

AI-generated on behalf of Engel Nyst (@enyst). Source: OpenHands/software-agent-sdk main@0988e976; also reproduced on 74f198df (not a regression from that range).

- `main-0988e97-terminal_heredoc-tmux-{1,2}.json`: `control-sdk program S14/terminal_heredoc --arg tmux` on main: `third` returns only "[Previous command outputs are truncated ...]".
- `base-74f198d-terminal_heredoc-tmux-1.json`: the same failure at BASE.
- `fix-branch-terminal_heredoc-tmux-{1,2}.json`: every check passes against the fix branch.
- `direct-repro/`: `repro.py` drives the terminal executor directly (no agent loop, no heredoc) at prompt delays 0, 0.1, 0.3 and 1.0 s on tmux and subprocess (`out_*.json` on main, `fix_tmux_*.json` on the fix); `trace.py`/`trace.out` show the blank pane right after `clear`.
- `fix-branch-terminal-suite.log`: `tests/tools/terminal` on the fix branch (486 passed, 39 skipped).
