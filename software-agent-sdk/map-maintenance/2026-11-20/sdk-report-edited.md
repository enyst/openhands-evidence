| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S01.context-overflow | fail | a514b30b475d | bullet 20: pass; bullet 24: fail (integration tests missing [] failed ['t01_fix_simple_typo', 't02_add_bash_hello'] (<scratch>/sdk/V-S01/work/S01-agent-loop-24/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N2_20261120_090132/results.json)) | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-24.log |
| S01.run-to-finish | fail | a514b30b475d | bullet 1: pass; bullet 21: pass; bullet 24: fail (integration tests missing [] failed ['t01_fix_simple_typo', 't02_add_bash_hello'] (<scratch>/sdk/V-S01/work/S01-agent-loop-24/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N2_20261120_090132/results.json)) | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-24.log |
| S02.error-mapping | fail | a514b30b475d | bullet 13: pass; bullet 26: fail (block 1 exited 1) | <scratch>/sdk/V-S02/transcripts/S02-llm-core-26.log |
| S02.metrics | fail | a514b30b475d | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 23: pass; bullet 24: pass; bullet 25: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | a514b30b475d | bullet 12: fail (block 1 exited 1) | <scratch>/sdk/V-S02/transcripts/S02-llm-core-12.log |
| S02.responses-reasoning | fail | a514b30b475d | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 27: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | a514b30b475d | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 24: pass; bullet 25: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-04.log |
| S09.observation | fail | abd260433593 | bullet 1: pass; bullet 14: pass; bullet 15: fail (block 1 exited 1); bullet 16: pass; bullet 17: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-15.log |
| S09.session-recovery | fail | abd260433593 | bullet 12: pass; bullet 13: fail (block 1 exited 1) | <scratch>/sdk/V-S09/transcripts/S09-mcp-13.log |
| S09.startup-failure-tolerated | fail | abd260433593 | bullet 3: pass; bullet 4: fail (block 1 exited 1) | <scratch>/sdk/V-S09/transcripts/S09-mcp-04.log |
| S13.mask-output | fail | abd260433593 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 10: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-04.log |
| S13.secret-registry | fail | abd260433593 | bullet 3: pass; bullet 4: fail (block 1 exited 1) | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-04.log |
| S15.interact | fail | 5c1db4bf28a0 | bullet 1: pass; bullet 9: fail (integration tests missing [] failed ['t05_simple_browsing'] (<scratch>/sdk/V-S15/work/S15-browser-09/block1-4/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_091053/results.json)) | <scratch>/sdk/V-S15/transcripts/S15-browser-09.log |
| S15.navigate-and-read | fail | 5c1db4bf28a0 | bullet 1: pass; bullet 9: fail (integration tests missing [] failed ['t05_simple_browsing'] (<scratch>/sdk/V-S15/work/S15-browser-09/block1-4/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_091053/results.json)); bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S15/transcripts/S15-browser-09.log |
| S21.npx-cache-warm | fail | 5c1db4bf28a0 | bullet 5: fail (block 1 exited 1) | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-05.log |
| S21.timeouts-retry | fail | 5c1db4bf28a0 | bullet 6: pass; bullet 7: fail (block 1 exited 1) | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-07.log |
| S15.chromium-detection | blocked | 5c1db4bf28a0 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/V-S15/transcripts/S15-browser-03.log |
| S15.degrade-on-failure | blocked | 5c1db4bf28a0 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/V-S15/transcripts/S15-browser-03.log |
| S15.recording-storage | blocked | 5c1db4bf28a0 | bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) |  |
| S21.live-turn | blocked | 5c1db4bf28a0 | bullet 15: blocked (bullet is labeled blocked) |  |
| S01.ask-agent | pass | a514b30b475d | bullet 18: pass; bullet 21: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-18.log |
| S01.async-step | pass | a514b30b475d | bullet 16: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-16.log |
| S01.content-policy | pass | a514b30b475d | bullet 3: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-03.log |
| S01.empty-reply-nudge | pass | a514b30b475d | bullet 4: pass; bullet 5: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-04.log |
| S01.finish-truncates-batch | pass | a514b30b475d | bullet 12: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-12.log |
| S01.image-input | pass | a514b30b475d | bullet 17: pass; bullet 25: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-17.log |
| S01.image-non-vision | pass | a514b30b475d | bullet 17: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-17.log |
| S01.iterative-refinement | pass | a514b30b475d | bullet 23: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-23.log |
| S01.malformed-tool-call | pass | a514b30b475d | bullet 3: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | a514b30b475d | bullet 7: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-07.log |
| S01.max-iterations | pass | a514b30b475d | bullet 6: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-06.log |
| S01.message-while-running | pass | a514b30b475d | bullet 15: pass; bullet 16: pass; bullet 22: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-15.log |
| S01.parallel-resource-locks | pass | a514b30b475d | bullet 13: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-13.log |
| S01.parallel-tools | pass | a514b30b475d | bullet 12: pass; bullet 22: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-12.log |
| S01.response-dispatch | pass | a514b30b475d | bullet 1: pass; bullet 2: pass; bullet 21: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | abd260433593 | bullet 19: pass; bullet 22: pass | <scratch>/sdk/V-S01-so/transcripts/S01-agent-loop-19.log |
| S01.stuck-detect | pass | a514b30b475d | bullet 8: pass; bullet 22: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-nudge | pass | a514b30b475d | bullet 11: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-11.log |
| S01.stuck-recover | pass | a514b30b475d | bullet 8: pass; bullet 9: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-thresholds | pass | a514b30b475d | bullet 10: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-10.log |
| S01.tool-exception | pass | a514b30b475d | bullet 14: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-14.log |
| S01.unknown-tool | pass | a514b30b475d | bullet 3: pass | <scratch>/sdk/V-S01/transcripts/S01-agent-loop-03.log |
| S02.anthropic-thinking | pass | a514b30b475d | bullet 7: pass; bullet 27: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | a514b30b475d | bullet 1: pass; bullet 2: pass; bullet 24: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | a514b30b475d | bullet 1: pass; bullet 24: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | a514b30b475d | bullet 16: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-16.log |
| S02.conversation-stats | pass | a514b30b475d | bullet 23: pass; bullet 25: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-23.log |
| S02.image-adapter-loss | pass | a514b30b475d | bullet 20: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-20.log |
| S02.image-inline | pass | a514b30b475d | bullet 18: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-18.log |
| S02.image-request-guard | pass | a514b30b475d | bullet 19: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-19.log |
| S02.log-completions | pass | a514b30b475d | bullet 1: pass; bullet 21: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | a514b30b475d | bullet 17: pass; bullet 25: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-17.log |
| S02.model-features | pass | a514b30b475d | bullet 9: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-09.log |
| S02.native-tool-calling | pass | a514b30b475d | bullet 1: pass; bullet 10: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | a514b30b475d | bullet 1: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | a514b30b475d | bullet 7: pass; bullet 14: pass; bullet 15: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | a514b30b475d | bullet 10: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-10.log |
| S02.reasoning-content | pass | a514b30b475d | bullet 1: pass; bullet 3: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | a514b30b475d | bullet 9: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-09.log |
| S02.retries | pass | a514b30b475d | bullet 11: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-11.log |
| S02.serialization | pass | a514b30b475d | bullet 22: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-22.log |
| S02.stream-no-callback | pass | a514b30b475d | bullet 3: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-03.log |
| S02.thinking-text-reply | pass | a514b30b475d | bullet 8: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-08.log |
| S02.timeouts | pass | a514b30b475d | bullet 6: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | a514b30b475d | bullet 16: pass | <scratch>/sdk/V-S02/transcripts/S02-llm-core-16.log |
| S09.argument-validation | pass | abd260433593 | bullet 1: pass; bullet 14: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | abd260433593 | bullet 14: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-14.log |
| S09.config-secrets | pass | abd260433593 | bullet 1: pass; bullet 14: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | abd260433593 | bullet 1: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | abd260433593 | bullet 5: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-05.log |
| S09.filter-tools-regex | pass | abd260433593 | bullet 2: pass; bullet 17: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | abd260433593 | bullet 7: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-07.log |
| S09.listing-timeout | pass | abd260433593 | bullet 6: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-06.log |
| S09.oauth | pass | abd260433593 | bullet 10: pass; bullet 11: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S09/transcripts/S09-mcp-10.log |
| S09.protocol-negotiation | pass | abd260433593 | bullet 8: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-08.log |
| S09.runtime-add-resume | pass | abd260433593 | bullet 19: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-19.log |
| S09.runtime-add-servers | pass | abd260433593 | bullet 18: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-18.log |
| S09.schema-conversion | pass | abd260433593 | bullet 1: pass; bullet 14: pass; bullet 16: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | abd260433593 | bullet 1: pass; bullet 16: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | abd260433593 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.startup-budget | pass | abd260433593 | bullet 20: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-20.log |
| S09.static-auth | pass | abd260433593 | bullet 9: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-09.log |
| S09.stdio-server | pass | abd260433593 | bullet 1: pass; bullet 7: pass; bullet 16: pass; bullet 17: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | abd260433593 | bullet 14: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-14.log |
| S09.tools-list-changed | pass | abd260433593 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/V-S09/transcripts/S09-mcp-01.log |
| S13.analysis-event | pass | abd260433593 | bullet 1: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-approve-reject | pass | abd260433593 | bullet 1: pass; bullet 7: pass; bullet 11: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-wait | pass | abd260433593 | bullet 1: pass; bullet 7: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.ensemble | pass | abd260433593 | bullet 2: pass; bullet 9: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.grayswan | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.llm-analyzer | pass | abd260433593 | bullet 1: pass; bullet 7: pass; bullet 11: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.mask-async | pass | abd260433593 | bullet 5: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-05.log |
| S13.mask-models | pass | abd260433593 | bullet 3: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-thinking | pass | abd260433593 | bullet 6: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-06.log |
| S13.mask-tool-output | pass | abd260433593 | bullet 3: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-03.log |
| S13.pattern-analyzer | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.policies | pass | abd260433593 | bullet 2: pass; bullet 9: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.policy-rails | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.risk-extraction | pass | abd260433593 | bullet 1: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.risk-levels | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.secret-injection | pass | abd260433593 | bullet 3: pass; bullet 10: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-sources | pass | abd260433593 | bullet 3: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-03.log |
| S13.security-policy-prompt | pass | abd260433593 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-01.log |
| S13.settings-security | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S13.toolshield | pass | abd260433593 | bullet 2: pass | <scratch>/sdk/V-S13/transcripts/S13-security-confirmation-02.log |
| S15.action-routing | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 6: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.cleanup | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 4: pass; bullet 6: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.executor-config | pass | 5c1db4bf28a0 | bullet 5: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-05.log |
| S15.observation | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.preset-browser | pass | 5c1db4bf28a0 | bullet 8: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-08.log |
| S15.prompt-guidance | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.recording-start-stop | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.session-recovery | pass | 5c1db4bf28a0 | bullet 6: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-06.log |
| S15.shared-executor | pass | 5c1db4bf28a0 | bullet 4: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-04.log |
| S15.storage | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.tabs | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 2: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S15.toolset-create | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S15/transcripts/S15-browser-01.log |
| S21.ask-agent | pass | 5c1db4bf28a0 | bullet 2: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-02.log |
| S21.auth-selection | pass | 5c1db4bf28a0 | bullet 9: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-09.log |
| S21.cancel-pause | pass | 5c1db4bf28a0 | bullet 8: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-08.log |
| S21.cleanup | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.construct | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.effort | pass | 5c1db4bf28a0 | bullet 11: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-11.log |
| S21.effort-switch | pass | 5c1db4bf28a0 | bullet 11: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-11.log |
| S21.file-secrets | pass | 5c1db4bf28a0 | bullet 9: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-09.log |
| S21.handshake-live | pass | 5c1db4bf28a0 | bullet 14: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-14.log |
| S21.init-state | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 4: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.masking | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.mcp-forwarding | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.model-discovery | pass | 5c1db4bf28a0 | bullet 10: pass; bullet 11: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-10.log |
| S21.model-selection | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 3: pass; bullet 9: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.model-switch | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.permissions-auto-approve | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.provider-registry | pass | 5c1db4bf28a0 | bullet 13: pass; bullet 14: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-13.log |
| S21.secrets-env | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 9: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.session-resume | pass | 5c1db4bf28a0 | bullet 3: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-03.log |
| S21.settings | pass | 5c1db4bf28a0 | bullet 10: pass; bullet 11: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-10.log |
| S21.step | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.tool-call-events | pass | 5c1db4bf28a0 | bullet 1: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
| S21.tracing | pass | 5c1db4bf28a0 | bullet 12: pass | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-12.log |
| S21.usage-cost | pass | 5c1db4bf28a0 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/V-S21/transcripts/S21-acp-agent-01.log |
