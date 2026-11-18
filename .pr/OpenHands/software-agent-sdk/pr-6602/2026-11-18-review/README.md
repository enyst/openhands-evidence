# Projects review evidence for SDK PR #6602

Reviewed on November 18, 2026, at `05a8f915e85e8f1617335e057405873ece833d27` against `f765648dd56dc01c4302b6de669ab067f5bd6ae9`. All observed results below are from that SDK head. [Pull request](https://github.com/OpenHands/software-agent-sdk/pull/6602) · [Reviewed source](https://github.com/OpenHands/software-agent-sdk/tree/05a8f915e85e8f1617335e057405873ece833d27)

## Observations

| Path exercised | Observed result |
|---|---|
| Runtime selection | An in-process request to create a coordinator explicitly selected Docker on a server configured for local conversations. The API accepted the request and the host conversation service returned a live local conversation. The coordinator stayed idle. See the captured output below. |
| Generic tags, deletion, and rollback | With Projects disabled, a tagged conversation start returned 422 and its untagged control returned 201. After project deletion the surviving coordinator’s child start returned 409. A PATCH with a concurrent coordinator deletion returned 404 and a subsequent GET showed the new worker profile had persisted. [Probe](data/project_data_probe.py) · [Observed HTTP results](data/observed.txt) |
| Stale question and abandoned reply | A coordinator card saved its database answer against a later color question. After navigation restored an earlier worker branch, reconciliation delivered the abandoned reply to the coordinator. The replay check invokes the real startup reconciler in process with a deliberately missed live delivery. [Method and checks](runtime/README.md) · [Captured results](runtime/results.txt) |
| ACP and the child copied after Projects was disabled | The first SDK run of the ACP coordinator failed during native-tool validation. The copied child retained the coordinator preset and rendered the synthetic project memory marker after its project tag and project tools were removed. [Launch probe](client/probe.py) · [Captured results](client/results.jsonl) |

For the data probe, set `EVIDENCE_DIR` to this evidence directory and run the following from the reviewed SDK checkout with its development dependencies installed.

```sh
PYTHONPATH=.:openhands-sdk:openhands-tools:openhands-agent-server:openhands-workspace \
  uv run --frozen python "$EVIDENCE_DIR/data/project_data_probe.py"
```

### Runtime selection

The local FastAPI Projects router used a real `ConversationService`, temporary file stores, and a saved synthetic agent profile. Its server configuration selected `local`. The coordinator creation request specified `conversation_runtime="docker"`. After the HTTP response, the probe looked up the returned coordinator through that same host service and inspected the conversation and workspace classes. This exercised runtime selection through the API without starting Docker or running a model. [Coordinator launch](https://github.com/OpenHands/software-agent-sdk/blob/05a8f915e85e8f1617335e057405873ece833d27/openhands-agent-server/openhands/agent_server/project_service.py#L505-L528)

```text
HTTP status 201
coordinator implementation LocalConversation
workspace implementation LocalWorkspace
```

## Focused suite

Six existing test modules ran on macOS using the reviewed source and an existing Python 3.13 development environment. The initial invocation aborted during macOS display discovery in the browser dependency. The completed run disabled that discovery and used LiteLLM’s local cost map. These are the test arguments for the completed run from the SDK checkout.

```sh
LITELLM_LOCAL_MODEL_COST_MAP=True OPENHANDS_SUPPRESS_BANNER=1 \
  uv run --frozen python -c 'import sys; sys.modules["AppKit"] = None; import pytest; raise SystemExit(pytest.main(sys.argv[1:]))' \
  -o addopts= -q \
  tests/agent_server/test_project_cards.py \
  tests/agent_server/test_conversation_tags.py \
  tests/agent_server/test_projects_feature_flag.py \
  tests/agent_server/test_project_board.py \
  tests/agent_server/test_project_profiles.py \
  tests/sdk/context/prompts/test_project_registry.py
```

```text
103 passed, 37 warnings in 8.01s
```

The TypeScript finding compares the public client declarations with the response built by the Agent Server. The Windows artifact finding comes from the regular-file handling and Python’s Windows platform contract. Windows execution and a deployed Docker or Cloud environment were outside the local verification. [Client contract](https://github.com/OpenHands/software-agent-sdk/blob/05a8f915e85e8f1617335e057405873ece833d27/clients/typescript/src/client/projects-client.ts#L37-L58) · [Server response](https://github.com/OpenHands/software-agent-sdk/blob/05a8f915e85e8f1617335e057405873ece833d27/openhands-agent-server/openhands/agent_server/projects_router.py#L489-L517) · [Artifact reader](https://github.com/OpenHands/software-agent-sdk/blob/05a8f915e85e8f1617335e057405873ece833d27/openhands-agent-server/openhands/agent_server/project_artifacts.py#L242-L257) · [Python documentation](https://docs.python.org/3.13/library/os.html#os.set_blocking)

Prepared by SmolPaws, an AI agent, on behalf of Engel Nyst.
