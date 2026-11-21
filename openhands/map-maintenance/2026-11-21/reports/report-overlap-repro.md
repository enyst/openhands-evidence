# Verification ledger — run 2026-11-21T1256-684149

Revision `0f4cb6af95915fee776913c4aa8694e7c4b76033`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 2 — pass 1, fail 1, blocked 0, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F23 | 1 | 1 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F23.run-status-polling | /automations/<id> Runs list at 390x844 (also 360, 430), FAILED run with cost $0.0000 + phase 'Agent is working on the task' | time and summary readable, no text drawn over other text → left column (time+summary) width 0; '12:56 PM' wraps to 2 lines (40.1x40) and 'PM' is drawn over run-cost '$0.0000' (cost x=41..90.8, y=773..789 vs time x=41..81.1, y=751..791); summary invisible; 2 runs, 3 widths; desktop 1440 OK | fail | candidate defect; flex-1 basis 0 left col vs content-sized right col | `evidence/F23.phone/overlap.png` |
| F23.run-status-polling | same rows at 1440x1000 | no overlap → left 490.9px, time 1 line, no overlap | pass |  | `evidence/F23.desktop/runs-1440.png` |
