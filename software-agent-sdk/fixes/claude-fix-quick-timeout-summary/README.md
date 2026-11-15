# Fix for OpenHands/software-agent-sdk#6864

Branch `claude/fix-quick-timeout-summary`, commit `0642fce` (on main `2aae48b`).

Program: `llm_failures.py` (verify-sdk `programs/S05/llm_failures.py`), run with
`control-sdk program S05/llm_failures --arg quick|exhausted` against the
skill's local fake OpenAI-compatible endpoint.

| File | What it shows |
|---|---|
| `before-main-2aae48b-quick.txt` | Stream idle exhaustion on main: hard-timeout summary naming the 30s timeout, classified `config/false/settings`. |
| `after-0642fce-quick.txt` | Same run with the fix: 3 requests, detail `LLM stream idle timeout after 0.3 seconds`, classified `transient/true/retry`. |
| `before-main-2aae48b-exhausted.txt` | Attempts reaching `timeout=1` (sync path): stops after 2 attempts, summary, `config/settings`. |
| `after-0642fce-exhausted.txt` | Unchanged with the fix: 2 attempts, summary, `config/settings`. |
