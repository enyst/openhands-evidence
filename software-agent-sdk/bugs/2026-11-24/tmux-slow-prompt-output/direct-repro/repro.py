"""Minimal repro: TerminalExecutor on tmux, slow PROMPT_COMMAND, no heredoc, no agent.

Usage: python repro.py <terminal_type> <sleep> [n_echo]
"""
import json, sys, tempfile
import openhands.tools.terminal.terminal.tmux_terminal as tt
from openhands.tools.terminal import TerminalAction
from openhands.tools.terminal.impl import TerminalExecutor

mode, delay = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
ex = TerminalExecutor(working_dir=tempfile.mkdtemp(), terminal_type=mode)
res = {"module": tt.__file__, "mode": mode, "sleep": delay, "steps": []}
def run(cmd):
    obs = ex(TerminalAction(command=cmd))
    text = obs.text
    res["steps"].append({"cmd": cmd, "exit": obs.exit_code, "text": text.split("\n[The command")[0]})
    return text
run(f'PROMPT_COMMAND="$PROMPT_COMMAND; sleep {delay}"')
lost = 0
for i in range(n):
    t = run(f"echo out-{i}")
    if f"out-{i}" not in t.split("\n[The command")[0]:
        lost += 1
res["lost"] = lost; res["total"] = n
ex.close()
print(json.dumps(res, indent=1))
