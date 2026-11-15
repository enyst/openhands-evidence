# Quick timeouts that run out of retries get the hard-timeout summary (software-agent-sdk, regression from #6822)

- `target-2aae48b.txt`: `control-sdk program S05/llm_failures --arg quick` on main 2aae48b6. A streamed LLM with `stream_idle_timeout=0.3`, `timeout=30`, `num_retries=3` against a local endpoint that stalls every stream: 3 requests, final `LLMTimeoutError` text says "within the LLM timeout of 30s ... or a higher timeout in the LLM settings"; classified `config` / not retryable / `settings`.
- `before-6822-10c38cf.txt`: the same program on 10c38cf (the commit before #6822): 3 requests, text `LLM stream idle timeout after 0.3 seconds`, classified `transient` / retryable / `retry`.
- `sdk-map-S05-quick-timeouts-transcript.log`: the verify-sdk map bullet (S05, "A run of quick timeouts") failing on main on the three classification checks.
- `llm_failures.py`: the program (verify-sdk `programs/S05/llm_failures.py`).
