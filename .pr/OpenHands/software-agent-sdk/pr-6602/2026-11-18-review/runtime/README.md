# Offline checks for project card forwarding and restart recovery

Reviewed revision `05a8f915e85e8f1617335e057405873ece833d27` of `OpenHands/software-agent-sdk`. A passing test means the reviewed revision exhibited the reported behavior. [Selected output from the run](results.txt).

## Run from the SDK checkout

Use that revision with its Python development dependencies installed. Place the accompanying script at `runtime/test_runtime.py` relative to the checkout root, then run the following command there.

```sh
PYTHONPATH=.:openhands-agent-server:openhands-sdk:openhands-workspace:openhands-tools \
  .venv/bin/python runtime/test_runtime.py
```

The command works offline and needs no credentials. The script enables Projects using the PR's test fixture. It uses a temporary workspace and persistence store, disables automatic model-generated titles and ambient plugin discovery, and uses LiteLLM's bundled model-cost map. On macOS it disables the browser dependency's unrelated screen probe for this process.

## What the checks exercise

- **Stale coordinator card.** A worker asks which database to use. Its coordinator presents a corresponding card. The user answers in the worker and the worker then asks which color to use. The test records a “Postgres” click on the original coordinator card, drains the real board subscriber and reads the worker's saved answer event. It checks the event ID against both worker questions.
- **Abandoned reply during recovery.** The test records a user task, a later coordinator task and an agent reply. It marks the worker finished and suppresses live delivery to model a missed update. The real navigation service moves the worker's active head back to the user's task. The test verifies that the reply lies outside the active branch, invokes the startup reconciliation function and reads the resulting message from the coordinator's saved event history.

Both checks use the PR's in-process service fixtures and synthetic events. The save-only fixture persists delivered messages and suppresses agent execution. The recovery check invokes the reconciler directly in the same process. The checks establish the saved event and its destination. Model behavior, process shutdown and process startup are outside their coverage.
