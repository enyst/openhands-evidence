# software-agent-sdk map maintenance, 2026-11-20 (delta pass, TARGET main@722e5d40)

AI-generated on behalf of Engel Nyst (@enyst) by the daily map-maintenance automation.

- Agent-server map: BASE main@0275e714 (48 commits). `map owners` listed 30 families, and every one was replayed live on a fresh run.
- SDK map: BASE main@14142392 (19 commits). `sdk-map owners` listed 17 families, and every one was replayed live.

This machine had no DeepSeek key, only a LiteLLM proxy serving `deepseek-v4.1-flash` (`LLM_BASE_URL`/`LLM_API_KEY`). Recipes that read `$DEEPSEEK_API_KEY` or assert the native `deepseek/deepseek-flash` model fail here for that reason alone. The previous pass saw the same fails, for the same reason: F03.init-child-launcher, F09, F21, F23, F30, F31, F32, F33, F34, and the SDK integration-runner blocks. F30–F34 were also driven through a local stand-in for the DeepSeek API that forwards to the proxy (`shim-*` runs).

The servers ran from the checkout on the work branch. Its commits after 722e5d40 touch only `.agents/skills/verify-*` map files and one verify-sdk program, so the product code is TARGET's. The report's "Checkout" column shows those work-branch SHAs. That is also why three F01 bullets failed the first time: they compare `build_git_sha` with HEAD, and HEAD moved mid-run. All three pass on the re-run.

## Files

- `agent-server-report-main.md`: one row per replayed bullet, including re-runs and failed first attempts.
- `agent-server-report-shim.md`: the stand-in runs.
- `agent-server-report-edited.md`: the F19 edit, re-run twice by the shard and once in full by an independent verifier.
- `map-run/A1..A4/`: the JSON output of every `control-agent-server map run` (`*.doctorfail*`/`*try*` are first attempts that failed `doctor`'s `openapi` ReadTimeout under load and ran no recipe).
- `sdk-report-main.md`: the replay of the 17 families.
- `sdk-report-edited.md`: the independent re-run of the edited families (S01, S02, S09, S13, S15, S21) plus the shards' post-edit runs.
- `sdk-runs/<run>/`: ledgers and the transcript of every non-pass bullet.
- `edited/`: the evidence for each changed bullet:
  - `F19/F19.conversation-mcp-add-restart/`: tool `qa-f19-rs_qa_echo` answers `QA_MCP_ECHO:two` after a restart.
  - `sdk/B2-S09-resume/`: S09.runtime-add-resume passes.
  - `sdk/B3-S15-tabs-after/`: S15.tabs passes.
  - `sdk/B3-S21-ask/`: S21.ask-agent passes.
  - `sdk/V-S01-so/`: S01.structured-output passes.
  - `sdk/final-S13/`: the new S13 rotated-secret bullet fails as its #7002 note says.
- `repro/6934/`: a live-only session socket closes with 1013 `frame_too_large` when a 5 MiB event is appended. `live-big.json` holds the frames; `after3.json` shows a reconnect past the event resumes.
- `repro/7002-server/`: agent-server repro of #7002, with a stub LLM and test values.
  - Before rotation, `OLD=<secret-hidden>`.
  - After `POST /secrets`, the new value prints in cleartext (`NEW=qa-rotnew-sekret`).
  - After it is exported, the old one does too (`OLD2=qa-rotold-sekret`).
- `ui/`: Agent Canvas (OpenHands/OpenHands 428b3dc, Agent Canvas 1.42.0) against an Agent Server built from this checkout.
  - `factories.png`: Settings → Experimental now lists the `factories` flag from #7016, off by default.
  - `factories-on.png`: the flag switched on and still on after a reload; the sidebar shows no Factories entry (Canvas main has no code for it yet: OpenHands/OpenHands#19800).
  - `factories-off.png`: the flag restored to off.

Scratch paths are shown as `<scratch>`. Keys are redacted by the CLIs. Before publishing, the files were scanned for the session's keys and for OpenAI, GitHub and AWS key patterns.
