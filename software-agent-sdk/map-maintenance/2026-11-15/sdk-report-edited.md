## Conflicting attempts

- S02.error-mapping: fail at 2026-11-15T09:34:33+00:00, pass at 2026-11-15T09:44:18+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S02.metrics | fail | a11a17b3df61 | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 22: pass; bullet 23: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | a11a17b3df61 | bullet 12: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-12.log |
| S02.responses-reasoning | fail | a11a17b3df61 | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | a11a17b3df61 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 23: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-04.log |
| S04.interactive-terminal | fail | a11a17b3df61 | bullet 23: fail (block 1 exited 1); bullet 29: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-23.log |
| S04.pause-during-startup | fail | a11a17b3df61 | bullet 12: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-12.log |
| S05.error-classification | fail | a11a17b3df61 | bullet 2: pass; bullet 3: pass; bullet 4: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-04.log |
| S05.token-event | blocked | a11a17b3df61 | bullet 11: blocked (bullet is labeled blocked) |  |
| S01.ask-agent | pass | 2aae48b67a57 | bullet 18: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-18.log |
| S01.async-step | pass | 2aae48b67a57 | bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-16.log |
| S01.content-policy | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-03.log |
| S01.context-overflow | pass | 2aae48b67a57 | bullet 20: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-20.log |
| S01.empty-reply-nudge | pass | 2aae48b67a57 | bullet 4: pass; bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-04.log |
| S01.finish-truncates-batch | pass | 2aae48b67a57 | bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-12.log |
| S01.image-input | pass | 2aae48b67a57 | bullet 17: pass; bullet 25: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-17.log |
| S01.image-non-vision | pass | 2aae48b67a57 | bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-17.log |
| S01.iterative-refinement | pass | 2aae48b67a57 | bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-23.log |
| S01.malformed-tool-call | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-07.log |
| S01.max-iterations | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-06.log |
| S01.message-while-running | pass | 2aae48b67a57 | bullet 15: pass; bullet 16: pass; bullet 22: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-15.log |
| S01.parallel-resource-locks | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-13.log |
| S01.parallel-tools | pass | 2aae48b67a57 | bullet 12: pass; bullet 22: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-12.log |
| S01.response-dispatch | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-01.log |
| S01.run-to-finish | pass | 2aae48b67a57 | bullet 1: pass; bullet 21: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | 2aae48b67a57 | bullet 19: pass; bullet 22: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-19.log |
| S01.stuck-detect | pass | 2aae48b67a57 | bullet 8: pass; bullet 22: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-nudge | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-11.log |
| S01.stuck-recover | pass | 2aae48b67a57 | bullet 8: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-thresholds | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-10.log |
| S01.tool-exception | pass | 2aae48b67a57 | bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-14.log |
| S01.unknown-tool | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S01/transcripts/S01-agent-loop-03.log |
| S02.anthropic-thinking | pass | a11a17b3df61 | bullet 7: pass; bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | a11a17b3df61 | bullet 1: pass; bullet 2: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | a11a17b3df61 | bullet 1: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | a11a17b3df61 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-15.log |
| S02.conversation-stats | pass | a11a17b3df61 | bullet 22: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-22.log |
| S02.error-mapping | pass | a11a17b3df61 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-09.log |
| S02.image-adapter-loss | pass | a11a17b3df61 | bullet 19: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-19.log |
| S02.image-inline | pass | a11a17b3df61 | bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-17.log |
| S02.image-request-guard | pass | a11a17b3df61 | bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-18.log |
| S02.log-completions | pass | a11a17b3df61 | bullet 1: pass; bullet 20: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | a11a17b3df61 | bullet 16: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-16.log |
| S02.model-features | pass | a11a17b3df61 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-09.log |
| S02.native-tool-calling | pass | a11a17b3df61 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | a11a17b3df61 | bullet 7: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | a11a17b3df61 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-10.log |
| S02.reasoning-content | pass | a11a17b3df61 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | a11a17b3df61 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-09.log |
| S02.retries | pass | a11a17b3df61 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-11.log |
| S02.serialization | pass | a11a17b3df61 | bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-21.log |
| S02.stream-no-callback | pass | a11a17b3df61 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-03.log |
| S02.thinking-text-reply | pass | a11a17b3df61 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-08.log |
| S02.timeouts | pass | a11a17b3df61 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | a11a17b3df61 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S02/transcripts/S02-llm-core-15.log |
| S04.arun-interrupt | pass | a11a17b3df61 | bullet 14: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-14.log |
| S04.arun-pause-persisted | pass | a11a17b3df61 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-15.log |
| S04.ask-agent-usage-saved | pass | a11a17b3df61 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-05.log |
| S04.async-callback | pass | a11a17b3df61 | bullet 13: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-13.log |
| S04.callbacks | pass | a11a17b3df61 | bullet 2: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | a11a17b3df61 | bullet 16: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-16.log |
| S04.close | pass | a11a17b3df61 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-10.log |
| S04.conversation-id | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-01.log |
| S04.custom-file-store | pass | a11a17b3df61 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-07.log |
| S04.factory | pass | a11a17b3df61 | bullet 1: pass; bullet 26: pass; bullet 30: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | a11a17b3df61 | bullet 24: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-24.log |
| S04.fork | pass | a11a17b3df61 | bullet 19: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-19.log |
| S04.fork-branch | pass | a11a17b3df61 | bullet 21: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-21.log |
| S04.fork-keeps-secrets | pass | a11a17b3df61 | bullet 20: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-20.log |
| S04.goal-loop | pass | a11a17b3df61 | bullet 22: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-22.log |
| S04.pause | pass | a11a17b3df61 | bullet 11: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-11.log |
| S04.persist-events | pass | a11a17b3df61 | bullet 2: pass; bullet 3: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-02.log |
| S04.resume | pass | a11a17b3df61 | bullet 2: pass; bullet 4: pass; bullet 26: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | a11a17b3df61 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-06.log |
| S04.run-error | pass | a11a17b3df61 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-09.log |
| S04.secrets-constructor | pass | a11a17b3df61 | bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-masking | pass | a11a17b3df61 | bullet 17: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-update | pass | a11a17b3df61 | bullet 17: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-17.log |
| S04.stats | pass | a11a17b3df61 | bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-25.log |
| S04.title-and-tags | pass | a11a17b3df61 | bullet 24: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-24.log |
| S04.visualizer-custom | pass | a11a17b3df61 | bullet 18: pass; bullet 28: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-18.log |
| S04.visualizer-default | pass | a11a17b3df61 | bullet 18: pass; bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S04/transcripts/S04-local-conversation-18.log |
| S05.completion-log-event | pass | a11a17b3df61 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-02.log |
| S05.event-base | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.event-cache | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.event-log-append | pass | a11a17b3df61 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-05.log |
| S05.event-log-files | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.event-log-recovery | pass | a11a17b3df61 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-06.log |
| S05.event-tree | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.events-to-messages | pass | a11a17b3df61 | bullet 1: pass; bullet 7: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.json-roundtrip | pass | a11a17b3df61 | bullet 1: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.openai-format | pass | a11a17b3df61 | bullet 1: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.resume-transcript | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.streaming-delta | pass | a11a17b3df61 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-02.log |
| S05.system-prompt-blocks | pass | a11a17b3df61 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-10.log |
| S05.to-llm-message | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.unmatched-actions | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S05.visualize | pass | a11a17b3df61 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S05/transcripts/S05-events-01.log |
| S20.automation-context | pass | ede5eb7d1db8 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-08.log |
| S20.automation-headers | pass | ede5eb7d1db8 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-08.log |
| S20.automation-kwargs | pass | ede5eb7d1db8 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-08.log |
| S20.conversation-args | pass | ede5eb7d1db8 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.delegate-trace | pass | ede5eb7d1db8 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-06.log |
| S20.enable-gate | pass | ede5eb7d1db8 | bullet 1: pass; bullet 3: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.env-conversation-defaults | pass | ede5eb7d1db8 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-02.log |
| S20.external-entry | pass | ede5eb7d1db8 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-02.log |
| S20.get-env | pass | ede5eb7d1db8 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-08.log |
| S20.laminar-init | pass | ede5eb7d1db8 | bullet 3: pass; bullet 12: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-03.log |
| S20.lazy-import | pass | ede5eb7d1db8 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-07.log |
| S20.llm-retry-log | pass | ede5eb7d1db8 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-10.log |
| S20.llm-span | pass | ede5eb7d1db8 | bullet 4: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-04.log |
| S20.llm-span-content | pass | ede5eb7d1db8 | bullet 5: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-05.log |
| S20.logger-config | pass | ede5eb7d1db8 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-09.log |
| S20.logger-quiet-thirdparty | pass | ede5eb7d1db8 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-09.log |
| S20.otel-backend | pass | ede5eb7d1db8 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.parallel-span-context | pass | ede5eb7d1db8 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.rolling-log-view | pass | ede5eb7d1db8 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-09.log |
| S20.root-span | pass | ede5eb7d1db8 | bullet 1: pass; bullet 11: pass; bullet 12: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.step-and-tool-spans | pass | ede5eb7d1db8 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-01.log |
| S20.utility-operation-metadata | pass | ede5eb7d1db8 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk-verify/S20/transcripts/S20-observability-04.log |
