# Projects: a coordinator update saved just before a restart is never run

AI-generated on behalf of Engel Nyst (@enyst) by the daily map-maintenance automation.

The server is OpenHands/software-agent-sdk at main@3a893a1b, plus map-only commits (branch cloud/nifty-ride-xjugwj at 1a9ecad). It was launched with `control-agent-server launch --new`, with `projects` on and the deepseek preset going through a LiteLLM proxy. An independent agent ran `restart-wake.sh` twice (attempts a and b) under a subreaper. Scratch paths are shown as `<scratch>`.

Steps:
1. A project starts a coordinator.
2. The coordinator starts a member with the task "Reply with the single word ok and finish".
3. The member finishes, and the server saves an `[Update from ...]` message in the coordinator and starts its run.
4. `control-agent-server restart` runs at once, a graceful restart.
5. After the restart the coordinator is `paused`. It is still `paused` two minutes later, with no agent event after the update.

- `restart-wake.sh`: the script.
- `rw-b.out`: attempt b's output. The update was saved at 15:45:47.18, and the shutdown's `PauseEvent` and `InterruptEvent` followed at 15:45:47.86. After that the coordinator does nothing.
- `attempt-{a,b}/*-cat-after-restart.json` and `*-cat-after-2min.json`: the coordinator's `execution_status` is `paused` both times.
- `attempt-{a,b}/*-cat-events-after-2min.json`: the coordinator's last events. The update is followed only by state updates, `PauseEvent` and `InterruptEvent`.
- `attempt-{a,b}/*-child.json`: the member. In attempt b it is `finished`, `resolved=auto`.
