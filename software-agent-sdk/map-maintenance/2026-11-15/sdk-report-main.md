## Conflicting attempts

- S02.error-mapping: fail at 2026-11-15T08:29:34+00:00, pass at 2026-11-15T09:04:38+00:00
- S14.preset-gpt5-gemini: fail at 2026-11-15T08:30:41+00:00, pass at 2026-11-15T08:32:57+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S02.metrics | fail | 2aae48b67a57 | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 22: pass; bullet 23: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | 2aae48b67a57 | bullet 12: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-12.log |
| S02.responses-reasoning | fail | 2aae48b67a57 | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | 2aae48b67a57 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 23: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-04.log |
| S03.registry-stats-wiring | fail | 2aae48b67a57 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-02.log |
| S04.interactive-terminal | fail | 2aae48b67a57 | bullet 21: fail (block 1 exited 1); bullet 27: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-21.log |
| S07.installed-lifecycle | fail | 2aae48b67a57 | bullet 6: pass; bullet 13: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-13.log |
| S08.secret-expansion | fail | 2aae48b67a57 | bullet 3: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-03.log |
| S09.session-recovery | fail | 2aae48b67a57 | bullet 11: pass; bullet 12: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-12.log |
| S11.task-observability | fail | 2aae48b67a57 | bullet 2: fail (block 1 exited 1); bullet 4: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-02.log |
| S13.confirm-approve-reject | fail | 2aae48b67a57 | bullet 1: pass; bullet 6: fail (block 1 exited 1); bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-06.log |
| S13.confirm-wait | fail | 2aae48b67a57 | bullet 1: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-06.log |
| S13.llm-analyzer | fail | 2aae48b67a57 | bullet 1: pass; bullet 6: fail (block 1 exited 1); bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13-rerun2/transcripts/S13-security-confirmation-06.log |
| S14.apply-patch | fail | 2aae48b67a57 | bullet 1: pass; bullet 9: pass; bullet 11: pass; bullet 13: fail (block 1 exited 1); bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-13.log |
| S14.gemini-file-tools | fail | 2aae48b67a57 | bullet 11: pass; bullet 13: fail (block 1 exited 1); bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-13.log |
| S14.terminal-backend-select | fail | 2aae48b67a57 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-06.log |
| S14.terminal-input-encoding | fail | 2aae48b67a57 | bullet 2: pass; bullet 5: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-05.log |
| S14.terminal-reset | fail | 2aae48b67a57 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-06.log |
| S15.tabs | fail | 2aae48b67a57 | bullet 1: pass; bullet 2: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-02.log |
| S17.schema-constraints | fail | 2aae48b67a57 | bullet 4: fail (block 1 exited 1) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-04.log |
| S05.token-event | blocked | 2aae48b67a57 | bullet 9: blocked (bullet is labeled blocked) |  |
| S14.terminal-windows | blocked | 2aae48b67a57 | bullet 7: blocked (bullet is labeled blocked) |  |
| S15.chromium-detection | blocked | 2aae48b67a57 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-03.log |
| S15.degrade-on-failure | blocked | 2aae48b67a57 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-03.log |
| S15.recording-storage | blocked | 2aae48b67a57 | bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) |  |
| S01.ask-agent | pass | 2aae48b67a57 | bullet 17: pass; bullet 20: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-17.log |
| S01.async-step | pass | 2aae48b67a57 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-15.log |
| S01.content-policy | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.context-overflow | pass | 2aae48b67a57 | bullet 19: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-19.log |
| S01.empty-reply-nudge | pass | 2aae48b67a57 | bullet 3: pass; bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.finish-truncates-batch | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.image-input | pass | 2aae48b67a57 | bullet 16: pass; bullet 24: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.image-non-vision | pass | 2aae48b67a57 | bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.iterative-refinement | pass | 2aae48b67a57 | bullet 22: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-22.log |
| S01.malformed-tool-call | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-06.log |
| S01.max-iterations | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-05.log |
| S01.message-while-running | pass | 2aae48b67a57 | bullet 14: pass; bullet 15: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-14.log |
| S01.parallel-resource-locks | pass | 2aae48b67a57 | bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-12.log |
| S01.parallel-tools | pass | 2aae48b67a57 | bullet 11: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.response-dispatch | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass; bullet 20: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.run-to-finish | pass | 2aae48b67a57 | bullet 1: pass; bullet 20: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | 2aae48b67a57 | bullet 18: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-18.log |
| S01.stuck-detect | pass | 2aae48b67a57 | bullet 7: pass; bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-07.log |
| S01.stuck-nudge | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-10.log |
| S01.stuck-recover | pass | 2aae48b67a57 | bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-07.log |
| S01.stuck-thresholds | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-09.log |
| S01.tool-exception | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-13.log |
| S01.unknown-tool | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S01/transcripts/S01-agent-loop-03.log |
| S02.anthropic-thinking | pass | 2aae48b67a57 | bullet 7: pass; bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | 2aae48b67a57 | bullet 1: pass; bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | 2aae48b67a57 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-15.log |
| S02.conversation-stats | pass | 2aae48b67a57 | bullet 22: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-22.log |
| S02.error-mapping | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-07.log |
| S02.image-adapter-loss | pass | 2aae48b67a57 | bullet 19: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-19.log |
| S02.image-inline | pass | 2aae48b67a57 | bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-17.log |
| S02.image-request-guard | pass | 2aae48b67a57 | bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-18.log |
| S02.log-completions | pass | 2aae48b67a57 | bullet 1: pass; bullet 20: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | 2aae48b67a57 | bullet 16: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-16.log |
| S02.model-features | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-09.log |
| S02.native-tool-calling | pass | 2aae48b67a57 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | 2aae48b67a57 | bullet 7: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-10.log |
| S02.reasoning-content | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-09.log |
| S02.retries | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-11.log |
| S02.serialization | pass | 2aae48b67a57 | bullet 21: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-21.log |
| S02.stream-no-callback | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-03.log |
| S02.thinking-text-reply | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-08.log |
| S02.timeouts | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | 2aae48b67a57 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S02/transcripts/S02-llm-core-15.log |
| S03.agent-llm-discovery | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.fallback-metrics | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-profile-resolution | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-skip | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.fallback-transient | pass | 2aae48b67a57 | bullet 7: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.meta-profile-store | pass | 2aae48b67a57 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-15.log |
| S03.multimodal-router-images | pass | 2aae48b67a57 | bullet 5: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.multimodal-router-text | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.profile-concurrency-limits | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-migration | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-save-load | pass | 2aae48b67a57 | bullet 8: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.profile-secrets | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.provider-connections | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-09.log |
| S03.random-router | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.registry-crud | pass | 2aae48b67a57 | bullet 1: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.registry-independent-metrics | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.route-task-to-model | pass | 2aae48b67a57 | bullet 14: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.router-validation | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.session-per-conversation | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-03.log |
| S03.subscription-login | pass | 2aae48b67a57 | bullet 16: pass; bullet 20: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-16.log |
| S03.subscription-requests | pass | 2aae48b67a57 | bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-16.log |
| S03.switch-keeps-usage | pass | 2aae48b67a57 | bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.switch-llm-object | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.switch-llm-tool | pass | 2aae48b67a57 | bullet 13: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-13.log |
| S03.switch-profile | pass | 2aae48b67a57 | bullet 10: pass; bullet 17: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S03/transcripts/S03-llm-routing-profiles-10.log |
| S04.arun-interrupt | pass | 2aae48b67a57 | bullet 13: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-13.log |
| S04.arun-pause-persisted | pass | 2aae48b67a57 | bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.ask-agent-usage-saved | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-05.log |
| S04.async-callback | pass | 2aae48b67a57 | bullet 12: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-12.log |
| S04.callbacks | pass | 2aae48b67a57 | bullet 2: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | 2aae48b67a57 | bullet 15: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-15.log |
| S04.close | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-10.log |
| S04.conversation-id | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.custom-file-store | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-07.log |
| S04.factory | pass | 2aae48b67a57 | bullet 1: pass; bullet 24: pass; bullet 28: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | 2aae48b67a57 | bullet 22: pass; bullet 24: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-22.log |
| S04.fork | pass | 2aae48b67a57 | bullet 18: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-18.log |
| S04.fork-branch | pass | 2aae48b67a57 | bullet 19: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-19.log |
| S04.goal-loop | pass | 2aae48b67a57 | bullet 20: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-20.log |
| S04.pause | pass | 2aae48b67a57 | bullet 11: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-11.log |
| S04.persist-events | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume | pass | 2aae48b67a57 | bullet 2: pass; bullet 4: pass; bullet 24: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-06.log |
| S04.run-error | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-09.log |
| S04.secrets-constructor | pass | 2aae48b67a57 | bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-16.log |
| S04.secrets-masking | pass | 2aae48b67a57 | bullet 16: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-16.log |
| S04.secrets-update | pass | 2aae48b67a57 | bullet 16: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-16.log |
| S04.stats | pass | 2aae48b67a57 | bullet 23: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-23.log |
| S04.title-and-tags | pass | 2aae48b67a57 | bullet 22: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-22.log |
| S04.visualizer-custom | pass | 2aae48b67a57 | bullet 17: pass; bullet 26: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-17.log |
| S04.visualizer-default | pass | 2aae48b67a57 | bullet 17: pass; bullet 25: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S04/transcripts/S04-local-conversation-17.log |
| S05.completion-log-event | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-02.log |
| S05.error-classification | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-02.log |
| S05.event-base | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.event-cache | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.event-log-append | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-03.log |
| S05.event-log-files | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.event-log-recovery | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-04.log |
| S05.event-tree | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.events-to-messages | pass | 2aae48b67a57 | bullet 1: pass; bullet 5: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.json-roundtrip | pass | 2aae48b67a57 | bullet 1: pass; bullet 5: pass; bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.openai-format | pass | 2aae48b67a57 | bullet 1: pass; bullet 5: pass; bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.resume-transcript | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.streaming-delta | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-02.log |
| S05.system-prompt-blocks | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-08.log |
| S05.to-llm-message | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.unmatched-actions | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S05.visualize | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S05/transcripts/S05-events-01.log |
| S06.condenser-resume | pass | 2aae48b67a57 | bullet 12: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-12.log |
| S06.context-datetime | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-overflow-request | pass | 2aae48b67a57 | bullet 11: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-11.log |
| S06.context-secrets | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-skills | pass | 2aae48b67a57 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-suffixes | pass | 2aae48b67a57 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.hard-reset | pass | 2aae48b67a57 | bullet 9: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-09.log |
| S06.manual-condense | pass | 2aae48b67a57 | bullet 10: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-10.log |
| S06.memory-load | pass | 2aae48b67a57 | bullet 3: pass; bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.memory-write-path | pass | 2aae48b67a57 | bullet 3: pass; bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.noop-condenser | pass | 2aae48b67a57 | bullet 6: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.observation-dispositions | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-07.log |
| S06.persona-soul | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.pipeline-condenser | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-13.log |
| S06.soft-vs-hard | pass | 2aae48b67a57 | bullet 8: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-08.log |
| S06.summarizing-reasons | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.summarizing-size | pass | 2aae48b67a57 | bullet 4: pass; bullet 14: pass; bullet 15: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.summarizing-tokens | pass | 2aae48b67a57 | bullet 5: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-05.log |
| S06.summary-llm-streaming | pass | 2aae48b67a57 | bullet 4: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.system-prompt-custom | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-model-specific | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-registry | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.view | pass | 2aae48b67a57 | bullet 4: pass; bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.view-atomicity | pass | 2aae48b67a57 | bullet 4: pass; bullet 14: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S06/transcripts/S06-context-condensers-04.log |
| S07.agentskills-load | pass | 2aae48b67a57 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.agentskills-trigger | pass | 2aae48b67a57 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.available-skills-prompt | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.disable-model-invocation | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.disabled-skills | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-05.log |
| S07.inline-commands | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-autoattach | pass | 2aae48b67a57 | bullet 2: pass; bullet 10: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-run | pass | 2aae48b67a57 | bullet 2: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.keyword-trigger | pass | 2aae48b67a57 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.load-project-flag | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-05.log |
| S07.marketplace-install | pass | 2aae48b67a57 | bullet 6: pass; bullet 7: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-06.log |
| S07.merge-precedence | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-05.log |
| S07.message-suffixes | pass | 2aae48b67a57 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.path-rules | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-04.log |
| S07.project-skills | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-05.log |
| S07.public-skills | pass | 2aae48b67a57 | bullet 8: pass; bullet 9: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-08.log |
| S07.repo-skill-always-on | pass | 2aae48b67a57 | bullet 1: pass; bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.resources | pass | 2aae48b67a57 | bullet 2: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.serialization | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.skill-mcp-json | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-02.log |
| S07.task-trigger | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.trigger-once | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-01.log |
| S07.user-skills | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S07/transcripts/S07-skills-05.log |
| S08.agent-plugins-layout | pass | 2aae48b67a57 | bullet 1: pass; bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.agent-plugins-mcp | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.ambient-plugins | pass | 2aae48b67a57 | bullet 2: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.claude-code-layout | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.commands-as-skills | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.conversation-attach | pass | 2aae48b67a57 | bullet 2: pass; bullet 4: pass; bullet 16: pass; bullet 17: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.fetch-cache | pass | 2aae48b67a57 | bullet 4: pass; bullet 5: pass; bullet 6: pass; bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-04.log |
| S08.installation-manager | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-10.log |
| S08.installed-plugins | pass | 2aae48b67a57 | bullet 7: pass; bullet 9: pass; bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-07.log |
| S08.load-plugin-runtime | pass | 2aae48b67a57 | bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-14.log |
| S08.marketplace-auto-load | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-13.log |
| S08.marketplace-import-path | pass | 2aae48b67a57 | bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-15.log |
| S08.marketplace-manifest | pass | 2aae48b67a57 | bullet 11: pass; bullet 18: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-11.log |
| S08.marketplace-registry | pass | 2aae48b67a57 | bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-12.log |
| S08.merge-semantics | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.path-containment | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.plugin-agents | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.resolved-refs | pass | 2aae48b67a57 | bullet 2: pass; bullet 16: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.source-parsing | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S09.argument-validation | pass | 2aae48b67a57 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-13.log |
| S09.config-secrets | pass | 2aae48b67a57 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-04.log |
| S09.filter-tools-regex | pass | 2aae48b67a57 | bullet 2: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-06.log |
| S09.listing-timeout | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-05.log |
| S09.oauth | pass | 2aae48b67a57 | bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-09.log |
| S09.observation | pass | 2aae48b67a57 | bullet 1: pass; bullet 13: pass; bullet 14: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.protocol-negotiation | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-07.log |
| S09.schema-conversion | pass | 2aae48b67a57 | bullet 1: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | 2aae48b67a57 | bullet 1: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.startup-failure-tolerated | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-03.log |
| S09.static-auth | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-08.log |
| S09.stdio-server | pass | 2aae48b67a57 | bullet 1: pass; bullet 6: pass; bullet 14: pass; bullet 15: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | 2aae48b67a57 | bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-13.log |
| S09.tools-list-changed | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S09/transcripts/S09-mcp-01.log |
| S10.agent-hook | pass | 2aae48b67a57 | bullet 4: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-04.log |
| S10.async-hooks | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.blocked-state-persistence | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-02.log |
| S10.command-exec | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-discovery | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-format | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-03.log |
| S10.definition-validation | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-03.log |
| S10.execution-events | pass | 2aae48b67a57 | bullet 1: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.exit-codes | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.llm-follows-switch | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-04.log |
| S10.matcher | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.plugin-hooks-merge | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-05.log |
| S10.plugin-hooks-reload-once | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-06.log |
| S10.post-tool-use | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.pre-tool-use-block | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.prompt-hook | pass | 2aae48b67a57 | bullet 4: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-04.log |
| S10.session-end-on-close | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.session-start | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.stop-hook | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S10.user-prompt-block | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-02.log |
| S10.user-prompt-context | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S10/transcripts/S10-hooks-01.log |
| S11.builtin-agents | pass | 2aae48b67a57 | bullet 6: pass; bullet 8: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-06.log |
| S11.conversation-autoregister | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-08.log |
| S11.definition-factory | pass | 2aae48b67a57 | bullet 5: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.definition-model | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.delegate-executor | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.delegation-visualizer | pass | 2aae48b67a57 | bullet 11: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.factory-info | pass | 2aae48b67a57 | bullet 6: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-06.log |
| S11.file-discovery | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.file-precedence | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.markdown-schema | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.plugin-agents | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-if-absent | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-programmatic | pass | 2aae48b67a57 | bullet 1: pass; bullet 5: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.sub-agent-scope | pass | 2aae48b67a57 | bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-10.log |
| S11.task-confirmation | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-09.log |
| S11.task-errors | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-hooks | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-limits | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-metrics | pass | 2aae48b67a57 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-persistence | pass | 2aae48b67a57 | bullet 1: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-resume | pass | 2aae48b67a57 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-run | pass | 2aae48b67a57 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-secrets | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S11/transcripts/S11-subagents-delegation-03.log |
| S12.api-evaluate | pass | 2aae48b67a57 | bullet 3: pass; bullet 5: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-03.log |
| S12.api-followup-prompt | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.api-key-handling | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.chat-template | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.critic-display | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.critic-result | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.custom-refine-policy | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.end-to-end-refinement | pass | 2aae48b67a57 | bullet 3: pass; bullet 4: pass; bullet 5: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-03.log |
| S12.eval-mode | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-02.log |
| S12.refinement-config | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.refinement-decision | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-02.log |
| S12.refinement-followup | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-02.log |
| S12.result-on-events | pass | 2aae48b67a57 | bullet 2: pass; bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-02.log |
| S12.rule-critics | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S12.settings-critic | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S12/transcripts/S12-critic-01.log |
| S13.analysis-event | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.ensemble | pass | 2aae48b67a57 | bullet 2: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.grayswan | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.mask-async | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-04.log |
| S13.mask-models | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-output | pass | 2aae48b67a57 | bullet 3: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-thinking | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-05.log |
| S13.mask-tool-output | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.pattern-analyzer | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policies | pass | 2aae48b67a57 | bullet 2: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policy-rails | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.risk-extraction | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.risk-levels | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.secret-injection | pass | 2aae48b67a57 | bullet 3: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-registry | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-sources | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.security-policy-prompt | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.settings-security | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.toolshield | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S14.file-editor-edit | pass | 2aae48b67a57 | bullet 8: pass; bullet 12: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.file-editor-validation | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.file-editor-view | pass | 2aae48b67a57 | bullet 8: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-08.log |
| S14.glob | pass | 2aae48b67a57 | bullet 1: pass; bullet 9: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.grep | pass | 2aae48b67a57 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.preset-default | pass | 2aae48b67a57 | bullet 11: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-11.log |
| S14.preset-gpt5-gemini | pass | 2aae48b67a57 | bullet 11: pass; bullet 13: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14-rerun/transcripts/S14-core-tools-11.log |
| S14.shared-working-dir | pass | 2aae48b67a57 | bullet 1: pass; bullet 12: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.terminal-cleanup | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-env | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-exec | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass; bullet 3: pass; bullet 12: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-01.log |
| S14.terminal-interactive | pass | 2aae48b67a57 | bullet 2: pass; bullet 4: pass; bullet 14: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-metadata | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-output-truncation | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-pane-pool | pass | 2aae48b67a57 | bullet 3: pass; bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-03.log |
| S14.terminal-secret-masking | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.terminal-timeout | pass | 2aae48b67a57 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-02.log |
| S14.tool-output-masking | pass | 2aae48b67a57 | bullet 8: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S14/transcripts/S14-core-tools-08.log |
| S15.action-routing | pass | 2aae48b67a57 | bullet 1: pass; bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.cleanup | pass | 2aae48b67a57 | bullet 1: pass; bullet 4: pass; bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.executor-config | pass | 2aae48b67a57 | bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-05.log |
| S15.interact | pass | 2aae48b67a57 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.navigate-and-read | pass | 2aae48b67a57 | bullet 1: pass; bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.observation | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.preset-browser | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-08.log |
| S15.prompt-guidance | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.recording-start-stop | pass | 2aae48b67a57 | bullet 1: pass; bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.session-recovery | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-06.log |
| S15.shared-executor | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-04.log |
| S15.storage | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S15.toolset-create | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S15/transcripts/S15-browser-01.log |
| S17.agent-tool-init | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-06.log |
| S17.annotations-and-resources | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.auto-naming | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.auto-registration | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.catalog | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.client-tool-ack | pass | 2aae48b67a57 | bullet 7: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-registration | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tool-schema | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-spec | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tools-conversation | pass | 2aae48b67a57 | bullet 7: pass; bullet 8: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.custom-tool-definition | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.execute-tool | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.injected-fields | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.llm-schemas | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.module-qualnames | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.output-coercion | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.py-type | pass | 2aae48b67a57 | bullet 3: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.register-tool | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.resolve-tool | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.schema-serialization | pass | 2aae48b67a57 | bullet 3: pass; bullet 5: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.tool-set | pass | 2aae48b67a57 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.tool-spec | pass | 2aae48b67a57 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.usability | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S20.automation-context | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-08.log |
| S20.automation-headers | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-08.log |
| S20.automation-kwargs | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-08.log |
| S20.conversation-args | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.delegate-trace | pass | 2aae48b67a57 | bullet 6: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-06.log |
| S20.enable-gate | pass | 2aae48b67a57 | bullet 1: pass; bullet 3: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.env-conversation-defaults | pass | 2aae48b67a57 | bullet 2: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-02.log |
| S20.external-entry | pass | 2aae48b67a57 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-02.log |
| S20.get-env | pass | 2aae48b67a57 | bullet 8: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-08.log |
| S20.laminar-init | pass | 2aae48b67a57 | bullet 3: pass; bullet 11: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-03.log |
| S20.lazy-import | pass | 2aae48b67a57 | bullet 7: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-07.log |
| S20.llm-span | pass | 2aae48b67a57 | bullet 4: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-04.log |
| S20.llm-span-content | pass | 2aae48b67a57 | bullet 5: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-05.log |
| S20.logger-config | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-09.log |
| S20.logger-quiet-thirdparty | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-09.log |
| S20.otel-backend | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.parallel-span-context | pass | 2aae48b67a57 | bullet 1: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.rolling-log-view | pass | 2aae48b67a57 | bullet 9: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-09.log |
| S20.root-span | pass | 2aae48b67a57 | bullet 1: pass; bullet 10: pass; bullet 11: blocked (bullet is labeled blocked) | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.step-and-tool-spans | pass | 2aae48b67a57 | bullet 1: pass; bullet 10: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-01.log |
| S20.utility-operation-metadata | pass | 2aae48b67a57 | bullet 4: pass | /tmp/claude-0/-home-user/69e6673c-4297-5278-94b4-b3ff6d575b6f/scratchpad/sdk/S20/transcripts/S20-observability-04.log |
