## Conflicting attempts

- S04.close: fail at 2026-11-17T10:40:07+00:00, pass at 2026-11-17T10:40:37+00:00, pass at 2026-11-17T10:45:55+00:00
- S14.apply-patch: fail at 2026-11-17T09:29:06+00:00, fail at 2026-11-17T10:02:16+00:00, pass at 2026-11-17T10:54:59+00:00
- S14.glob: fail at 2026-11-17T09:29:06+00:00, fail at 2026-11-17T10:02:16+00:00, pass at 2026-11-17T10:54:59+00:00
- S14.grep: fail at 2026-11-17T09:29:06+00:00, fail at 2026-11-17T10:02:16+00:00, pass at 2026-11-17T10:11:23+00:00, pass at 2026-11-17T10:54:59+00:00
- S14.shared-working-dir: fail at 2026-11-17T09:29:06+00:00, fail at 2026-11-17T09:32:23+00:00, fail at 2026-11-17T10:02:16+00:00, pass at 2026-11-17T10:54:59+00:00
- S14.terminal-exec: fail at 2026-11-17T09:29:06+00:00, fail at 2026-11-17T10:02:16+00:00, pass at 2026-11-17T10:54:59+00:00
- S16.oracle-consult: fail at 2026-11-17T09:30:52+00:00, pass at 2026-11-17T09:52:56+00:00
- S16.oracle-errors: fail at 2026-11-17T09:30:52+00:00, pass at 2026-11-17T09:52:56+00:00
- S16.oracle-tool: fail at 2026-11-17T09:30:52+00:00, pass at 2026-11-17T09:52:56+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S02.error-mapping | fail | 495f1e50e7d3 | bullet 13: pass; bullet 25: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-25.log |
| S02.metrics | fail | 495f1e50e7d3 | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 22: pass; bullet 23: pass; bullet 24: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | 495f1e50e7d3 | bullet 12: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-12.log |
| S02.responses-reasoning | fail | 495f1e50e7d3 | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 26: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | 495f1e50e7d3 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 23: pass; bullet 24: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-04.log |
| S03.registry-stats-wiring | fail | 495f1e50e7d3 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 17: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-02.log |
| S04.goal-asked-branch | fail | 495f1e50e7d3 | bullet 24: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-24.log |
| S04.interactive-terminal | fail | 495f1e50e7d3 | bullet 25: fail (block 1 exited 1); bullet 31: pass | <scratch>/sdk-verifier/S04-rerun/transcripts/S04-local-conversation-25.log |
| S04.pause-during-startup | fail | 495f1e50e7d3 | bullet 12: fail (block 1 exited 1) | <scratch>/sdk-verifier/S04-rerun/transcripts/S04-local-conversation-12.log |
| S07.installed-lifecycle | fail | 495f1e50e7d3 | bullet 6: pass; bullet 14: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-14.log |
| S08.secret-expansion | fail | 495f1e50e7d3 | bullet 3: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-03.log |
| S09.runtime-add-resume | fail | 495f1e50e7d3 | bullet 17: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-17.log |
| S09.session-recovery | fail | 495f1e50e7d3 | bullet 11: pass; bullet 12: fail (block 1 exited 1) | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-12.log |
| S11.task-observability | fail | 7b3d12d12dab | bullet 2: fail (block 1 exited 1); bullet 4: blocked (bullet is labeled blocked) | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-02.log |
| S14.terminal-backend-select | fail | 7b3d12d12dab | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-06.log |
| S14.terminal-input-encoding | fail | 7b3d12d12dab | bullet 2: pass; bullet 5: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-05.log |
| S14.terminal-reset | fail | 7b3d12d12dab | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-06.log |
| S15.tabs | fail | 7b3d12d12dab | bullet 1: pass; bullet 2: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-02.log |
| S17.schema-constraints | fail | 7b3d12d12dab | bullet 4: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-04.log |
| S18.workspace-factory | fail | 7b3d12d12dab | bullet 1: pass; bullet 3: fail (block 1 exited 1) | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-03.log |
| S21.ask-agent | fail | 4a7f09bfe4b6 | bullet 2: fail (block 1 exited 1); bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-02.log |
| S21.npx-cache-warm | fail | 4a7f09bfe4b6 | bullet 5: fail (block 1 exited 1) | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-05.log |
| S21.timeouts-retry | fail | 4a7f09bfe4b6 | bullet 6: pass; bullet 7: fail (block 1 exited 1) | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-07.log |
| S14.terminal-windows | blocked | 7b3d12d12dab | bullet 9: blocked (bullet is labeled blocked) |  |
| S15.chromium-detection | blocked | 7b3d12d12dab | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-03.log |
| S15.degrade-on-failure | blocked | 7b3d12d12dab | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-03.log |
| S15.recording-storage | blocked | 7b3d12d12dab | bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) |  |
| S18.agent-sandbox | blocked | 7b3d12d12dab | bullet 11: blocked (bullet is labeled blocked) |  |
| S18.api-remote-lifecycle | blocked | 7b3d12d12dab | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.api-remote-start | blocked | 7b3d12d12dab | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.apptainer | blocked | 7b3d12d12dab | bullet 11: blocked (bullet is labeled blocked) |  |
| S18.cloud-sandbox | blocked | 7b3d12d12dab | bullet 10: blocked (bullet is labeled blocked) |  |
| S18.docker-dev-build | blocked | 7b3d12d12dab | bullet 9: blocked (bullet is labeled blocked) |  |
| S18.docker-lifecycle | blocked | 7b3d12d12dab | bullet 9: blocked (bullet is labeled blocked) |  |
| S18.docker-start | blocked | 7b3d12d12dab | bullet 9: blocked (bullet is labeled blocked) |  |
| S21.live-turn | blocked | 4a7f09bfe4b6 | bullet 15: blocked (bullet is labeled blocked) |  |
| S02.anthropic-thinking | pass | 495f1e50e7d3 | bullet 7: pass; bullet 26: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | 495f1e50e7d3 | bullet 1: pass; bullet 2: pass; bullet 23: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | 495f1e50e7d3 | bullet 1: pass; bullet 23: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | 495f1e50e7d3 | bullet 15: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-15.log |
| S02.conversation-stats | pass | 495f1e50e7d3 | bullet 22: pass; bullet 24: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-22.log |
| S02.image-adapter-loss | pass | 495f1e50e7d3 | bullet 19: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-19.log |
| S02.image-inline | pass | 495f1e50e7d3 | bullet 17: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-17.log |
| S02.image-request-guard | pass | 495f1e50e7d3 | bullet 18: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-18.log |
| S02.log-completions | pass | 495f1e50e7d3 | bullet 1: pass; bullet 20: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | 495f1e50e7d3 | bullet 16: pass; bullet 24: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-16.log |
| S02.model-features | pass | 495f1e50e7d3 | bullet 9: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-09.log |
| S02.native-tool-calling | pass | 495f1e50e7d3 | bullet 1: pass; bullet 10: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | 495f1e50e7d3 | bullet 7: pass; bullet 14: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | 495f1e50e7d3 | bullet 10: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-10.log |
| S02.reasoning-content | pass | 495f1e50e7d3 | bullet 1: pass; bullet 3: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | 495f1e50e7d3 | bullet 9: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-09.log |
| S02.retries | pass | 495f1e50e7d3 | bullet 11: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-11.log |
| S02.serialization | pass | 495f1e50e7d3 | bullet 21: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-21.log |
| S02.stream-no-callback | pass | 495f1e50e7d3 | bullet 3: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-03.log |
| S02.thinking-text-reply | pass | 495f1e50e7d3 | bullet 8: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-08.log |
| S02.timeouts | pass | 495f1e50e7d3 | bullet 6: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | 495f1e50e7d3 | bullet 15: pass | <scratch>/sdk-triage5/full-S02/transcripts/S02-llm-core-15.log |
| S03.agent-llm-discovery | pass | 495f1e50e7d3 | bullet 4: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.fallback-metrics | pass | 495f1e50e7d3 | bullet 7: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-profile-resolution | pass | 495f1e50e7d3 | bullet 7: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-skip | pass | 495f1e50e7d3 | bullet 7: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-transient | pass | 495f1e50e7d3 | bullet 7: pass; bullet 18: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.meta-profile-store | pass | 495f1e50e7d3 | bullet 15: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-15.log |
| S03.multimodal-router-images | pass | 495f1e50e7d3 | bullet 5: pass; bullet 19: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.multimodal-router-text | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.profile-concurrency-limits | pass | 495f1e50e7d3 | bullet 8: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-migration | pass | 495f1e50e7d3 | bullet 8: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-save-load | pass | 495f1e50e7d3 | bullet 8: pass; bullet 18: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-secrets | pass | 495f1e50e7d3 | bullet 8: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.provider-connections | pass | 495f1e50e7d3 | bullet 9: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-09.log |
| S03.random-router | pass | 495f1e50e7d3 | bullet 6: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.registry-crud | pass | 495f1e50e7d3 | bullet 1: pass; bullet 18: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.registry-independent-metrics | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.route-task-to-model | pass | 495f1e50e7d3 | bullet 14: pass; bullet 19: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.router-validation | pass | 495f1e50e7d3 | bullet 6: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.session-per-conversation | pass | 495f1e50e7d3 | bullet 3: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-03.log |
| S03.subscription-login | pass | 495f1e50e7d3 | bullet 16: pass; bullet 20: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-16.log |
| S03.subscription-requests | pass | 495f1e50e7d3 | bullet 16: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-16.log |
| S03.switch-keeps-usage | pass | 495f1e50e7d3 | bullet 12: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.switch-llm-object | pass | 495f1e50e7d3 | bullet 11: pass | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.switch-llm-tool | pass | 495f1e50e7d3 | bullet 13: pass; bullet 19: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-13.log |
| S03.switch-profile | pass | 495f1e50e7d3 | bullet 10: pass; bullet 17: pass; bullet 19: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S03/transcripts/S03-llm-routing-profiles-10.log |
| S04.arun-interrupt | pass | 495f1e50e7d3 | bullet 14: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-14.log |
| S04.arun-pause-persisted | pass | 495f1e50e7d3 | bullet 15: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-15.log |
| S04.ask-agent-usage-saved | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-05.log |
| S04.async-callback | pass | 495f1e50e7d3 | bullet 13: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-13.log |
| S04.callbacks | pass | 495f1e50e7d3 | bullet 2: pass; bullet 8: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | 495f1e50e7d3 | bullet 16: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-16.log |
| S04.close | pass | 495f1e50e7d3 | bullet 10: pass | <scratch>/sdk-verifier/S04-rerun/transcripts/S04-local-conversation-10.log |
| S04.conversation-id | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-01.log |
| S04.custom-file-store | pass | 495f1e50e7d3 | bullet 7: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-07.log |
| S04.factory | pass | 495f1e50e7d3 | bullet 1: pass; bullet 28: pass; bullet 32: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | 495f1e50e7d3 | bullet 26: pass; bullet 28: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-26.log |
| S04.fork | pass | 495f1e50e7d3 | bullet 19: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-19.log |
| S04.fork-branch | pass | 495f1e50e7d3 | bullet 21: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-21.log |
| S04.fork-keeps-secrets | pass | 495f1e50e7d3 | bullet 20: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-20.log |
| S04.goal-asked | pass | 495f1e50e7d3 | bullet 23: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-23.log |
| S04.goal-loop | pass | 495f1e50e7d3 | bullet 22: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-22.log |
| S04.pause | pass | 495f1e50e7d3 | bullet 11: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-11.log |
| S04.persist-events | pass | 495f1e50e7d3 | bullet 2: pass; bullet 3: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-02.log |
| S04.resume | pass | 495f1e50e7d3 | bullet 2: pass; bullet 4: pass; bullet 28: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | 495f1e50e7d3 | bullet 6: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-06.log |
| S04.run-error | pass | 495f1e50e7d3 | bullet 9: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-09.log |
| S04.secrets-constructor | pass | 495f1e50e7d3 | bullet 17: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-masking | pass | 495f1e50e7d3 | bullet 17: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-update | pass | 495f1e50e7d3 | bullet 17: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-17.log |
| S04.stats | pass | 495f1e50e7d3 | bullet 27: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-27.log |
| S04.title-and-tags | pass | 495f1e50e7d3 | bullet 26: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-26.log |
| S04.visualizer-custom | pass | 495f1e50e7d3 | bullet 18: pass; bullet 30: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-18.log |
| S04.visualizer-default | pass | 495f1e50e7d3 | bullet 18: pass; bullet 29: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-18.log |
| S05.event-log-recovery | pass | 495f1e50e7d3 | bullet 3: pass | <scratch>/sdk-triage5/full-S04/transcripts/S04-local-conversation-03.log |
| S07.agentskills-load | pass | 495f1e50e7d3 | bullet 2: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.agentskills-trigger | pass | 495f1e50e7d3 | bullet 2: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.available-skills-prompt | pass | 495f1e50e7d3 | bullet 2: pass; bullet 3: pass; bullet 11: pass; bullet 16: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.disable-model-invocation | pass | 495f1e50e7d3 | bullet 2: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.disabled-skills | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-05.log |
| S07.inline-commands | pass | 495f1e50e7d3 | bullet 2: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-autoattach | pass | 495f1e50e7d3 | bullet 2: pass; bullet 11: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-run | pass | 495f1e50e7d3 | bullet 2: pass; bullet 11: pass; bullet 16: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.keyword-trigger | pass | 495f1e50e7d3 | bullet 1: pass; bullet 12: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.load-project-flag | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-05.log |
| S07.marketplace-install | pass | 495f1e50e7d3 | bullet 6: pass; bullet 7: pass; bullet 15: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-06.log |
| S07.merge-precedence | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-05.log |
| S07.message-suffixes | pass | 495f1e50e7d3 | bullet 1: pass; bullet 12: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.path-rules | pass | 495f1e50e7d3 | bullet 4: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-04.log |
| S07.project-skills | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-05.log |
| S07.public-skills | pass | 495f1e50e7d3 | bullet 8: pass; bullet 9: pass; bullet 12: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-08.log |
| S07.public-skills-switch | pass | 495f1e50e7d3 | bullet 10: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-10.log |
| S07.repo-skill-always-on | pass | 495f1e50e7d3 | bullet 1: pass; bullet 12: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.resources | pass | 495f1e50e7d3 | bullet 2: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.serialization | pass | 495f1e50e7d3 | bullet 1: pass; bullet 2: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.skill-mcp-json | pass | 495f1e50e7d3 | bullet 2: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-02.log |
| S07.task-trigger | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.trigger-once | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-01.log |
| S07.user-skills | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S07/transcripts/S07-skills-05.log |
| S08.agent-plugins-layout | pass | 495f1e50e7d3 | bullet 1: pass; bullet 17: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.agent-plugins-mcp | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.ambient-plugins | pass | 495f1e50e7d3 | bullet 2: pass; bullet 7: pass; bullet 8: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.claude-code-layout | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.commands-as-skills | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.conversation-attach | pass | 495f1e50e7d3 | bullet 2: pass; bullet 4: pass; bullet 16: pass; bullet 17: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.fetch-cache | pass | 495f1e50e7d3 | bullet 4: pass; bullet 5: pass; bullet 6: pass; bullet 16: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-04.log |
| S08.installation-manager | pass | 495f1e50e7d3 | bullet 10: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-10.log |
| S08.installed-plugins | pass | 495f1e50e7d3 | bullet 7: pass; bullet 9: pass; bullet 16: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-07.log |
| S08.load-plugin-runtime | pass | 495f1e50e7d3 | bullet 14: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-14.log |
| S08.marketplace-auto-load | pass | 495f1e50e7d3 | bullet 13: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-13.log |
| S08.marketplace-import-path | pass | 495f1e50e7d3 | bullet 15: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-15.log |
| S08.marketplace-manifest | pass | 495f1e50e7d3 | bullet 11: pass; bullet 18: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-11.log |
| S08.marketplace-registry | pass | 495f1e50e7d3 | bullet 12: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-12.log |
| S08.merge-semantics | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.path-containment | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.plugin-agents | pass | 495f1e50e7d3 | bullet 2: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.resolved-refs | pass | 495f1e50e7d3 | bullet 2: pass; bullet 16: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.source-parsing | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S08/transcripts/S08-plugins-marketplace-01.log |
| S09.argument-validation | pass | 495f1e50e7d3 | bullet 1: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | 495f1e50e7d3 | bullet 13: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-13.log |
| S09.config-secrets | pass | 495f1e50e7d3 | bullet 1: pass; bullet 13: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | 495f1e50e7d3 | bullet 1: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | 495f1e50e7d3 | bullet 4: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-04.log |
| S09.filter-tools-regex | pass | 495f1e50e7d3 | bullet 2: pass; bullet 15: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | 495f1e50e7d3 | bullet 6: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-06.log |
| S09.listing-timeout | pass | 495f1e50e7d3 | bullet 5: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-05.log |
| S09.oauth | pass | 495f1e50e7d3 | bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-09.log |
| S09.observation | pass | 495f1e50e7d3 | bullet 1: pass; bullet 13: pass; bullet 14: pass; bullet 15: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.protocol-negotiation | pass | 495f1e50e7d3 | bullet 7: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-07.log |
| S09.runtime-add-servers | pass | 495f1e50e7d3 | bullet 16: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-16.log |
| S09.schema-conversion | pass | 495f1e50e7d3 | bullet 1: pass; bullet 13: pass; bullet 14: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | 495f1e50e7d3 | bullet 1: pass; bullet 14: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | 495f1e50e7d3 | bullet 1: pass; bullet 7: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.startup-budget | pass | 495f1e50e7d3 | bullet 18: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-18.log |
| S09.startup-failure-tolerated | pass | 495f1e50e7d3 | bullet 3: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-03.log |
| S09.static-auth | pass | 495f1e50e7d3 | bullet 8: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-08.log |
| S09.stdio-server | pass | 495f1e50e7d3 | bullet 1: pass; bullet 6: pass; bullet 14: pass; bullet 15: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | 495f1e50e7d3 | bullet 13: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-13.log |
| S09.tools-list-changed | pass | 495f1e50e7d3 | bullet 1: pass; bullet 7: pass | <scratch>/sdk-triage5/full-S09/transcripts/S09-mcp-01.log |
| S11.builtin-agents | pass | 7b3d12d12dab | bullet 6: pass; bullet 8: pass; bullet 13: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-06.log |
| S11.conversation-autoregister | pass | 7b3d12d12dab | bullet 8: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-08.log |
| S11.definition-factory | pass | 7b3d12d12dab | bullet 5: pass; bullet 14: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.definition-model | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.delegate-executor | pass | 7b3d12d12dab | bullet 11: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-11.log |
| S11.delegation-visualizer | pass | 7b3d12d12dab | bullet 11: pass; bullet 12: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-11.log |
| S11.factory-info | pass | 7b3d12d12dab | bullet 6: pass; bullet 7: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-06.log |
| S11.file-discovery | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.file-precedence | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.markdown-schema | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.plugin-agents | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-if-absent | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-programmatic | pass | 7b3d12d12dab | bullet 1: pass; bullet 5: pass; bullet 13: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.sub-agent-scope | pass | 7b3d12d12dab | bullet 10: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-10.log |
| S11.task-confirmation | pass | 7b3d12d12dab | bullet 9: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-09.log |
| S11.task-errors | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-hooks | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-limits | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-metrics | pass | 7b3d12d12dab | bullet 1: pass; bullet 13: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-persistence | pass | 7b3d12d12dab | bullet 1: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-resume | pass | 7b3d12d12dab | bullet 1: pass; bullet 12: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-run | pass | 7b3d12d12dab | bullet 1: pass; bullet 12: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-secrets | pass | 7b3d12d12dab | bullet 3: pass | <scratch>/sdk-triage3/full-S11/transcripts/S11-subagents-delegation-03.log |
| S14.apply-patch | pass | 6eb2039a7650 | bullet 1: pass; bullet 11: pass; bullet 13: pass; bullet 15: pass; bullet 16: pass | <scratch>/sdk-coordinator-long-path-check-for-the-clip-limit-xxxxxxxxxxxxxxxxxxxxxxxx/s14b1-all/transcripts/S14-core-tools-01.log |
| S14.file-editor-edit | pass | 7b3d12d12dab | bullet 10: pass; bullet 14: pass; bullet 16: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-10.log |
| S14.file-editor-validation | pass | 7b3d12d12dab | bullet 10: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-10.log |
| S14.file-editor-view | pass | 7b3d12d12dab | bullet 10: pass; bullet 16: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-10.log |
| S14.gemini-file-tools | pass | 7b3d12d12dab | bullet 13: pass; bullet 15: pass; bullet 16: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-13.log |
| S14.glob | pass | 6eb2039a7650 | bullet 1: pass; bullet 11: pass; bullet 12: pass | <scratch>/sdk-coordinator-long-path-check-for-the-clip-limit-xxxxxxxxxxxxxxxxxxxxxxxx/s14b1-all/transcripts/S14-core-tools-01.log |
| S14.grep | pass | 6eb2039a7650 | bullet 1: pass; bullet 11: pass | <scratch>/sdk-coordinator-long-path-check-for-the-clip-limit-xxxxxxxxxxxxxxxxxxxxxxxx/s14b1-all/transcripts/S14-core-tools-01.log |
| S14.preset-default | pass | 7b3d12d12dab | bullet 13: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-13.log |
| S14.preset-gpt5-gemini | pass | 7b3d12d12dab | bullet 13: pass; bullet 15: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-13.log |
| S14.shared-working-dir | pass | 6eb2039a7650 | bullet 1: pass; bullet 14: pass | <scratch>/sdk-coordinator-long-path-check-for-the-clip-limit-xxxxxxxxxxxxxxxxxxxxxxxx/s14b1-all/transcripts/S14-core-tools-01.log |
| S14.terminal-cleanup | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-env | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-exec | pass | 6eb2039a7650 | bullet 1: pass; bullet 2: pass; bullet 3: pass; bullet 14: pass; bullet 16: pass | <scratch>/sdk-coordinator-long-path-check-for-the-clip-limit-xxxxxxxxxxxxxxxxxxxxxxxx/s14b1-all/transcripts/S14-core-tools-01.log |
| S14.terminal-interactive | pass | 7b3d12d12dab | bullet 2: pass; bullet 4: pass; bullet 16: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-metadata | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-observation-wait-cap | pass | 7b3d12d12dab | bullet 7: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-07.log |
| S14.terminal-output-truncation | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-pane-pool | pass | 7b3d12d12dab | bullet 3: pass; bullet 4: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-03.log |
| S14.terminal-secret-masking | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.terminal-shell-exit | pass | 7b3d12d12dab | bullet 7: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-07.log |
| S14.terminal-timeout | pass | 7b3d12d12dab | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-02.log |
| S14.tool-output-masking | pass | 7b3d12d12dab | bullet 10: pass; bullet 11: pass | <scratch>/sdk-triage3/full-S14/transcripts/S14-core-tools-10.log |
| S15.action-routing | pass | 7b3d12d12dab | bullet 1: pass; bullet 6: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.cleanup | pass | 7b3d12d12dab | bullet 1: pass; bullet 4: pass; bullet 6: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.executor-config | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-05.log |
| S15.interact | pass | 7b3d12d12dab | bullet 1: pass; bullet 9: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.navigate-and-read | pass | 7b3d12d12dab | bullet 1: pass; bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.observation | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.preset-browser | pass | 7b3d12d12dab | bullet 8: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-08.log |
| S15.prompt-guidance | pass | 7b3d12d12dab | bullet 1: pass; bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.recording-start-stop | pass | 7b3d12d12dab | bullet 1: pass; bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.session-recovery | pass | 7b3d12d12dab | bullet 6: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-06.log |
| S15.shared-executor | pass | 7b3d12d12dab | bullet 4: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-04.log |
| S15.storage | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S15.toolset-create | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S15/transcripts/S15-browser-01.log |
| S16.ask-user-answer | pass | 4a7f09bfe4b6 | bullet 16: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-16.log |
| S16.ask-user-chat-reply | pass | 4a7f09bfe4b6 | bullet 16: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-16.log |
| S16.ask-user-holds-completion | pass | 4a7f09bfe4b6 | bullet 16: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-16.log |
| S16.ask-user-tool | pass | 4a7f09bfe4b6 | bullet 16: pass; bullet 17: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-16.log |
| S16.conversation-mention-link | pass | 4a7f09bfe4b6 | bullet 15: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-15.log |
| S16.conversation-mention-tools | pass | 4a7f09bfe4b6 | bullet 15: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-15.log |
| S16.message-edit-event | pass | 4a7f09bfe4b6 | bullet 13: pass; bullet 14: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-13.log |
| S16.message-edit-llm-view | pass | 4a7f09bfe4b6 | bullet 13: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-13.log |
| S16.message-edit-tool | pass | 4a7f09bfe4b6 | bullet 13: pass; bullet 14: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-13.log |
| S16.oracle-consult | pass | 4a7f09bfe4b6 | bullet 4: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-errors | pass | 4a7f09bfe4b6 | bullet 4: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-tool | pass | 4a7f09bfe4b6 | bullet 4: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.plan-edit-restriction | pass | 4a7f09bfe4b6 | bullet 2: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-headers | pass | 4a7f09bfe4b6 | bullet 2: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-location | pass | 4a7f09bfe4b6 | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-then-execute | pass | 4a7f09bfe4b6 | bullet 2: pass; bullet 7: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-agent | pass | 4a7f09bfe4b6 | bullet 2: pass; bullet 7: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-tools | pass | 4a7f09bfe4b6 | bullet 2: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.reactions | pass | 4a7f09bfe4b6 | bullet 11: pass; bullet 12: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-11.log |
| S16.task-tracker-persistence | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.task-tracker-plan-view | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.tom-consult | pass | 4a7f09bfe4b6 | bullet 5: pass; bullet 9: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-sleeptime | pass | 4a7f09bfe4b6 | bullet 5: pass; bullet 9: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-storage-root | pass | 4a7f09bfe4b6 | bullet 5: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.workflow-errors-and-output | pass | 4a7f09bfe4b6 | bullet 6: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-fan-out | pass | 4a7f09bfe4b6 | bullet 6: pass; bullet 10: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-lifecycle | pass | 4a7f09bfe4b6 | bullet 6: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-pipeline | pass | 4a7f09bfe4b6 | bullet 6: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-script-validation | pass | 4a7f09bfe4b6 | bullet 6: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-toolset | pass | 4a7f09bfe4b6 | bullet 6: pass; bullet 10: pass | <scratch>/sdk-triage3/full-S16/transcripts/S16-planning-workflow-tools-06.log |
| S17.agent-tool-init | pass | 7b3d12d12dab | bullet 6: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-06.log |
| S17.annotations-and-resources | pass | 7b3d12d12dab | bullet 1: pass; bullet 3: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.auto-naming | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.auto-registration | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.catalog | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.client-tool-ack | pass | 7b3d12d12dab | bullet 7: pass; bullet 10: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-registration | pass | 7b3d12d12dab | bullet 8: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tool-schema | pass | 7b3d12d12dab | bullet 7: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-spec | pass | 7b3d12d12dab | bullet 8: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tools-conversation | pass | 7b3d12d12dab | bullet 7: pass; bullet 8: pass; bullet 10: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.custom-tool-definition | pass | 7b3d12d12dab | bullet 1: pass; bullet 3: pass; bullet 9: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.execute-tool | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.injected-fields | pass | 7b3d12d12dab | bullet 3: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.llm-schemas | pass | 7b3d12d12dab | bullet 3: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.module-qualnames | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.output-coercion | pass | 7b3d12d12dab | bullet 3: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.py-type | pass | 7b3d12d12dab | bullet 3: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.register-tool | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.resolve-tool | pass | 7b3d12d12dab | bullet 1: pass; bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.schema-serialization | pass | 7b3d12d12dab | bullet 3: pass; bullet 5: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.tool-set | pass | 7b3d12d12dab | bullet 1: pass; bullet 9: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.tool-spec | pass | 7b3d12d12dab | bullet 1: pass; bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.usability | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S17/transcripts/S17-custom-and-client-tools-02.log |
| S18.async-remote | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-02.log |
| S18.cloud-automation-tags | pass | 7b3d12d12dab | bullet 7: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-07.log |
| S18.cloud-credentials | pass | 7b3d12d12dab | bullet 7: pass; bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-07.log |
| S18.cloud-local-mode | pass | 7b3d12d12dab | bullet 7: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-07.log |
| S18.completion-callback | pass | 7b3d12d12dab | bullet 1: pass; bullet 5: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-01.log |
| S18.conversation-binding | pass | 7b3d12d12dab | bullet 1: pass; bullet 5: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-01.log |
| S18.local-ops | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-01.log |
| S18.local-pause-resume | pass | 7b3d12d12dab | bullet 1: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-01.log |
| S18.remote-alive | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-client | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-command-exec | pass | 7b3d12d12dab | bullet 2: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-files-git | pass | 7b3d12d12dab | bullet 2: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-02.log |
| S18.remote-settings | pass | 7b3d12d12dab | bullet 4: pass; bullet 8: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-04.log |
| S18.repos-and-skills | pass | 7b3d12d12dab | bullet 6: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-06.log |
| S18.runtime-scope | pass | 7b3d12d12dab | bullet 5: pass | <scratch>/sdk-triage3/full-S18/transcripts/S18-workspace-backends-05.log |
| S21.auth-selection | pass | 4a7f09bfe4b6 | bullet 9: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-09.log |
| S21.cancel-pause | pass | 4a7f09bfe4b6 | bullet 8: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-08.log |
| S21.cleanup | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.construct | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.effort | pass | 4a7f09bfe4b6 | bullet 11: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-11.log |
| S21.effort-switch | pass | 4a7f09bfe4b6 | bullet 11: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-11.log |
| S21.file-secrets | pass | 4a7f09bfe4b6 | bullet 9: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-09.log |
| S21.handshake-live | pass | 4a7f09bfe4b6 | bullet 14: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-14.log |
| S21.init-state | pass | 4a7f09bfe4b6 | bullet 1: pass; bullet 4: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.masking | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.mcp-forwarding | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.model-discovery | pass | 4a7f09bfe4b6 | bullet 10: pass; bullet 11: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-10.log |
| S21.model-selection | pass | 4a7f09bfe4b6 | bullet 1: pass; bullet 3: pass; bullet 9: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.model-switch | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.permissions-auto-approve | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.provider-registry | pass | 4a7f09bfe4b6 | bullet 13: pass; bullet 14: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-13.log |
| S21.secrets-env | pass | 4a7f09bfe4b6 | bullet 1: pass; bullet 9: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.session-resume | pass | 4a7f09bfe4b6 | bullet 3: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-03.log |
| S21.settings | pass | 4a7f09bfe4b6 | bullet 10: pass; bullet 11: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-10.log |
| S21.step | pass | 4a7f09bfe4b6 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.tool-call-events | pass | 4a7f09bfe4b6 | bullet 1: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
| S21.tracing | pass | 4a7f09bfe4b6 | bullet 12: pass | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-12.log |
| S21.usage-cost | pass | 4a7f09bfe4b6 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk-triage4/full/transcripts/S21-acp-agent-01.log |
