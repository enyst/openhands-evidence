| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S01.context-overflow | fail | 722e5d403cf7 | bullet 20: pass; bullet 24: fail (integration tests missing [] failed ['t01_fix_simple_typo', 't02_add_bash_hello'] (<scratch>/sdk/B1-S01/work/S01-agent-loop-24/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N2_20261120_084721/results.json)) | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-24.log |
| S01.run-to-finish | fail | 722e5d403cf7 | bullet 1: pass; bullet 21: pass; bullet 24: fail (integration tests missing [] failed ['t01_fix_simple_typo', 't02_add_bash_hello'] (<scratch>/sdk/B1-S01/work/S01-agent-loop-24/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N2_20261120_084721/results.json)) | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-24.log |
| S02.error-mapping | fail | 722e5d403cf7 | bullet 13: pass; bullet 26: fail (block 1 exited 1) | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-26.log |
| S02.metrics | fail | 722e5d403cf7 | bullet 1: pass; bullet 5: fail (block 1 exited 1); bullet 23: pass; bullet 24: pass; bullet 25: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-05.log |
| S02.no-response-retry | fail | 722e5d403cf7 | bullet 12: fail (block 1 exited 1) | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-12.log |
| S02.responses-reasoning | fail | 722e5d403cf7 | bullet 2: pass; bullet 4: fail (block 1 exited 1); bullet 27: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-04.log |
| S02.streaming | fail | 722e5d403cf7 | bullet 3: pass; bullet 4: fail (block 1 exited 1); bullet 24: pass; bullet 25: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-04.log |
| S03.model-router-before-first-run | fail | 722e5d403cf7 | bullet 10: fail (block 1 exited 1) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-10.log |
| S03.registry-stats-wiring | fail | 722e5d403cf7 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 21: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-02.log |
| S04.goal-asked-branch | fail | 722e5d403cf7 | bullet 24: fail (block 1 exited 1) | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-24.log |
| S04.interactive-terminal | fail | 722e5d403cf7 | bullet 25: fail (block 1 exited 1); bullet 34: fail (integration tests missing [] failed ['t07_interactive_commands'] (<scratch>/sdk/B1-S04/work/S04-local-conversation-34/block1-3/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_084636/results.json)) | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-25.log |
| S04.pause-during-startup | fail | 722e5d403cf7 | bullet 12: fail (block 1 exited 1) | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-12.log |
| S05.error-classification | fail | 722e5d403cf7 | bullet 2: pass; bullet 3: fail (block 1 exited 1); bullet 4: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-03.log |
| S05.events-to-messages | fail | 722e5d403cf7 | bullet 1: pass; bullet 7: pass; bullet 9: fail (block 1 exited 1) | <scratch>/sdk/B1-S05/transcripts/S05-events-09.log |
| S06.context-overflow-request | fail | 722e5d403cf7 | bullet 12: pass; bullet 19: fail (integration tests missing [] failed ['c02_hard_context_reset', 'c03_delayed_condensation', 'c04_token_condenser', 'c05_size_condenser'] (<scratch>/sdk/B1-S06/work/S06-context-condensers-19/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N4_20261120_084327/results.json)) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-19.log |
| S06.hard-reset | fail | 722e5d403cf7 | bullet 10: pass; bullet 19: fail (integration tests missing [] failed ['c02_hard_context_reset', 'c03_delayed_condensation', 'c04_token_condenser', 'c05_size_condenser'] (<scratch>/sdk/B1-S06/work/S06-context-condensers-19/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N4_20261120_084327/results.json)) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-19.log |
| S06.soft-vs-hard | fail | 722e5d403cf7 | bullet 8: pass; bullet 9: fail (block 1 exited 1); bullet 19: fail (integration tests missing [] failed ['c02_hard_context_reset', 'c03_delayed_condensation', 'c04_token_condenser', 'c05_size_condenser'] (<scratch>/sdk/B1-S06/work/S06-context-condensers-19/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N4_20261120_084327/results.json)) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-09.log |
| S06.summarizing-size | fail | 722e5d403cf7 | bullet 4: pass; bullet 9: fail (block 1 exited 1); bullet 15: pass; bullet 16: pass; bullet 19: fail (integration tests missing [] failed ['c02_hard_context_reset', 'c03_delayed_condensation', 'c04_token_condenser', 'c05_size_condenser'] (<scratch>/sdk/B1-S06/work/S06-context-condensers-19/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N4_20261120_084327/results.json)) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-09.log |
| S06.summarizing-tokens | fail | 722e5d403cf7 | bullet 5: pass; bullet 19: fail (integration tests missing [] failed ['c02_hard_context_reset', 'c03_delayed_condensation', 'c04_token_condenser', 'c05_size_condenser'] (<scratch>/sdk/B1-S06/work/S06-context-condensers-19/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N4_20261120_084327/results.json)) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-19.log |
| S07.available-skills-prompt | fail | 722e5d403cf7 | bullet 2: pass; bullet 3: pass; bullet 11: pass; bullet 16: fail (integration tests missing [] failed ['t09_invoke_skill'] (<scratch>/sdk/B2-S07/work/S07-skills-16/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083700/results.json)) | <scratch>/sdk/B2-S07/transcripts/S07-skills-16.log |
| S07.installed-lifecycle | fail | 722e5d403cf7 | bullet 6: pass; bullet 14: fail (block 1 exited 1) | <scratch>/sdk/B2-S07/transcripts/S07-skills-14.log |
| S07.invoke-skill-run | fail | 722e5d403cf7 | bullet 2: pass; bullet 11: pass; bullet 16: fail (integration tests missing [] failed ['t09_invoke_skill'] (<scratch>/sdk/B2-S07/work/S07-skills-16/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083700/results.json)) | <scratch>/sdk/B2-S07/transcripts/S07-skills-16.log |
| S08.agent-plugins-layout | fail | 722e5d403cf7 | bullet 1: pass; bullet 17: fail (integration tests missing [] failed ['t10_agent_plugins_skill'] (<scratch>/sdk/B2-S08/work/S08-plugins-marketplace-17/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083650/results.json)) | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-17.log |
| S08.conversation-attach | fail | 722e5d403cf7 | bullet 2: pass; bullet 4: pass; bullet 16: pass; bullet 17: fail (integration tests missing [] failed ['t10_agent_plugins_skill'] (<scratch>/sdk/B2-S08/work/S08-plugins-marketplace-17/block1-2/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083650/results.json)) | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-17.log |
| S08.secret-expansion | fail | 722e5d403cf7 | bullet 3: fail (block 1 exited 1) | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-03.log |
| S09.observation | fail | 722e5d403cf7 | bullet 1: pass; bullet 14: pass; bullet 15: fail (block 1 exited 1); bullet 16: pass; bullet 17: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-15.log |
| S09.session-recovery | fail | 722e5d403cf7 | bullet 12: pass; bullet 13: fail (block 1 exited 1) | <scratch>/sdk/B2-S09/transcripts/S09-mcp-13.log |
| S09.startup-failure-tolerated | fail | 722e5d403cf7 | bullet 3: pass; bullet 4: fail (block 1 exited 1) | <scratch>/sdk/B2-S09/transcripts/S09-mcp-04.log |
| S10.command-exec | fail | 722e5d403cf7 | bullet 1: pass; bullet 3: fail (block 1 exited 1); bullet 4: pass; bullet 8: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-03.log |
| S11.delegate-executor | fail | 722e5d403cf7 | bullet 11: fail (block 1 exited 1); bullet 13: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-11.log |
| S11.task-confirmation | fail | 722e5d403cf7 | bullet 10: pass; bullet 11: fail (block 1 exited 1) | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-11.log |
| S11.task-observability | fail | 722e5d403cf7 | bullet 3: fail (block 1 exited 1); bullet 5: blocked (bullet is labeled blocked) | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-03.log |
| S11.task-persistence | fail | 722e5d403cf7 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 9: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-02.log |
| S11.task-resume | fail | 722e5d403cf7 | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 14: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-02.log |
| S15.interact | fail | 722e5d403cf7 | bullet 1: pass; bullet 9: fail (integration tests missing [] failed ['t05_simple_browsing'] (<scratch>/sdk/B3-S15/work/S15-browser-09/block1-4/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083420/results.json)) | <scratch>/sdk/B3-S15/transcripts/S15-browser-09.log |
| S15.navigate-and-read | fail | 722e5d403cf7 | bullet 1: pass; bullet 9: fail (integration tests missing [] failed ['t05_simple_browsing'] (<scratch>/sdk/B3-S15/work/S15-browser-09/block1-4/deepseek_deepseek_flash_agent-sdk-integration_N1_20261120_083420/results.json)); bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S15/transcripts/S15-browser-09.log |
| S17.schema-constraints | fail | 722e5d403cf7 | bullet 4: fail (block 1 exited 1) | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-04.log |
| S20.enable-gate | fail | 722e5d403cf7 | bullet 1: pass; bullet 3: pass; bullet 7: fail (block 1 exited 1); bullet 8: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-07.log |
| S20.external-entry | fail | 722e5d403cf7 | bullet 2: pass; bullet 7: fail (block 1 exited 1) | <scratch>/sdk/B3-S20/transcripts/S20-observability-07.log |
| S20.lazy-import | fail | 722e5d403cf7 | bullet 7: fail (block 1 exited 1) | <scratch>/sdk/B3-S20/transcripts/S20-observability-07.log |
| S21.npx-cache-warm | fail | 722e5d403cf7 | bullet 5: fail (block 1 exited 1) | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-05.log |
| S21.timeouts-retry | fail | 722e5d403cf7 | bullet 6: pass; bullet 7: fail (block 1 exited 1) | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-07.log |
| S05.token-event | blocked | 722e5d403cf7 | bullet 11: blocked (bullet is labeled blocked) |  |
| S15.chromium-detection | blocked | 722e5d403cf7 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/B3-S15/transcripts/S15-browser-03.log |
| S15.degrade-on-failure | blocked | 722e5d403cf7 | bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/B3-S15/transcripts/S15-browser-03.log |
| S15.recording-storage | blocked | 722e5d403cf7 | bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) |  |
| S21.live-turn | blocked | 722e5d403cf7 | bullet 15: blocked (bullet is labeled blocked) |  |
| S01.ask-agent | pass | 722e5d403cf7 | bullet 18: pass; bullet 21: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-18.log |
| S01.async-step | pass | 722e5d403cf7 | bullet 16: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-16.log |
| S01.content-policy | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-03.log |
| S01.empty-reply-nudge | pass | 722e5d403cf7 | bullet 4: pass; bullet 5: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-04.log |
| S01.finish-truncates-batch | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-12.log |
| S01.image-input | pass | 722e5d403cf7 | bullet 17: pass; bullet 25: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-17.log |
| S01.image-non-vision | pass | 722e5d403cf7 | bullet 17: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-17.log |
| S01.iterative-refinement | pass | 722e5d403cf7 | bullet 23: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-23.log |
| S01.malformed-tool-call | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-07.log |
| S01.max-iterations | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-06.log |
| S01.message-while-running | pass | 722e5d403cf7 | bullet 15: pass; bullet 16: pass; bullet 22: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-15.log |
| S01.parallel-resource-locks | pass | 722e5d403cf7 | bullet 13: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-13.log |
| S01.parallel-tools | pass | 722e5d403cf7 | bullet 12: pass; bullet 22: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-12.log |
| S01.response-dispatch | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass; bullet 21: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | 722e5d403cf7 | bullet 19: pass; bullet 22: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-19.log |
| S01.stuck-detect | pass | 722e5d403cf7 | bullet 8: pass; bullet 22: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-nudge | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-11.log |
| S01.stuck-recover | pass | 722e5d403cf7 | bullet 8: pass; bullet 9: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-08.log |
| S01.stuck-thresholds | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-10.log |
| S01.tool-exception | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-14.log |
| S01.unknown-tool | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S01/transcripts/S01-agent-loop-03.log |
| S02.anthropic-thinking | pass | 722e5d403cf7 | bullet 7: pass; bullet 27: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-07.log |
| S02.api-mode | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass; bullet 24: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.completion | pass | 722e5d403cf7 | bullet 1: pass; bullet 24: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.context-window-guard | pass | 722e5d403cf7 | bullet 16: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-16.log |
| S02.conversation-stats | pass | 722e5d403cf7 | bullet 23: pass; bullet 25: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-23.log |
| S02.image-adapter-loss | pass | 722e5d403cf7 | bullet 20: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-20.log |
| S02.image-inline | pass | 722e5d403cf7 | bullet 18: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-18.log |
| S02.image-request-guard | pass | 722e5d403cf7 | bullet 19: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-19.log |
| S02.log-completions | pass | 722e5d403cf7 | bullet 1: pass; bullet 21: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.message-formatting | pass | 722e5d403cf7 | bullet 17: pass; bullet 25: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-17.log |
| S02.model-features | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-09.log |
| S02.native-tool-calling | pass | 722e5d403cf7 | bullet 1: pass; bullet 10: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.pricing-override | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.prompt-caching | pass | 722e5d403cf7 | bullet 7: pass; bullet 14: pass; bullet 15: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-07.log |
| S02.prompted-tool-calling | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-10.log |
| S02.reasoning-content | pass | 722e5d403cf7 | bullet 1: pass; bullet 3: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-01.log |
| S02.reasoning-options | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-09.log |
| S02.retries | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-11.log |
| S02.serialization | pass | 722e5d403cf7 | bullet 22: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-22.log |
| S02.stream-no-callback | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-03.log |
| S02.thinking-text-reply | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-08.log |
| S02.timeouts | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-06.log |
| S02.token-count | pass | 722e5d403cf7 | bullet 16: pass | <scratch>/sdk/B1-S02/transcripts/S02-llm-core-16.log |
| S03.agent-llm-discovery | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.fallback-metrics | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.fallback-profile-resolution | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.fallback-skip | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.fallback-transient | pass | 722e5d403cf7 | bullet 11: pass; bullet 22: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.meta-profile-store | pass | 722e5d403cf7 | bullet 19: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-19.log |
| S03.model-router-add-route | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.model-router-selection | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.model-router-switch-replaces | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-09.log |
| S03.multimodal-router-images | pass | 722e5d403cf7 | bullet 5: pass; bullet 23: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.multimodal-router-text | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.profile-concurrency-limits | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.profile-migration | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.profile-save-load | pass | 722e5d403cf7 | bullet 12: pass; bullet 22: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.profile-secrets | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.provider-connections | pass | 722e5d403cf7 | bullet 13: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-13.log |
| S03.random-router | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.registry-crud | pass | 722e5d403cf7 | bullet 1: pass; bullet 22: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.registry-independent-metrics | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.route-task-to-model | pass | 722e5d403cf7 | bullet 18: pass; bullet 23: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-18.log |
| S03.router-validation | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.session-per-conversation | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-03.log |
| S03.subscription-login | pass | 722e5d403cf7 | bullet 20: pass; bullet 24: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-20.log |
| S03.subscription-requests | pass | 722e5d403cf7 | bullet 20: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-20.log |
| S03.switch-keeps-usage | pass | 722e5d403cf7 | bullet 16: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-16.log |
| S03.switch-llm-object | pass | 722e5d403cf7 | bullet 15: pass | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-15.log |
| S03.switch-llm-tool | pass | 722e5d403cf7 | bullet 17: pass; bullet 23: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-17.log |
| S03.switch-profile | pass | 722e5d403cf7 | bullet 14: pass; bullet 21: blocked (block 1 is blocked (exit 3: a missing prerequisite)); bullet 23: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S03/transcripts/S03-llm-routing-profiles-14.log |
| S04.arun-interrupt | pass | 722e5d403cf7 | bullet 14: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-14.log |
| S04.arun-pause-persisted | pass | 722e5d403cf7 | bullet 15: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-15.log |
| S04.ask-agent-usage-saved | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-05.log |
| S04.async-callback | pass | 722e5d403cf7 | bullet 13: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-13.log |
| S04.callbacks | pass | 722e5d403cf7 | bullet 2: pass; bullet 8: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | 722e5d403cf7 | bullet 16: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-16.log |
| S04.close | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-10.log |
| S04.conversation-id | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-01.log |
| S04.conversation-sender | pass | 722e5d403cf7 | bullet 28: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-28.log |
| S04.custom-file-store | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-07.log |
| S04.factory | pass | 722e5d403cf7 | bullet 1: pass; bullet 31: pass; bullet 35: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | 722e5d403cf7 | bullet 26: pass; bullet 31: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-26.log |
| S04.fork | pass | 722e5d403cf7 | bullet 19: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-19.log |
| S04.fork-branch | pass | 722e5d403cf7 | bullet 21: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-21.log |
| S04.fork-keeps-secrets | pass | 722e5d403cf7 | bullet 20: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-20.log |
| S04.goal-asked | pass | 722e5d403cf7 | bullet 23: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-23.log |
| S04.goal-loop | pass | 722e5d403cf7 | bullet 22: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-22.log |
| S04.pause | pass | 722e5d403cf7 | bullet 11: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-11.log |
| S04.persist-events | pass | 722e5d403cf7 | bullet 2: pass; bullet 3: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-02.log |
| S04.resolution-judge | pass | 722e5d403cf7 | bullet 30: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-30.log |
| S04.resolution-verdict | pass | 722e5d403cf7 | bullet 29: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-29.log |
| S04.resume | pass | 722e5d403cf7 | bullet 2: pass; bullet 4: pass; bullet 31: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-06.log |
| S04.run-error | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-09.log |
| S04.secrets-constructor | pass | 722e5d403cf7 | bullet 17: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-masking | pass | 722e5d403cf7 | bullet 17: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-17.log |
| S04.secrets-update | pass | 722e5d403cf7 | bullet 17: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-17.log |
| S04.stats | pass | 722e5d403cf7 | bullet 27: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-27.log |
| S04.title-and-tags | pass | 722e5d403cf7 | bullet 26: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-26.log |
| S04.visualizer-custom | pass | 722e5d403cf7 | bullet 18: pass; bullet 33: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-18.log |
| S04.visualizer-default | pass | 722e5d403cf7 | bullet 18: pass; bullet 32: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-18.log |
| S05.completion-log-event | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-02.log |
| S05.event-base | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.event-cache | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.event-log-append | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-05.log |
| S05.event-log-files | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.event-log-recovery | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B1-S04/transcripts/S04-local-conversation-03.log |
| S05.event-tree | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.json-roundtrip | pass | 722e5d403cf7 | bullet 1: pass; bullet 7: pass; bullet 8: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.openai-format | pass | 722e5d403cf7 | bullet 1: pass; bullet 7: pass; bullet 8: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.resume-transcript | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.streaming-delta | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-02.log |
| S05.system-prompt-blocks | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-10.log |
| S05.to-llm-message | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.unmatched-actions | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S05.visualize | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S05/transcripts/S05-events-01.log |
| S06.condenser-resume | pass | 722e5d403cf7 | bullet 13: pass; bullet 16: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-13.log |
| S06.context-datetime | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-01.log |
| S06.context-secrets | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-01.log |
| S06.context-skills | pass | 722e5d403cf7 | bullet 1: pass; bullet 18: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-01.log |
| S06.context-suffixes | pass | 722e5d403cf7 | bullet 1: pass; bullet 18: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-01.log |
| S06.manual-condense | pass | 722e5d403cf7 | bullet 11: pass; bullet 15: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-11.log |
| S06.memory-load | pass | 722e5d403cf7 | bullet 3: pass; bullet 17: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-03.log |
| S06.memory-write-path | pass | 722e5d403cf7 | bullet 3: pass; bullet 17: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-03.log |
| S06.noop-condenser | pass | 722e5d403cf7 | bullet 6: pass; bullet 14: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-06.log |
| S06.observation-dispositions | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-07.log |
| S06.persona-soul | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-02.log |
| S06.pipeline-condenser | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-14.log |
| S06.summarizing-reasons | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-06.log |
| S06.summary-llm-streaming | pass | 722e5d403cf7 | bullet 4: pass; bullet 16: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-04.log |
| S06.system-prompt-custom | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-model-specific | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-registry | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-02.log |
| S06.view | pass | 722e5d403cf7 | bullet 4: pass; bullet 6: pass | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-04.log |
| S06.view-atomicity | pass | 722e5d403cf7 | bullet 4: pass; bullet 15: pass; bullet 20: blocked (bullet is labeled blocked) | <scratch>/sdk/B1-S06/transcripts/S06-context-condensers-04.log |
| S07.agentskills-load | pass | 722e5d403cf7 | bullet 2: pass; bullet 13: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.agentskills-trigger | pass | 722e5d403cf7 | bullet 2: pass; bullet 13: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.disable-model-invocation | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.disabled-skills | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-05.log |
| S07.inline-commands | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-autoattach | pass | 722e5d403cf7 | bullet 2: pass; bullet 11: pass; bullet 13: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.keyword-trigger | pass | 722e5d403cf7 | bullet 1: pass; bullet 12: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.load-project-flag | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-05.log |
| S07.marketplace-install | pass | 722e5d403cf7 | bullet 6: pass; bullet 7: pass; bullet 15: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-06.log |
| S07.merge-precedence | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-05.log |
| S07.message-suffixes | pass | 722e5d403cf7 | bullet 1: pass; bullet 12: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.path-rules | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-04.log |
| S07.project-skills | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-05.log |
| S07.public-skills | pass | 722e5d403cf7 | bullet 8: pass; bullet 9: pass; bullet 12: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-08.log |
| S07.public-skills-switch | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-10.log |
| S07.repo-skill-always-on | pass | 722e5d403cf7 | bullet 1: pass; bullet 12: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.resources | pass | 722e5d403cf7 | bullet 2: pass; bullet 13: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.serialization | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.skill-mcp-json | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-02.log |
| S07.task-trigger | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.trigger-once | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-01.log |
| S07.user-skills | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S07/transcripts/S07-skills-05.log |
| S08.agent-plugins-mcp | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.ambient-plugins | pass | 722e5d403cf7 | bullet 2: pass; bullet 7: pass; bullet 8: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.claude-code-layout | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.commands-as-skills | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.fetch-cache | pass | 722e5d403cf7 | bullet 4: pass; bullet 5: pass; bullet 6: pass; bullet 16: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-04.log |
| S08.installation-manager | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-10.log |
| S08.installed-plugins | pass | 722e5d403cf7 | bullet 7: pass; bullet 9: pass; bullet 16: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-07.log |
| S08.load-plugin-runtime | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-14.log |
| S08.marketplace-auto-load | pass | 722e5d403cf7 | bullet 13: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-13.log |
| S08.marketplace-import-path | pass | 722e5d403cf7 | bullet 15: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-15.log |
| S08.marketplace-manifest | pass | 722e5d403cf7 | bullet 11: pass; bullet 18: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-11.log |
| S08.marketplace-registry | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-12.log |
| S08.merge-semantics | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.path-containment | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S08.plugin-agents | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.resolved-refs | pass | 722e5d403cf7 | bullet 2: pass; bullet 16: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-02.log |
| S08.source-parsing | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S08/transcripts/S08-plugins-marketplace-01.log |
| S09.argument-validation | pass | 722e5d403cf7 | bullet 1: pass; bullet 14: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-14.log |
| S09.config-secrets | pass | 722e5d403cf7 | bullet 1: pass; bullet 14: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-05.log |
| S09.filter-tools-regex | pass | 722e5d403cf7 | bullet 2: pass; bullet 17: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-07.log |
| S09.listing-timeout | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-06.log |
| S09.oauth | pass | 722e5d403cf7 | bullet 10: pass; bullet 11: blocked (bullet is labeled blocked) | <scratch>/sdk/B2-S09/transcripts/S09-mcp-10.log |
| S09.protocol-negotiation | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-08.log |
| S09.runtime-add-resume | pass | 722e5d403cf7 | bullet 19: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-19.log |
| S09.runtime-add-servers | pass | 722e5d403cf7 | bullet 18: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-18.log |
| S09.schema-conversion | pass | 722e5d403cf7 | bullet 1: pass; bullet 14: pass; bullet 16: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | 722e5d403cf7 | bullet 1: pass; bullet 16: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.startup-budget | pass | 722e5d403cf7 | bullet 20: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-20.log |
| S09.static-auth | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-09.log |
| S09.stdio-server | pass | 722e5d403cf7 | bullet 1: pass; bullet 7: pass; bullet 16: pass; bullet 17: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-14.log |
| S09.tools-list-changed | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/B2-S09/transcripts/S09-mcp-01.log |
| S10.agent-hook | pass | 722e5d403cf7 | bullet 5: pass; bullet 9: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-05.log |
| S10.async-hooks | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.blocked-state-persistence | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-02.log |
| S10.config-discovery | pass | 722e5d403cf7 | bullet 1: pass; bullet 4: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.config-format | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-04.log |
| S10.definition-validation | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-04.log |
| S10.execution-events | pass | 722e5d403cf7 | bullet 1: pass; bullet 9: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.exit-codes | pass | 722e5d403cf7 | bullet 1: pass; bullet 4: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.llm-follows-switch | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-05.log |
| S10.matcher | pass | 722e5d403cf7 | bullet 1: pass; bullet 4: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.plugin-hooks-merge | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-06.log |
| S10.plugin-hooks-reload-once | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-07.log |
| S10.post-tool-use | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.pre-tool-use-block | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.prompt-hook | pass | 722e5d403cf7 | bullet 5: pass; bullet 10: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-05.log |
| S10.session-end-on-close | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.session-start | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.stop-hook | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass; bullet 9: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S10.user-prompt-block | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-02.log |
| S10.user-prompt-context | pass | 722e5d403cf7 | bullet 1: pass; bullet 8: pass | <scratch>/sdk/B2-S10/transcripts/S10-hooks-01.log |
| S11.builtin-agents | pass | 722e5d403cf7 | bullet 7: pass; bullet 9: pass; bullet 15: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-07.log |
| S11.conversation-autoregister | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-09.log |
| S11.definition-factory | pass | 722e5d403cf7 | bullet 6: pass; bullet 16: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.definition-model | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.delegation-visualizer | pass | 722e5d403cf7 | bullet 13: pass; bullet 14: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-13.log |
| S11.factory-info | pass | 722e5d403cf7 | bullet 7: pass; bullet 8: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-07.log |
| S11.file-discovery | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.file-precedence | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.markdown-schema | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.plugin-agents | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.register-if-absent | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-06.log |
| S11.register-programmatic | pass | 722e5d403cf7 | bullet 1: pass; bullet 6: pass; bullet 15: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.sub-agent-scope | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-12.log |
| S11.task-errors | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-hooks | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-limits | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-metrics | pass | 722e5d403cf7 | bullet 1: pass; bullet 15: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-run | pass | 722e5d403cf7 | bullet 1: pass; bullet 14: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-secrets | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B2-S11/transcripts/S11-subagents-delegation-04.log |
| S13.analysis-event | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-approve-reject | pass | 722e5d403cf7 | bullet 1: pass; bullet 6: pass; bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-wait | pass | 722e5d403cf7 | bullet 1: pass; bullet 6: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.ensemble | pass | 722e5d403cf7 | bullet 2: pass; bullet 8: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.grayswan | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.llm-analyzer | pass | 722e5d403cf7 | bullet 1: pass; bullet 6: pass; bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.mask-async | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-04.log |
| S13.mask-models | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-output | pass | 722e5d403cf7 | bullet 3: pass; bullet 9: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-thinking | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-05.log |
| S13.mask-tool-output | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.pattern-analyzer | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.policies | pass | 722e5d403cf7 | bullet 2: pass; bullet 8: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.policy-rails | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.risk-extraction | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.risk-levels | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.secret-injection | pass | 722e5d403cf7 | bullet 3: pass; bullet 9: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-registry | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-sources | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-03.log |
| S13.security-policy-prompt | pass | 722e5d403cf7 | bullet 1: pass; bullet 7: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-01.log |
| S13.settings-security | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S13.toolshield | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B2-S13/transcripts/S13-security-confirmation-02.log |
| S15.action-routing | pass | 722e5d403cf7 | bullet 1: pass; bullet 6: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.cleanup | pass | 722e5d403cf7 | bullet 1: pass; bullet 4: pass; bullet 6: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.executor-config | pass | 722e5d403cf7 | bullet 5: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-05.log |
| S15.observation | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.preset-browser | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-08.log |
| S15.prompt-guidance | pass | 722e5d403cf7 | bullet 1: pass; bullet 3: blocked (block 1 is blocked (exit 3: a missing prerequisite)) | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.recording-start-stop | pass | 722e5d403cf7 | bullet 1: pass; bullet 7: blocked (bullet is labeled blocked); bullet 10: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.session-recovery | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-06.log |
| S15.shared-executor | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-04.log |
| S15.storage | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.tabs | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S15.toolset-create | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S15/transcripts/S15-browser-01.log |
| S17.agent-tool-init | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-06.log |
| S17.annotations-and-resources | pass | 722e5d403cf7 | bullet 1: pass; bullet 3: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.auto-naming | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.auto-registration | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.catalog | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.client-tool-ack | pass | 722e5d403cf7 | bullet 7: pass; bullet 10: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-registration | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tool-schema | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-spec | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tools-conversation | pass | 722e5d403cf7 | bullet 7: pass; bullet 8: pass; bullet 10: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.custom-tool-definition | pass | 722e5d403cf7 | bullet 1: pass; bullet 3: pass; bullet 9: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.execute-tool | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.injected-fields | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.llm-schemas | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.module-qualnames | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.output-coercion | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.py-type | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.register-tool | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.resolve-tool | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.schema-serialization | pass | 722e5d403cf7 | bullet 3: pass; bullet 5: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.tool-set | pass | 722e5d403cf7 | bullet 1: pass; bullet 9: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.tool-spec | pass | 722e5d403cf7 | bullet 1: pass; bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.usability | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S17/transcripts/S17-custom-and-client-tools-02.log |
| S19.acp-providers-catalog | pass | 722e5d403cf7 | bullet 4: pass; bullet 5: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-04.log |
| S19.acp-settings | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.apply-diff | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.condenser-settings | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.conversation-settings | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.credential-binding | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-10.log |
| S19.mcp-config-secrets | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.persisted-baselines | pass | 722e5d403cf7 | bullet 6: pass; bullet 7: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-06.log |
| S19.profile-migrations | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.profile-model | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.profile-refs | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.profile-resolve | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.profile-sandbox | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-09.log |
| S19.profile-seed | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.profile-store | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-08.log |
| S19.pypi-baseline-gate | pass | 722e5d403cf7 | bullet 7: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-07.log |
| S19.retired-switches | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.schema-export | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.schema-migrations | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.settings-create-agent | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.settings-roundtrip | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.settings-tools | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.subscription-llm-settings | pass | 722e5d403cf7 | bullet 2: pass; bullet 3: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.tool-concurrency-persona | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S19.validate-dispatch | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-02.log |
| S19.verification-settings | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S19/transcripts/S19-settings-01.log |
| S20.automation-context | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-08.log |
| S20.automation-headers | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-08.log |
| S20.automation-kwargs | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-08.log |
| S20.conversation-args | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-01.log |
| S20.delegate-trace | pass | 722e5d403cf7 | bullet 6: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-06.log |
| S20.env-conversation-defaults | pass | 722e5d403cf7 | bullet 2: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-02.log |
| S20.get-env | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-08.log |
| S20.laminar-init | pass | 722e5d403cf7 | bullet 3: pass; bullet 12: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S20/transcripts/S20-observability-03.log |
| S20.llm-retry-log | pass | 722e5d403cf7 | bullet 10: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-10.log |
| S20.llm-span | pass | 722e5d403cf7 | bullet 4: pass; bullet 11: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-04.log |
| S20.llm-span-content | pass | 722e5d403cf7 | bullet 5: pass; bullet 11: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-05.log |
| S20.logger-config | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-09.log |
| S20.logger-quiet-thirdparty | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-09.log |
| S20.otel-backend | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-01.log |
| S20.parallel-span-context | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-01.log |
| S20.rolling-log-view | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-09.log |
| S20.root-span | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass; bullet 12: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S20/transcripts/S20-observability-01.log |
| S20.step-and-tool-spans | pass | 722e5d403cf7 | bullet 1: pass; bullet 11: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-01.log |
| S20.utility-operation-metadata | pass | 722e5d403cf7 | bullet 4: pass | <scratch>/sdk/B3-S20/transcripts/S20-observability-04.log |
| S21.ask-agent | pass | 722e5d403cf7 | bullet 2: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-02.log |
| S21.auth-selection | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-09.log |
| S21.cancel-pause | pass | 722e5d403cf7 | bullet 8: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-08.log |
| S21.cleanup | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.construct | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.effort | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-11.log |
| S21.effort-switch | pass | 722e5d403cf7 | bullet 11: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-11.log |
| S21.file-secrets | pass | 722e5d403cf7 | bullet 9: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-09.log |
| S21.handshake-live | pass | 722e5d403cf7 | bullet 14: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-14.log |
| S21.init-state | pass | 722e5d403cf7 | bullet 1: pass; bullet 4: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.masking | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.mcp-forwarding | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.model-discovery | pass | 722e5d403cf7 | bullet 10: pass; bullet 11: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-10.log |
| S21.model-selection | pass | 722e5d403cf7 | bullet 1: pass; bullet 3: pass; bullet 9: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.model-switch | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.permissions-auto-approve | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.provider-registry | pass | 722e5d403cf7 | bullet 13: pass; bullet 14: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-13.log |
| S21.secrets-env | pass | 722e5d403cf7 | bullet 1: pass; bullet 9: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.session-resume | pass | 722e5d403cf7 | bullet 3: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-03.log |
| S21.settings | pass | 722e5d403cf7 | bullet 10: pass; bullet 11: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-10.log |
| S21.step | pass | 722e5d403cf7 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.tool-call-events | pass | 722e5d403cf7 | bullet 1: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
| S21.tracing | pass | 722e5d403cf7 | bullet 12: pass | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-12.log |
| S21.usage-cost | pass | 722e5d403cf7 | bullet 1: pass; bullet 15: blocked (bullet is labeled blocked) | <scratch>/sdk/B3-S21/transcripts/S21-acp-agent-01.log |
