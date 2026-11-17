# software-agent-sdk map maintenance, 2026-11-17 (full pass, main 2aae48b6..0275e714)

Most of both maps was affected (35 of 37 agent-server families and 20 of 21 SDK families own changed paths), so the pass replayed every family of both maps at main 0275e714, then edited the maps and re-ran every edited family independently.

- `agent-server-report-main.md`, `sdk-report-main.md`: every family of both maps replayed at 0275e714 with the map as it was on main. Every fail row is triaged in the PR description: map drift (fixed), the known race #6745, or known open bugs.
- `agent-server-report-edited.md`, `sdk-report-edited.md`: an independent full re-run of every edited family (F03, F06, F07, F09, F14, F15, F18, F19, F23, F25, F26, F34, F40; S04, S07, S09, S14, S16) plus the triage re-runs (S02, S03, S08, S11, S15, S17, S18, S21) with the edited map. All fail rows are known failures with open issues.
- `edited/agent-server/<run>/`: map-run transcripts of the edited agent-server families. `edited/sdk/<family>/`: SDK transcripts; `edited/sdk/S14-clip-fix/` shows S14's search bullet passing with a long run path after the `sdk_verify.py` clip fix.
- `main/agent-server-fails/`, `main/sdk-fails/`: transcripts of every bullet that failed in the main replay.
- `ui/`: Agent Canvas (OpenHands/OpenHands 5ed4ffa) on an agent server built from 0275e714 (see `ui/README.md`).

Scratch paths are shown as `<scratch>`. Keys are redacted by the CLIs; the files were scanned for DeepSeek and GitHub key patterns before publishing.
