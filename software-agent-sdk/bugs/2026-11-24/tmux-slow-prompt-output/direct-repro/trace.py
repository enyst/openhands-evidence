"""Trace screen state around clear_screen with slow PROMPT_COMMAND (tmux)."""
import sys, tempfile, time
from openhands.tools.terminal import TerminalAction
from openhands.tools.terminal.terminal import create_terminal_session
s = create_terminal_session(work_dir=tempfile.mkdtemp(), terminal_type="tmux")
s.initialize()
print(s.execute(TerminalAction(command='PROMPT_COMMAND="$PROMPT_COMMAND; sleep 0.3"')).text)
scr = s.terminal.read_screen()
print("SCREEN right after clear_screen returned:", repr(scr))
obs = s.execute(TerminalAction(command="echo out-0"))
print("OBS:", repr(obs.text))
time.sleep(1)
print("SCREEN 1s later:", repr(s.terminal.read_screen()))
s.close()
