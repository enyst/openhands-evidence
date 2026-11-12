## Conflicting attempts

- S02.error-mapping: pass at 2026-11-12T11:35:33+00:00, pass at 2026-11-12T11:52:28+00:00, pass at 2026-11-12T12:36:43+00:00, pass at 2026-11-12T12:42:16+00:00, fail at 2026-11-12T13:11:50+00:00
- S04.cancel-token: fail at 2026-11-12T11:46:07+00:00, fail at 2026-11-12T11:47:40+00:00, pass at 2026-11-12T11:48:55+00:00, pass at 2026-11-12T12:30:56+00:00, pass at 2026-11-12T12:49:57+00:00
- S15.interact: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.navigate-and-read: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.observation: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.prompt-guidance: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.recording-start-stop: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.storage: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00
- S15.tabs: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T11:56:58+00:00, pass at 2026-11-12T11:57:48+00:00, pass at 2026-11-12T11:58:09+00:00, pass at 2026-11-12T11:58:29+00:00, pass at 2026-11-12T11:58:52+00:00, pass at 2026-11-12T11:59:10+00:00, pass at 2026-11-12T11:59:23+00:00, fail at 2026-11-12T12:41:35+00:00, fail at 2026-11-12T12:41:58+00:00, pass at 2026-11-12T12:42:11+00:00, pass at 2026-11-12T12:42:24+00:00, pass at 2026-11-12T12:42:43+00:00, pass at 2026-11-12T12:43:01+00:00, pass at 2026-11-12T12:43:15+00:00, fail at 2026-11-12T13:18:19+00:00
- S15.toolset-create: fail at 2026-11-12T11:32:15+00:00, fail at 2026-11-12T12:41:35+00:00, pass at 2026-11-12T13:18:19+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S01.stuck-recover | fail | 068879a4eb18 | bullet 7: pass; bullet 8: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-08.log |
| S02.error-mapping | fail | ae8860e6a3d4 | bullet 12: pass; bullet 21: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S02-compliance/transcripts/S02-llm-core-21.log |
| S02.metrics | fail | fb417f7247f6 | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 18: pass; bullet 19: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | fb417f7247f6 | bullet 11: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-11.log |
| S02.responses-reasoning | fail | fb417f7247f6 | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 22: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | fb417f7247f6 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 19: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-04.log |
| S03.registry-stats-wiring | fail | 068879a4eb18 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 15: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-02.log |
| S04.interactive-terminal | fail | 31224c4ca8b9 | bullet 19: fail (block 1 exited 1); bullet 25: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-19.log |
| S07.installed-lifecycle | fail | ae8860e6a3d4 | bullet 6: pass; bullet 13: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-13.log |
| S08.secret-expansion | fail | ae8860e6a3d4 | bullet 3: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-03.log |
| S09.session-recovery | fail | ae8860e6a3d4 | bullet 10: pass; bullet 11: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-11.log |
| S11.factory-info | fail | a0644a9e5747 | bullet 6: pass; bullet 7: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-07.log |
| S11.task-observability | fail | a0644a9e5747 | bullet 2: fail (block 1 exited 1); bullet 4: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-02.log |
| S11.task-secrets | fail | ae2134fc63ee | bullet 3: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S11-fix/transcripts/S11-subagents-delegation-03.log |
| S14.terminal-backend-select | fail | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-06.log |
| S14.terminal-input-encoding | fail | 4cd6bcc59322 | bullet 2: pass; bullet 5: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-05.log |
| S14.terminal-reset | fail | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-06.log |
| S15.action-routing | fail | b74ddf43388d | bullet 1: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-06.log |
| S15.cleanup | fail | b74ddf43388d | bullet 1: pass; bullet 4: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-06.log |
| S15.session-recovery | fail | b74ddf43388d | bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-06.log |
| S15.tabs | fail | b74ddf43388d | bullet 1: pass; bullet 2: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-02.log |
| S17.schema-constraints | fail | ae2134fc63ee | bullet 4: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/FIX/sdk/S17-fix/transcripts/S17-custom-and-client-tools-04.log |
| S18.workspace-factory | fail | 068879a4eb18 | bullet 1: pass; bullet 3: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-03.log |
| S21.ask-agent | fail | 4cd6bcc59322 | bullet 2: fail (block 1 exited 1); bullet 14: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-02.log |
| S21.timeouts-retry | fail | 4cd6bcc59322 | bullet 5: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-06.log |
| S05.token-event | blocked | 068879a4eb18 | bullet 9: blocked (bullet is labeled blocked) |  |
| S14.terminal-windows | blocked | 4cd6bcc59322 | bullet 7: blocked (bullet is labeled blocked) |  |
| S15.chromium-detection | blocked | b74ddf43388d | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-03.log |
| S15.degrade-on-failure | blocked | b74ddf43388d | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-03.log |
| S15.recording-storage | blocked | b74ddf43388d | bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) |  |
| S18.agent-sandbox | blocked | 068879a4eb18 | bullet 11: blocked (bullet is labeled blocked) |  |
| S18.api-remote-lifecycle | blocked | 068879a4eb18 | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.api-remote-start | blocked | 068879a4eb18 | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.apptainer | blocked | 068879a4eb18 | bullet 11: blocked (bullet is labeled blocked) |  |
| S18.cloud-sandbox | blocked | 068879a4eb18 | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.docker-dev-build | blocked | 068879a4eb18 | bullet 9: blocked (bullet is labeled blocked) |  |
| S18.docker-lifecycle | blocked | 068879a4eb18 | bullet 9: blocked (bullet is labeled blocked) |  |
| S18.docker-start | blocked | 068879a4eb18 | bullet 9: blocked (bullet is labeled blocked) |  |
| S21.live-turn | blocked | 4cd6bcc59322 | bullet 14: blocked (bullet is labeled blocked) |  |
| S01.ask-agent | pass | 068879a4eb18 | bullet 17: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-17.log |
| S01.async-step | pass | 068879a4eb18 | bullet 15: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-15.log |
| S01.content-policy | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.context-overflow | pass | 068879a4eb18 | bullet 19: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-19.log |
| S01.empty-reply-nudge | pass | 068879a4eb18 | bullet 3: pass; bullet 4: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.finish-truncates-batch | pass | 068879a4eb18 | bullet 11: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.image-input | pass | 068879a4eb18 | bullet 16: pass; bullet 24: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.image-non-vision | pass | 068879a4eb18 | bullet 16: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.iterative-refinement | pass | 068879a4eb18 | bullet 22: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-22.log |
| S01.malformed-tool-call | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-06.log |
| S01.max-iterations | pass | 068879a4eb18 | bullet 5: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-05.log |
| S01.message-while-running | pass | 068879a4eb18 | bullet 14: pass; bullet 15: pass; bullet 21: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-14.log |
| S01.parallel-resource-locks | pass | 068879a4eb18 | bullet 12: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-12.log |
| S01.parallel-tools | pass | 068879a4eb18 | bullet 11: pass; bullet 21: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.response-dispatch | pass | 068879a4eb18 | bullet 1: pass; bullet 2: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.run-to-finish | pass | 068879a4eb18 | bullet 1: pass; bullet 20: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | 068879a4eb18 | bullet 18: pass; bullet 21: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-18.log |
| S01.stuck-detect | pass | 068879a4eb18 | bullet 7: pass; bullet 21: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-07.log |
| S01.stuck-nudge | pass | 068879a4eb18 | bullet 10: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-10.log |
| S01.stuck-thresholds | pass | 068879a4eb18 | bullet 9: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-09.log |
| S01.tool-exception | pass | 068879a4eb18 | bullet 13: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-13.log |
| S01.unknown-tool | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S01/transcripts/S01-agent-loop-03.log |
| S02.anthropic-thinking | pass | fb417f7247f6 | bullet 7: pass; bullet 22: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | fb417f7247f6 | bullet 1: pass; bullet 2: pass; bullet 19: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | fb417f7247f6 | bullet 1: pass; bullet 19: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | fb417f7247f6 | bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-14.log |
| S02.conversation-stats | pass | fb417f7247f6 | bullet 18: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-18.log |
| S02.image-inline | pass | fb417f7247f6 | bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-16.log |
| S02.log-completions | pass | fb417f7247f6 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | fb417f7247f6 | bullet 15: pass; bullet 20: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-15.log |
| S02.model-features | pass | fb417f7247f6 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-08.log |
| S02.native-tool-calling | pass | fb417f7247f6 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | fb417f7247f6 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | fb417f7247f6 | bullet 7: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | fb417f7247f6 | bullet 9: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-09.log |
| S02.reasoning-content | pass | fb417f7247f6 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | fb417f7247f6 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-08.log |
| S02.retries | pass | fb417f7247f6 | bullet 10: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-10.log |
| S02.serialization | pass | fb417f7247f6 | bullet 17: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-17.log |
| S02.stream-no-callback | pass | fb417f7247f6 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-03.log |
| S02.timeouts | pass | fb417f7247f6 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | fb417f7247f6 | bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S02/transcripts/S02-llm-core-14.log |
| S03.agent-llm-discovery | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-03.log |
| S03.fallback-metrics | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-profile-resolution | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-skip | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-transient | pass | 068879a4eb18 | bullet 6: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.meta-profile-store | pass | 068879a4eb18 | bullet 13: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-13.log |
| S03.multimodal-router-images | pass | 068879a4eb18 | bullet 4: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.multimodal-router-text | pass | 068879a4eb18 | bullet 4: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.profile-concurrency-limits | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-migration | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-save-load | pass | 068879a4eb18 | bullet 7: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-secrets | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.provider-connections | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.random-router | pass | 068879a4eb18 | bullet 5: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.registry-crud | pass | 068879a4eb18 | bullet 1: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.registry-independent-metrics | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.route-task-to-model | pass | 068879a4eb18 | bullet 12: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.router-validation | pass | 068879a4eb18 | bullet 5: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.subscription-login | pass | 068879a4eb18 | bullet 14: pass; bullet 18: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.subscription-requests | pass | 068879a4eb18 | bullet 14: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.switch-llm-object | pass | 068879a4eb18 | bullet 10: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-10.log |
| S03.switch-llm-tool | pass | 068879a4eb18 | bullet 11: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.switch-profile | pass | 068879a4eb18 | bullet 9: pass; bullet 15: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD1/sdk/S03/transcripts/S03-llm-routing-profiles-09.log |
| S04.arun-interrupt | pass | 31224c4ca8b9 | bullet 12: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-12.log |
| S04.async-callback | pass | 31224c4ca8b9 | bullet 11: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-11.log |
| S04.callbacks | pass | 31224c4ca8b9 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | 31224c4ca8b9 | bullet 13: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-13.log |
| S04.close | pass | 31224c4ca8b9 | bullet 9: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-09.log |
| S04.conversation-id | pass | 31224c4ca8b9 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.custom-file-store | pass | 31224c4ca8b9 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-06.log |
| S04.factory | pass | 31224c4ca8b9 | bullet 1: pass; bullet 22: pass; bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | 31224c4ca8b9 | bullet 20: pass; bullet 22: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-20.log |
| S04.fork | pass | 31224c4ca8b9 | bullet 16: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-16.log |
| S04.fork-branch | pass | 31224c4ca8b9 | bullet 17: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-17.log |
| S04.goal-loop | pass | 31224c4ca8b9 | bullet 18: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-18.log |
| S04.pause | pass | 31224c4ca8b9 | bullet 10: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-10.log |
| S04.persist-events | pass | 31224c4ca8b9 | bullet 2: pass; bullet 3: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume | pass | 31224c4ca8b9 | bullet 2: pass; bullet 4: pass; bullet 22: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | 31224c4ca8b9 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-05.log |
| S04.run-error | pass | 31224c4ca8b9 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-08.log |
| S04.secrets-constructor | pass | 31224c4ca8b9 | bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.secrets-masking | pass | 31224c4ca8b9 | bullet 14: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.secrets-update | pass | 31224c4ca8b9 | bullet 14: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.stats | pass | 31224c4ca8b9 | bullet 21: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-21.log |
| S04.title-and-tags | pass | 31224c4ca8b9 | bullet 20: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-20.log |
| S04.visualizer-custom | pass | 31224c4ca8b9 | bullet 15: pass; bullet 24: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-15.log |
| S04.visualizer-default | pass | 31224c4ca8b9 | bullet 15: pass; bullet 23: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-15.log |
| S05.completion-log-event | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-02.log |
| S05.error-classification | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-02.log |
| S05.event-base | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.event-cache | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.event-log-append | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-03.log |
| S05.event-log-files | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.event-log-recovery | pass | 31224c4ca8b9 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S04/transcripts/S04-local-conversation-03.log |
| S05.event-tree | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.events-to-messages | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.json-roundtrip | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.openai-format | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.resume-transcript | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.streaming-delta | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-02.log |
| S05.system-prompt-blocks | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-08.log |
| S05.to-llm-message | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.unmatched-actions | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S05.visualize | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S05/transcripts/S05-events-01.log |
| S06.condenser-resume | pass | ae8860e6a3d4 | bullet 12: pass; bullet 15: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-12.log |
| S06.context-datetime | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-overflow-request | pass | ae8860e6a3d4 | bullet 11: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-11.log |
| S06.context-secrets | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-skills | pass | ae8860e6a3d4 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-suffixes | pass | ae8860e6a3d4 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.hard-reset | pass | ae8860e6a3d4 | bullet 9: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-09.log |
| S06.manual-condense | pass | ae8860e6a3d4 | bullet 10: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-10.log |
| S06.memory-load | pass | ae8860e6a3d4 | bullet 3: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.memory-write-path | pass | ae8860e6a3d4 | bullet 3: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.noop-condenser | pass | ae8860e6a3d4 | bullet 6: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.observation-dispositions | pass | ae8860e6a3d4 | bullet 7: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-07.log |
| S06.persona-soul | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.pipeline-condenser | pass | ae8860e6a3d4 | bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-13.log |
| S06.soft-vs-hard | pass | ae8860e6a3d4 | bullet 8: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-08.log |
| S06.summarizing-reasons | pass | ae8860e6a3d4 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.summarizing-size | pass | ae8860e6a3d4 | bullet 4: pass; bullet 14: pass; bullet 15: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.summarizing-tokens | pass | ae8860e6a3d4 | bullet 5: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-05.log |
| S06.summary-llm-streaming | pass | ae8860e6a3d4 | bullet 4: pass; bullet 15: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.system-prompt-custom | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-model-specific | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-registry | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.view | pass | ae8860e6a3d4 | bullet 4: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.view-atomicity | pass | ae8860e6a3d4 | bullet 4: pass; bullet 14: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC5/sdk/S06/transcripts/S06-context-condensers-04.log |
| S07.agentskills-load | pass | ae8860e6a3d4 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.agentskills-trigger | pass | ae8860e6a3d4 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.available-skills-prompt | pass | ae8860e6a3d4 | bullet 2: pass; bullet 3: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.disable-model-invocation | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.disabled-skills | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-05.log |
| S07.inline-commands | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-autoattach | pass | ae8860e6a3d4 | bullet 2: pass; bullet 10: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-run | pass | ae8860e6a3d4 | bullet 2: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.keyword-trigger | pass | ae8860e6a3d4 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.load-project-flag | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-05.log |
| S07.marketplace-install | pass | ae8860e6a3d4 | bullet 6: pass; bullet 7: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-06.log |
| S07.merge-precedence | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-05.log |
| S07.message-suffixes | pass | ae8860e6a3d4 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.path-rules | pass | ae8860e6a3d4 | bullet 4: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-04.log |
| S07.project-skills | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-05.log |
| S07.public-skills | pass | ae8860e6a3d4 | bullet 8: pass; bullet 9: pass; bullet 11: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-08.log |
| S07.repo-skill-always-on | pass | ae8860e6a3d4 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.resources | pass | ae8860e6a3d4 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.serialization | pass | ae8860e6a3d4 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.skill-mcp-json | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-02.log |
| S07.task-trigger | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.trigger-once | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-01.log |
| S07.user-skills | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S07/transcripts/S07-skills-05.log |
| S08.agent-plugins-layout | pass | ae8860e6a3d4 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.agent-plugins-mcp | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.ambient-plugins | pass | ae8860e6a3d4 | bullet 2: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S08-resume/transcripts/S08-plugins-marketplace-02.log |
| S08.claude-code-layout | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.commands-as-skills | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.conversation-attach | pass | ae8860e6a3d4 | bullet 2: pass; bullet 4: pass; bullet 16: pass; bullet 17: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.fetch-cache | pass | ae8860e6a3d4 | bullet 4: pass; bullet 5: pass; bullet 6: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-04.log |
| S08.installation-manager | pass | ae8860e6a3d4 | bullet 10: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-10.log |
| S08.installed-plugins | pass | ae8860e6a3d4 | bullet 7: pass; bullet 9: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-07.log |
| S08.load-plugin-runtime | pass | ae8860e6a3d4 | bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-14.log |
| S08.marketplace-auto-load | pass | ae8860e6a3d4 | bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-13.log |
| S08.marketplace-import-path | pass | ae8860e6a3d4 | bullet 15: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-15.log |
| S08.marketplace-manifest | pass | ae8860e6a3d4 | bullet 11: pass; bullet 18: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-11.log |
| S08.marketplace-registry | pass | ae8860e6a3d4 | bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-12.log |
| S08.merge-semantics | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.path-containment | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.plugin-agents | pass | ae8860e6a3d4 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.resolved-refs | pass | ae8860e6a3d4 | bullet 2: pass; bullet 16: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.source-parsing | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S09.argument-validation | pass | ae8860e6a3d4 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | ae8860e6a3d4 | bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-12.log |
| S09.config-secrets | pass | ae8860e6a3d4 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | ae8860e6a3d4 | bullet 4: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-04.log |
| S09.filter-tools-regex | pass | ae8860e6a3d4 | bullet 2: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | ae8860e6a3d4 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-06.log |
| S09.listing-timeout | pass | ae8860e6a3d4 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-05.log |
| S09.oauth | pass | ae8860e6a3d4 | bullet 8: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-08.log |
| S09.observation | pass | ae8860e6a3d4 | bullet 1: pass; bullet 12: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.schema-conversion | pass | ae8860e6a3d4 | bullet 1: pass; bullet 12: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | ae8860e6a3d4 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.startup-failure-tolerated | pass | ae8860e6a3d4 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-03.log |
| S09.static-auth | pass | ae8860e6a3d4 | bullet 7: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-07.log |
| S09.stdio-server | pass | ae8860e6a3d4 | bullet 1: pass; bullet 6: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | ae8860e6a3d4 | bullet 12: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-12.log |
| S09.tools-list-changed | pass | ae8860e6a3d4 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC5/sdk/S09/transcripts/S09-mcp-01.log |
| S10.agent-hook | pass | cd2bae18bd0d | bullet 4: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-04.log |
| S10.async-hooks | pass | cd2bae18bd0d | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.blocked-state-persistence | pass | cd2bae18bd0d | bullet 2: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-02.log |
| S10.command-exec | pass | cd2bae18bd0d | bullet 1: pass; bullet 3: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-discovery | pass | cd2bae18bd0d | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-format | pass | cd2bae18bd0d | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-03.log |
| S10.definition-validation | pass | cd2bae18bd0d | bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-03.log |
| S10.execution-events | pass | cd2bae18bd0d | bullet 1: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.exit-codes | pass | cd2bae18bd0d | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.llm-follows-switch | pass | cd2bae18bd0d | bullet 4: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-04.log |
| S10.matcher | pass | cd2bae18bd0d | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.plugin-hooks-merge | pass | cd2bae18bd0d | bullet 5: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-05.log |
| S10.post-tool-use | pass | cd2bae18bd0d | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.pre-tool-use-block | pass | cd2bae18bd0d | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.prompt-hook | pass | cd2bae18bd0d | bullet 4: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-04.log |
| S10.session-end-on-close | pass | cd2bae18bd0d | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.session-start | pass | cd2bae18bd0d | bullet 1: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.stop-hook | pass | cd2bae18bd0d | bullet 1: pass; bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S10.user-prompt-block | pass | cd2bae18bd0d | bullet 2: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-02.log |
| S10.user-prompt-context | pass | cd2bae18bd0d | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD1/sdk/S10/transcripts/S10-hooks-01.log |
| S11.builtin-agents | pass | a0644a9e5747 | bullet 6: pass; bullet 8: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-06.log |
| S11.conversation-autoregister | pass | a0644a9e5747 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-08.log |
| S11.definition-factory | pass | a0644a9e5747 | bullet 5: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.definition-model | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.delegate-executor | pass | a0644a9e5747 | bullet 11: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.delegation-visualizer | pass | a0644a9e5747 | bullet 11: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.file-discovery | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.file-precedence | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.markdown-schema | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.plugin-agents | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-if-absent | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-programmatic | pass | a0644a9e5747 | bullet 1: pass; bullet 5: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.sub-agent-scope | pass | a0644a9e5747 | bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-10.log |
| S11.task-confirmation | pass | a0644a9e5747 | bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-09.log |
| S11.task-errors | pass | a0644a9e5747 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-hooks | pass | a0644a9e5747 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-limits | pass | a0644a9e5747 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-metrics | pass | a0644a9e5747 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-persistence | pass | a0644a9e5747 | bullet 1: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-resume | pass | a0644a9e5747 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-run | pass | a0644a9e5747 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S12.api-evaluate | pass | 068879a4eb18 | bullet 3: pass; bullet 5: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-03.log |
| S12.api-followup-prompt | pass | 068879a4eb18 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.api-key-handling | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.chat-template | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.critic-display | pass | 068879a4eb18 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.critic-result | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.custom-refine-policy | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.end-to-end-refinement | pass | 068879a4eb18 | bullet 3: pass; bullet 4: pass; bullet 5: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-03.log |
| S12.eval-mode | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-02.log |
| S12.refinement-config | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.refinement-decision | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-02.log |
| S12.refinement-followup | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-02.log |
| S12.result-on-events | pass | 068879a4eb18 | bullet 2: pass; bullet 4: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-02.log |
| S12.rule-critics | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S12.settings-critic | pass | 068879a4eb18 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S12/transcripts/S12-critic-01.log |
| S13.analysis-event | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-approve-reject | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-wait | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.ensemble | pass | 068879a4eb18 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.grayswan | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.llm-analyzer | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.mask-async | pass | 068879a4eb18 | bullet 4: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-04.log |
| S13.mask-models | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-output | pass | 068879a4eb18 | bullet 3: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-tool-output | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.pattern-analyzer | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policies | pass | 068879a4eb18 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policy-rails | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.risk-extraction | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.risk-levels | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.secret-injection | pass | 068879a4eb18 | bullet 3: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-registry | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-sources | pass | 068879a4eb18 | bullet 3: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.security-policy-prompt | pass | 068879a4eb18 | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.settings-security | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.toolshield | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S14.apply-patch | pass | 4cd6bcc59322 | bullet 1: pass; bullet 9: pass; bullet 11: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.file-editor-edit | pass | 4cd6bcc59322 | bullet 8: pass; bullet 12: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.file-editor-validation | pass | 4cd6bcc59322 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.file-editor-view | pass | 4cd6bcc59322 | bullet 8: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.gemini-file-tools | pass | 4cd6bcc59322 | bullet 11: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-11.log |
| S14.glob | pass | 4cd6bcc59322 | bullet 1: pass; bullet 9: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.grep | pass | 4cd6bcc59322 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.preset-default | pass | 4cd6bcc59322 | bullet 11: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-11.log |
| S14.preset-gpt5-gemini | pass | 4cd6bcc59322 | bullet 11: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-11.log |
| S14.shared-working-dir | pass | 4cd6bcc59322 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.terminal-cleanup | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-env | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-exec | pass | 4cd6bcc59322 | bullet 1: pass; bullet 2: pass; bullet 3: pass; bullet 12: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.terminal-interactive | pass | 4cd6bcc59322 | bullet 2: pass; bullet 4: pass; bullet 14: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-metadata | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-output-truncation | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-pane-pool | pass | 4cd6bcc59322 | bullet 3: pass; bullet 4: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-03.log |
| S14.terminal-secret-masking | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-timeout | pass | 4cd6bcc59322 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.tool-output-masking | pass | 4cd6bcc59322 | bullet 8: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S14/transcripts/S14-core-tools-08.log |
| S15.executor-config | pass | b74ddf43388d | bullet 5: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-05.log |
| S15.interact | pass | b74ddf43388d | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.navigate-and-read | pass | b74ddf43388d | bullet 1: pass; bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.observation | pass | b74ddf43388d | bullet 1: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.preset-browser | pass | b74ddf43388d | bullet 8: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-08.log |
| S15.prompt-guidance | pass | b74ddf43388d | bullet 1: pass; bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.recording-start-stop | pass | b74ddf43388d | bullet 1: pass; bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.shared-executor | pass | b74ddf43388d | bullet 4: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-04.log |
| S15.storage | pass | b74ddf43388d | bullet 1: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S15.toolset-create | pass | b74ddf43388d | bullet 1: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S15-split/transcripts/S15-browser-01.log |
| S16.oracle-consult | pass | a0644a9e5747 | bullet 4: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-errors | pass | a0644a9e5747 | bullet 4: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-tool | pass | a0644a9e5747 | bullet 4: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.plan-edit-restriction | pass | a0644a9e5747 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-headers | pass | a0644a9e5747 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-location | pass | a0644a9e5747 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-then-execute | pass | a0644a9e5747 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-agent | pass | a0644a9e5747 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-tools | pass | a0644a9e5747 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.reactions | pass | ae2134fc63ee | bullet 11: pass; bullet 12: pass | /tmp/claude-0/scratch/runs/FIX/sdk/S16-fix/transcripts/S16-planning-workflow-tools-11.log |
| S16.task-tracker-persistence | pass | a0644a9e5747 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.task-tracker-plan-view | pass | a0644a9e5747 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.tom-consult | pass | a0644a9e5747 | bullet 5: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-sleeptime | pass | a0644a9e5747 | bullet 5: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-storage-root | pass | a0644a9e5747 | bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.workflow-errors-and-output | pass | a0644a9e5747 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-fan-out | pass | a0644a9e5747 | bullet 6: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-lifecycle | pass | a0644a9e5747 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-pipeline | pass | a0644a9e5747 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-script-validation | pass | a0644a9e5747 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-toolset | pass | a0644a9e5747 | bullet 6: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S17.agent-tool-init | pass | 4cd6bcc59322 | bullet 6: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-06.log |
| S17.annotations-and-resources | pass | 4cd6bcc59322 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.auto-naming | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.auto-registration | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.catalog | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.client-tool-ack | pass | 4cd6bcc59322 | bullet 7: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-registration | pass | 4cd6bcc59322 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tool-schema | pass | 4cd6bcc59322 | bullet 7: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-spec | pass | 4cd6bcc59322 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tools-conversation | pass | 4cd6bcc59322 | bullet 7: pass; bullet 8: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.custom-tool-definition | pass | 4cd6bcc59322 | bullet 1: pass; bullet 3: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.execute-tool | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.injected-fields | pass | 4cd6bcc59322 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.llm-schemas | pass | 4cd6bcc59322 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.module-qualnames | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.output-coercion | pass | 4cd6bcc59322 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.py-type | pass | 4cd6bcc59322 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.register-tool | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.resolve-tool | pass | 4cd6bcc59322 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.schema-serialization | pass | 4cd6bcc59322 | bullet 3: pass; bullet 5: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.tool-set | pass | 4cd6bcc59322 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.tool-spec | pass | 4cd6bcc59322 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.usability | pass | 4cd6bcc59322 | bullet 2: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S18.async-remote | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-02.log |
| S18.cloud-automation-tags | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-07.log |
| S18.cloud-credentials | pass | 068879a4eb18 | bullet 7: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-07.log |
| S18.cloud-local-mode | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-07.log |
| S18.completion-callback | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-01.log |
| S18.conversation-binding | pass | 068879a4eb18 | bullet 1: pass; bullet 5: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-01.log |
| S18.local-ops | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-01.log |
| S18.local-pause-resume | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-01.log |
| S18.remote-alive | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-client | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-command-exec | pass | 068879a4eb18 | bullet 2: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-files-git | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-settings | pass | 068879a4eb18 | bullet 4: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-04.log |
| S18.repos-and-skills | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-06.log |
| S18.runtime-scope | pass | 068879a4eb18 | bullet 5: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S18/transcripts/S18-workspace-backends-05.log |
| S19.acp-providers-catalog | pass | 068879a4eb18 | bullet 4: pass; bullet 5: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-04.log |
| S19.acp-settings | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.apply-diff | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.condenser-settings | pass | 068879a4eb18 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.conversation-settings | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.credential-binding | pass | 068879a4eb18 | bullet 9: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-09.log |
| S19.mcp-config-secrets | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.persisted-baselines | pass | 068879a4eb18 | bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-06.log |
| S19.profile-migrations | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.profile-model | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.profile-refs | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.profile-resolve | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.profile-seed | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.profile-store | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-08.log |
| S19.pypi-baseline-gate | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-07.log |
| S19.retired-switches | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.schema-export | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.schema-migrations | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.settings-create-agent | pass | 068879a4eb18 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.settings-roundtrip | pass | 068879a4eb18 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.settings-tools | pass | 068879a4eb18 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.subscription-llm-settings | pass | 068879a4eb18 | bullet 2: pass; bullet 3: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.tool-concurrency-persona | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S19.validate-dispatch | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-02.log |
| S19.verification-settings | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S19/transcripts/S19-settings-01.log |
| S20.automation-context | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-07.log |
| S20.automation-headers | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-07.log |
| S20.automation-kwargs | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-07.log |
| S20.conversation-args | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.delegate-trace | pass | 068879a4eb18 | bullet 5: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-05.log |
| S20.enable-gate | pass | 068879a4eb18 | bullet 1: pass; bullet 3: pass; bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.env-conversation-defaults | pass | 068879a4eb18 | bullet 2: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-02.log |
| S20.external-entry | pass | 068879a4eb18 | bullet 2: pass; bullet 6: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-02.log |
| S20.get-env | pass | 068879a4eb18 | bullet 7: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-07.log |
| S20.laminar-init | pass | 068879a4eb18 | bullet 3: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-03.log |
| S20.lazy-import | pass | 068879a4eb18 | bullet 6: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-06.log |
| S20.llm-span | pass | 068879a4eb18 | bullet 4: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-04.log |
| S20.logger-config | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-08.log |
| S20.logger-quiet-thirdparty | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-08.log |
| S20.otel-backend | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.parallel-span-context | pass | 068879a4eb18 | bullet 1: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.rolling-log-view | pass | 068879a4eb18 | bullet 8: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-08.log |
| S20.root-span | pass | 068879a4eb18 | bullet 1: pass; bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.step-and-tool-spans | pass | 068879a4eb18 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-01.log |
| S20.utility-operation-metadata | pass | 068879a4eb18 | bullet 4: pass | /tmp/claude-0/scratch/runs/SD2/sdk/S20/transcripts/S20-observability-04.log |
| S21.auth-selection | pass | 4cd6bcc59322 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-08.log |
| S21.cancel-pause | pass | 4cd6bcc59322 | bullet 7: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-07.log |
| S21.cleanup | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.construct | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.effort | pass | 4cd6bcc59322 | bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-10.log |
| S21.effort-switch | pass | 4cd6bcc59322 | bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-10.log |
| S21.file-secrets | pass | 4cd6bcc59322 | bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-08.log |
| S21.handshake-live | pass | 4cd6bcc59322 | bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-13.log |
| S21.init-state | pass | 4cd6bcc59322 | bullet 1: pass; bullet 4: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.masking | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.mcp-forwarding | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.model-discovery | pass | 4cd6bcc59322 | bullet 9: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-09.log |
| S21.model-selection | pass | 4cd6bcc59322 | bullet 1: pass; bullet 3: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.model-switch | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.permissions-auto-approve | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.provider-registry | pass | 4cd6bcc59322 | bullet 12: pass; bullet 13: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-12.log |
| S21.secrets-env | pass | 4cd6bcc59322 | bullet 1: pass; bullet 8: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.session-resume | pass | 4cd6bcc59322 | bullet 3: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-03.log |
| S21.settings | pass | 4cd6bcc59322 | bullet 9: pass; bullet 10: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-09.log |
| S21.step | pass | 4cd6bcc59322 | bullet 1: pass; bullet 14: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.tool-call-events | pass | 4cd6bcc59322 | bullet 1: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
| S21.tracing | pass | 4cd6bcc59322 | bullet 11: pass | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-11.log |
| S21.usage-cost | pass | 4cd6bcc59322 | bullet 1: pass; bullet 14: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs/RC2/sdk/S21/transcripts/S21-acp-agent-01.log |
