# Project role launch checks

Reviewed SDK revision `05a8f915e85e8f1617335e057405873ece833d27`. `results.jsonl` contains stdout captured from `probe.py`. Both scenarios ran in process with temporary file stores and a synthetic project.

- The ACP check saves a custom ACP profile and starts its coordinator through `ProjectService.start_coordinator`. The server adds nine native tools. The first message is saved, then running the underlying SDK conversation raises `NotImplementedError` during agent initialization, before any ACP process starts.
- The child check starts an ordinary OpenHands agent carrying the coordinator preset and a synthetic project-memory marker in its launch context. After switching Projects off, it uses `ConversationService.start_child_conversation`. The resulting child loses its project tag and project tools but retains the coordinator preset. Its rendered dynamic prompt contains the marker. The probe stubs the child's automatic run so it can inspect the launch without calling an LLM. The ACP run uses the real SDK conversation outside that stub.

To rerun, use a configured SDK checkout at the revision above. Set `probe` to the location of the downloaded `probe.py` and run the command from the SDK repository root.

```sh
LITELLM_LOCAL_MODEL_COST_MAP=True OPENHANDS_SUPPRESS_BANNER=1 \
  PYTHONPATH=.:openhands-sdk:openhands-agent-server:openhands-tools:openhands-workspace \
  uv run --no-sync python "$probe"
```
