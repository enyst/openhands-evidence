# Project worker prompt: stale substitution logs a warning on every SDK import

AI-generated on behalf of Engel Nyst (@enyst). Source: OpenHands/software-agent-sdk main@0988e976 (regression from #7068, commit ebec01b; BASE 74f198df and ebec01b^ log nothing).

- `main-0988e97-prompt_warnings.json`: `control-sdk program S06/prompt_warnings` on main: one `Default prompt text changed` warning.
- `fix-branch-prompt_warnings.json`: the same program against the fix branch: none.
- `independent-repro.txt`, `tb-*.txt`, `count_warn.py`: an independent agent's reproduction on TARGET, BASE and ebec01b^, and the worker `<TROUBLESHOOTING>` blocks.
