# software-agent-sdk map maintenance, 2026-11-21 (delta pass, TARGET main@3a893a1b)

AI-generated on behalf of Engel Nyst (@enyst) by the daily map-maintenance automation.

- **Agent-server map:** BASE main@0275e714 (62 commits). `map owners` listed 34 families, and every one was replayed live on a fresh run.
- **SDK map:** BASE main@722e5d40 (14 commits). `sdk-map owners` listed 12 families, and every one was replayed live.

This machine has no DeepSeek key, only a LiteLLM proxy serving `deepseek-v4.1-flash` (`LLM_BASE_URL`/`LLM_API_KEY`). Recipes that read `$DEEPSEEK_API_KEY` or assert the native `deepseek/...` models fail here for that reason alone. Every agent-server family with such fails (F03, F09, F21, F22, F23, F30–F34) was re-run through a local stand-in for the DeepSeek API that forwards to the proxy (`shim-*` runs). The SDK integration-runner blocks were also re-run through it.

The servers ran from main@3a893a1b, detached. Map edits were made and re-run in separate worktrees, and then re-run by an independent verifier from the map branch.

## Files

- `agent-server-report-main.md`: every attempt of the main replay of the 34 families, one row per bullet. That includes re-runs of bullets that failed on model variance (F07.error-non-json, F39.tool, F40.goal-asked).
- `agent-server-report-shim.md`: the final stand-in runs of F09, F21, F22, F23 and F30–F34.
  - Two fails: `F33.completion-logs` (the stand-in reports the proxy's model name in the completion log) and `F34.endpoint-audit` (the drift fixed in this PR).
  - `agent-server-report-shim-all-attempts.md` adds earlier stand-in attempts. Their fails are stand-in limits (`thinking` rejected by the proxy, no key check), not product results.
- `agent-server-report-edited-shards.md`: the shards' re-runs of edited bullets from their worktrees.
- `agent-server-report-verifier.md`: the independent verifier's re-run from the map branch (F18, F36, F34.endpoint-audit, F19.conversation-mcp-add-start-failure).
- `sdk-report-main.md`: the replay of the 12 SDK families.
- `sdk-report-edited-shards.md` and `sdk-report-verifier.md`: S03, S06 and S09 re-run after the edits.
- `edited/`: evidence for each changed or new bullet.
  - `F36/F36.flag-off`: with `projects` off, `GET` and `POST /api/projects` answer 404 `Projects are turned off`; switched on, the same projects are served (200) without a restart.
  - `F36/F36.runtime-env`: `OH_RUNTIME_EXPERIMENTAL_FEATURES` overrides the stored switch in both directions, and an unparsable value counts as off.
  - `F36/F36.pull-requests`: a stub `gh pr create` result becomes the `prs` tag and the board's `pull_requests`; the tag is cleared when the conversation is removed.
  - `F36/F36.judge-failed`, `F36.resolved` (reopen), `F36.artifacts-rest` (from-conversation), `F36.remove-conversation`, `F36.wake`, `F36.flag-off-tools`.
  - `F18/F18.experimental-switch`: all six features switch on, survive a restart and switch off. `F18/F18.experimental-file-changes`: an edit of `settings.json` by another process, a corruption and a restore are each seen on the next request.
  - `F34/map-run`: `F34.endpoint-audit` passes. `F19/map-run`: `F19.conversation-mcp-add-start-failure` passes.
  - `sdk/S-wt-S03-route`: `route_task_to_model` on a `RouterLLM` conversation. `sdk/S-wt-S06-prompt`: the project prompt presets. `sdk/S-wt-S09-resume`.
- `ui/`: Agent Canvas (OpenHands/OpenHands 0f4cb6a, Agent Canvas 1.43.0) against an Agent Server built from main@3a893a1b.
  - `projects-off.png`: Settings → Experimental lists the `projects` switch from #6602, off.
  - `projects-on.png`: the switch turned on; `GET /api/projects` answered 200 at once.
  - `projects-on-home.png`: Canvas main shows no Projects entry yet (that UI is OpenHands/OpenHands#19495).
  - `projects-off-again.png`: the switch turned off again; `GET /api/projects` is back to 404 `Projects are turned off`.

Bug evidence for #7054 is under `../../bugs/2026-11-21/projects-tags-while-off/`.

Scratch paths are shown as `<scratch>`. Keys are redacted by the CLIs. Before publishing, the files were scanned for the session's keys and for OpenAI, GitHub and AWS key patterns.
