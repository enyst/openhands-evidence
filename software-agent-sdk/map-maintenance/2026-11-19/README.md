# software-agent-sdk map maintenance, 2026-11-19 (delta pass, main 0275e714..14142392)

Both maps' owners listed most families (29 of 38 agent-server, 18 of 21 SDK), so every listed family was replayed live at main 14142392, the maps were edited, and every edited family was replayed again in full.

This machine had no DeepSeek key, only a LiteLLM proxy serving `deepseek-v4.1-flash` (`LLM_BASE_URL`/`LLM_API_KEY`). `control-agent-server llm preset deepseek` already uses it; this pass taught `control-sdk` to as well. Recipes that read `$DEEPSEEK_API_KEY` or assert the native `deepseek/deepseek-flash` model fail here for that reason only (F09, F21, F23, F30, F31, F32, F33, F34 and the SDK integration-runner blocks); each such fail was classified in triage and, where possible, the same family was driven through a local stand-in for the DeepSeek API (`shim-*` runs).

- `agent-server-report-main.md`, `sdk-report-main.md`: the replay of every listed family at 14142392 with the map as it was on main.
- `agent-server-report-edited.md`, `sdk-report-edited.md`: full replays of every edited family with the edited maps (F04, F06, F09, F19, F21, F27, F30; S03, S04, S06, S09, S10, S11, S14, S19), plus the F09 model-router run and the shim runs that drove F03, F33 and F34 past the key gap. Every fail row there is a known failure with an issue, or the missing DeepSeek key.
- `main/agent-server-fails/<run>/`, `main/sdk-fails/<family>/`: transcripts of every bullet that failed in the main replay.
- `edited/agent-server/<run>/`, `edited/sdk/<family>/`: transcripts and ledgers of the edited-family replays.
- `ui/`: Agent Canvas (OpenHands/OpenHands e1b8b60) on an agent server built from this checkout: `dialog.png` is ⋮ → Edit tags with `qaenv: one` added (`F04.edit-tags`), `saved.png` the conversation row after Save and a reload, showing the chips `Qaenv: one` and `Qaseed: x` that `GET /api/conversations/search` also returns.

Scratch paths are shown as `<scratch>`/`<tmp>`. Keys are redacted by the CLIs; the files were scanned for the session's keys and for OpenAI/GitHub key patterns before publishing.
