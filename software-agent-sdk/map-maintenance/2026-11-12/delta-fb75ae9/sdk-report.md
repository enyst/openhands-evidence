## Conflicting attempts

- S11.definition-factory: fail at 2026-11-12T15:01:57+00:00, pass at 2026-11-12T15:19:17+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S03.registry-stats-wiring | fail | 106217297f4c | bullet 1: pass; bullet 2: fail (block 1 exited 1); bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-02.log |
| S04.interactive-terminal | fail | 106217297f4c | bullet 19: fail (block 1 exited 1); bullet 25: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-19.log |
| S07.installed-lifecycle | fail | 106217297f4c | bullet 6: pass; bullet 13: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-13.log |
| S08.secret-expansion | fail | 106217297f4c | bullet 3: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-03.log |
| S09.session-recovery | fail | 106217297f4c | bullet 10: pass; bullet 11: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-11.log |
| S11.task-observability | fail | 031dcf31879c | bullet 2: fail (block 1 exited 1); bullet 4: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-02.log |
| S11.task-secrets | fail | 031dcf31879c | bullet 3: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-03.log |
| S17.schema-constraints | fail | ab93d923b3d0 | bullet 4: fail (block 1 exited 1) | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-04.log |
| S01.ask-agent | pass | 106217297f4c | bullet 17: pass; bullet 20: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-17.log |
| S01.async-step | pass | 106217297f4c | bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-15.log |
| S01.content-policy | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.context-overflow | pass | 106217297f4c | bullet 19: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-19.log |
| S01.empty-reply-nudge | pass | 106217297f4c | bullet 3: pass; bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.finish-truncates-batch | pass | 106217297f4c | bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.image-input | pass | 106217297f4c | bullet 16: pass; bullet 24: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.image-non-vision | pass | 106217297f4c | bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-16.log |
| S01.iterative-refinement | pass | 106217297f4c | bullet 22: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-22.log |
| S01.malformed-tool-call | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-03.log |
| S01.max-budget | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01-rerun-maxbudget/transcripts/S01-agent-loop-06.log |
| S01.max-iterations | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-05.log |
| S01.message-while-running | pass | 106217297f4c | bullet 14: pass; bullet 15: pass; bullet 21: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-14.log |
| S01.parallel-resource-locks | pass | 106217297f4c | bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-12.log |
| S01.parallel-tools | pass | 106217297f4c | bullet 11: pass; bullet 21: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-11.log |
| S01.response-dispatch | pass | 106217297f4c | bullet 1: pass; bullet 2: pass; bullet 20: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.run-to-finish | pass | 106217297f4c | bullet 1: pass; bullet 20: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-01.log |
| S01.structured-output | pass | 106217297f4c | bullet 18: pass; bullet 21: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-18.log |
| S01.stuck-detect | pass | 106217297f4c | bullet 7: pass; bullet 21: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-07.log |
| S01.stuck-nudge | pass | 106217297f4c | bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-10.log |
| S01.stuck-recover | pass | 106217297f4c | bullet 7: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-07.log |
| S01.stuck-thresholds | pass | 106217297f4c | bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-09.log |
| S01.tool-exception | pass | 106217297f4c | bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-13.log |
| S01.unknown-tool | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S01/transcripts/S01-agent-loop-03.log |
| S03.agent-llm-discovery | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-03.log |
| S03.fallback-metrics | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-profile-resolution | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-skip | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.fallback-transient | pass | 106217297f4c | bullet 6: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-06.log |
| S03.meta-profile-store | pass | 106217297f4c | bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-13.log |
| S03.multimodal-router-images | pass | 106217297f4c | bullet 4: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.multimodal-router-text | pass | 106217297f4c | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-04.log |
| S03.profile-concurrency-limits | pass | 106217297f4c | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-migration | pass | 106217297f4c | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-save-load | pass | 106217297f4c | bullet 7: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.profile-secrets | pass | 106217297f4c | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-07.log |
| S03.provider-connections | pass | 106217297f4c | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-08.log |
| S03.random-router | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.registry-crud | pass | 106217297f4c | bullet 1: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.registry-independent-metrics | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-01.log |
| S03.route-task-to-model | pass | 106217297f4c | bullet 12: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-12.log |
| S03.router-validation | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-05.log |
| S03.subscription-login | pass | 106217297f4c | bullet 14: pass; bullet 18: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.subscription-requests | pass | 106217297f4c | bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-14.log |
| S03.switch-llm-object | pass | 106217297f4c | bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-10.log |
| S03.switch-llm-tool | pass | 106217297f4c | bullet 11: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-11.log |
| S03.switch-profile | pass | 106217297f4c | bullet 9: pass; bullet 15: pass; bullet 17: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S03/transcripts/S03-llm-routing-profiles-09.log |
| S04.arun-interrupt | pass | 106217297f4c | bullet 12: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-12.log |
| S04.async-callback | pass | 106217297f4c | bullet 11: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-11.log |
| S04.callbacks | pass | 106217297f4c | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.cancel-token | pass | 106217297f4c | bullet 13: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-13.log |
| S04.close | pass | 106217297f4c | bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-09.log |
| S04.conversation-id | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.custom-file-store | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-06.log |
| S04.factory | pass | 106217297f4c | bullet 1: pass; bullet 22: pass; bullet 26: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-01.log |
| S04.final-response | pass | 106217297f4c | bullet 20: pass; bullet 22: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-20.log |
| S04.fork | pass | 106217297f4c | bullet 16: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-16.log |
| S04.fork-branch | pass | 106217297f4c | bullet 17: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-17.log |
| S04.goal-loop | pass | 106217297f4c | bullet 18: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-18.log |
| S04.pause | pass | 106217297f4c | bullet 10: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-10.log |
| S04.persist-events | pass | 106217297f4c | bullet 2: pass; bullet 3: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume | pass | 106217297f4c | bullet 2: pass; bullet 4: pass; bullet 22: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-02.log |
| S04.resume-agent-compat | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-05.log |
| S04.run-error | pass | 106217297f4c | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-08.log |
| S04.secrets-constructor | pass | 106217297f4c | bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.secrets-masking | pass | 106217297f4c | bullet 14: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.secrets-update | pass | 106217297f4c | bullet 14: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-14.log |
| S04.stats | pass | 106217297f4c | bullet 21: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-21.log |
| S04.title-and-tags | pass | 106217297f4c | bullet 20: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-20.log |
| S04.visualizer-custom | pass | 106217297f4c | bullet 15: pass; bullet 24: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-15.log |
| S04.visualizer-default | pass | 106217297f4c | bullet 15: pass; bullet 23: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-15.log |
| S05.event-log-recovery | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S04/transcripts/S04-local-conversation-03.log |
| S06.condenser-resume | pass | 106217297f4c | bullet 12: pass; bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-12.log |
| S06.context-datetime | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-overflow-request | pass | 106217297f4c | bullet 11: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-11.log |
| S06.context-secrets | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-skills | pass | 106217297f4c | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.context-suffixes | pass | 106217297f4c | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-01.log |
| S06.hard-reset | pass | 106217297f4c | bullet 9: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-09.log |
| S06.manual-condense | pass | 106217297f4c | bullet 10: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-10.log |
| S06.memory-load | pass | 106217297f4c | bullet 3: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.memory-write-path | pass | 106217297f4c | bullet 3: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-03.log |
| S06.noop-condenser | pass | 106217297f4c | bullet 6: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.observation-dispositions | pass | 106217297f4c | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-07.log |
| S06.persona-soul | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.pipeline-condenser | pass | 106217297f4c | bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-13.log |
| S06.soft-vs-hard | pass | 106217297f4c | bullet 8: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-08.log |
| S06.summarizing-reasons | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-06.log |
| S06.summarizing-size | pass | 106217297f4c | bullet 4: pass; bullet 14: pass; bullet 15: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.summarizing-tokens | pass | 106217297f4c | bullet 5: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-05.log |
| S06.summary-llm-streaming | pass | 106217297f4c | bullet 4: pass; bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.system-prompt-custom | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-model-specific | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.system-prompt-registry | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-02.log |
| S06.view | pass | 106217297f4c | bullet 4: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-04.log |
| S06.view-atomicity | pass | 106217297f4c | bullet 4: pass; bullet 14: pass; bullet 19: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S06/transcripts/S06-context-condensers-04.log |
| S07.agentskills-load | pass | 106217297f4c | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.agentskills-trigger | pass | 106217297f4c | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.available-skills-prompt | pass | 106217297f4c | bullet 2: pass; bullet 3: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.disable-model-invocation | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.disabled-skills | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-05.log |
| S07.inline-commands | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-autoattach | pass | 106217297f4c | bullet 2: pass; bullet 10: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.invoke-skill-run | pass | 106217297f4c | bullet 2: pass; bullet 10: pass; bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.keyword-trigger | pass | 106217297f4c | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.load-project-flag | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-05.log |
| S07.marketplace-install | pass | 106217297f4c | bullet 6: pass; bullet 7: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-06.log |
| S07.merge-precedence | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-05.log |
| S07.message-suffixes | pass | 106217297f4c | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.path-rules | pass | 106217297f4c | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-04.log |
| S07.project-skills | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-05.log |
| S07.public-skills | pass | 106217297f4c | bullet 8: pass; bullet 9: pass; bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-08.log |
| S07.repo-skill-always-on | pass | 106217297f4c | bullet 1: pass; bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.resources | pass | 106217297f4c | bullet 2: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.serialization | pass | 106217297f4c | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.skill-mcp-json | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-02.log |
| S07.task-trigger | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.trigger-once | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-01.log |
| S07.user-skills | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S07/transcripts/S07-skills-05.log |
| S08.agent-plugins-layout | pass | 106217297f4c | bullet 1: pass; bullet 17: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.agent-plugins-mcp | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.ambient-plugins | pass | 106217297f4c | bullet 2: pass; bullet 7: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.claude-code-layout | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.commands-as-skills | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.conversation-attach | pass | 106217297f4c | bullet 2: pass; bullet 4: pass; bullet 16: pass; bullet 17: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.fetch-cache | pass | 106217297f4c | bullet 4: pass; bullet 5: pass; bullet 6: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-04.log |
| S08.installation-manager | pass | 106217297f4c | bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-10.log |
| S08.installed-plugins | pass | 106217297f4c | bullet 7: pass; bullet 9: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-07.log |
| S08.load-plugin-runtime | pass | 106217297f4c | bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-14.log |
| S08.marketplace-auto-load | pass | 106217297f4c | bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-13.log |
| S08.marketplace-import-path | pass | 106217297f4c | bullet 15: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-15.log |
| S08.marketplace-manifest | pass | 106217297f4c | bullet 11: pass; bullet 18: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-11.log |
| S08.marketplace-registry | pass | 106217297f4c | bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-12.log |
| S08.merge-semantics | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.path-containment | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S08.plugin-agents | pass | 106217297f4c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.resolved-refs | pass | 106217297f4c | bullet 2: pass; bullet 16: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-02.log |
| S08.source-parsing | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S08/transcripts/S08-plugins-marketplace-01.log |
| S09.argument-validation | pass | 106217297f4c | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-model | pass | 106217297f4c | bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-12.log |
| S09.config-secrets | pass | 106217297f4c | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.config-var-expansion | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.enabled-flag | pass | 106217297f4c | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-04.log |
| S09.filter-tools-regex | pass | 106217297f4c | bullet 2: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-02.log |
| S09.http-sse-server | pass | 106217297f4c | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-06.log |
| S09.listing-timeout | pass | 106217297f4c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-05.log |
| S09.oauth | pass | 106217297f4c | bullet 8: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-08.log |
| S09.observation | pass | 106217297f4c | bullet 1: pass; bullet 12: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.schema-conversion | pass | 106217297f4c | bullet 1: pass; bullet 12: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.secret-refs-in-calls | pass | 106217297f4c | bullet 1: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.session-reuse | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.startup-failure-tolerated | pass | 106217297f4c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-03.log |
| S09.static-auth | pass | 106217297f4c | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-07.log |
| S09.stdio-server | pass | 106217297f4c | bullet 1: pass; bullet 6: pass; bullet 13: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S09.tool-serialization | pass | 106217297f4c | bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-12.log |
| S09.tools-list-changed | pass | 106217297f4c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S09/transcripts/S09-mcp-01.log |
| S10.agent-hook | pass | 031dcf31879c | bullet 4: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-04.log |
| S10.async-hooks | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.blocked-state-persistence | pass | 031dcf31879c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-02.log |
| S10.command-exec | pass | 031dcf31879c | bullet 1: pass; bullet 3: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-discovery | pass | 031dcf31879c | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.config-format | pass | 031dcf31879c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-03.log |
| S10.definition-validation | pass | 031dcf31879c | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-03.log |
| S10.execution-events | pass | 031dcf31879c | bullet 1: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.exit-codes | pass | 031dcf31879c | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.llm-follows-switch | pass | 031dcf31879c | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-04.log |
| S10.matcher | pass | 031dcf31879c | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.plugin-hooks-merge | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-05.log |
| S10.post-tool-use | pass | 031dcf31879c | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.pre-tool-use-block | pass | 031dcf31879c | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.prompt-hook | pass | 031dcf31879c | bullet 4: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-04.log |
| S10.session-end-on-close | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.session-start | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.stop-hook | pass | 031dcf31879c | bullet 1: pass; bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S10.user-prompt-block | pass | 031dcf31879c | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-02.log |
| S10.user-prompt-context | pass | 031dcf31879c | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S10/transcripts/S10-hooks-01.log |
| S11.builtin-agents | pass | 031dcf31879c | bullet 6: pass; bullet 8: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-06.log |
| S11.conversation-autoregister | pass | 031dcf31879c | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-08.log |
| S11.definition-factory | pass | ab93d923b3d0 | bullet 5: pass; bullet 14: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11-rerun-defactory/transcripts/S11-subagents-delegation-05.log |
| S11.definition-model | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.delegate-executor | pass | 031dcf31879c | bullet 11: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.delegation-visualizer | pass | 031dcf31879c | bullet 11: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-11.log |
| S11.factory-info | pass | 031dcf31879c | bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-06.log |
| S11.file-discovery | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.file-precedence | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.markdown-schema | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.plugin-agents | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-if-absent | pass | 031dcf31879c | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-05.log |
| S11.register-programmatic | pass | 031dcf31879c | bullet 1: pass; bullet 5: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.sub-agent-scope | pass | 031dcf31879c | bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-10.log |
| S11.task-confirmation | pass | 031dcf31879c | bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-09.log |
| S11.task-errors | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-hooks | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-limits | pass | 031dcf31879c | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-metrics | pass | 031dcf31879c | bullet 1: pass; bullet 13: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-persistence | pass | 031dcf31879c | bullet 1: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-resume | pass | 031dcf31879c | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S11.task-run | pass | 031dcf31879c | bullet 1: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S11/transcripts/S11-subagents-delegation-01.log |
| S13.analysis-event | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-approve-reject | pass | ab93d923b3d0 | bullet 1: pass; bullet 5: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.confirm-wait | pass | ab93d923b3d0 | bullet 1: pass; bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.ensemble | pass | ab93d923b3d0 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.grayswan | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.llm-analyzer | pass | ab93d923b3d0 | bullet 1: pass; bullet 5: pass; bullet 9: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.mask-async | pass | ab93d923b3d0 | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-04.log |
| S13.mask-models | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-output | pass | ab93d923b3d0 | bullet 3: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.mask-tool-output | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.pattern-analyzer | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policies | pass | ab93d923b3d0 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.policy-rails | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.risk-extraction | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.risk-levels | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.secret-injection | pass | ab93d923b3d0 | bullet 3: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-registry | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.secret-sources | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-03.log |
| S13.security-policy-prompt | pass | ab93d923b3d0 | bullet 1: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-01.log |
| S13.settings-security | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S13.toolshield | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S13/transcripts/S13-security-confirmation-02.log |
| S16.oracle-consult | pass | ab93d923b3d0 | bullet 4: pass; bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-errors | pass | ab93d923b3d0 | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.oracle-tool | pass | ab93d923b3d0 | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-04.log |
| S16.plan-edit-restriction | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-headers | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-file-location | pass | ab93d923b3d0 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.plan-then-execute | pass | ab93d923b3d0 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-agent | pass | ab93d923b3d0 | bullet 2: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.planning-tools | pass | ab93d923b3d0 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-02.log |
| S16.reactions | pass | ab93d923b3d0 | bullet 11: pass; bullet 12: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-11.log |
| S16.task-tracker-persistence | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.task-tracker-plan-view | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-01.log |
| S16.tom-consult | pass | ab93d923b3d0 | bullet 5: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-sleeptime | pass | ab93d923b3d0 | bullet 5: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.tom-storage-root | pass | ab93d923b3d0 | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-05.log |
| S16.workflow-errors-and-output | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-fan-out | pass | ab93d923b3d0 | bullet 6: pass; bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-lifecycle | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-pipeline | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-script-validation | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S16.workflow-toolset | pass | ab93d923b3d0 | bullet 6: pass; bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S16/transcripts/S16-planning-workflow-tools-06.log |
| S17.agent-tool-init | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-06.log |
| S17.annotations-and-resources | pass | ab93d923b3d0 | bullet 1: pass; bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.auto-naming | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.auto-registration | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.catalog | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.client-tool-ack | pass | ab93d923b3d0 | bullet 7: pass; bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-registration | pass | ab93d923b3d0 | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tool-schema | pass | ab93d923b3d0 | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.client-tool-spec | pass | ab93d923b3d0 | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-08.log |
| S17.client-tools-conversation | pass | ab93d923b3d0 | bullet 7: pass; bullet 8: pass; bullet 10: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-07.log |
| S17.custom-tool-definition | pass | ab93d923b3d0 | bullet 1: pass; bullet 3: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.execute-tool | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.injected-fields | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.llm-schemas | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.module-qualnames | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.output-coercion | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.py-type | pass | ab93d923b3d0 | bullet 3: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.register-tool | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S17.resolve-tool | pass | ab93d923b3d0 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.schema-serialization | pass | ab93d923b3d0 | bullet 3: pass; bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-03.log |
| S17.tool-set | pass | ab93d923b3d0 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.tool-spec | pass | ab93d923b3d0 | bullet 1: pass; bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-01.log |
| S17.usability | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S17/transcripts/S17-custom-and-client-tools-02.log |
| S20.automation-context | pass | ab93d923b3d0 | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-07.log |
| S20.automation-headers | pass | ab93d923b3d0 | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-07.log |
| S20.automation-kwargs | pass | ab93d923b3d0 | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-07.log |
| S20.conversation-args | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.delegate-trace | pass | ab93d923b3d0 | bullet 5: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-05.log |
| S20.enable-gate | pass | ab93d923b3d0 | bullet 1: pass; bullet 3: pass; bullet 6: pass; bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.env-conversation-defaults | pass | ab93d923b3d0 | bullet 2: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-02.log |
| S20.external-entry | pass | ab93d923b3d0 | bullet 2: pass; bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-02.log |
| S20.get-env | pass | ab93d923b3d0 | bullet 7: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-07.log |
| S20.laminar-init | pass | ab93d923b3d0 | bullet 3: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-03.log |
| S20.lazy-import | pass | ab93d923b3d0 | bullet 6: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-06.log |
| S20.llm-span | pass | ab93d923b3d0 | bullet 4: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-04.log |
| S20.logger-config | pass | ab93d923b3d0 | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-08.log |
| S20.logger-quiet-thirdparty | pass | ab93d923b3d0 | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-08.log |
| S20.otel-backend | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.parallel-span-context | pass | ab93d923b3d0 | bullet 1: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.rolling-log-view | pass | ab93d923b3d0 | bullet 8: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-08.log |
| S20.root-span | pass | ab93d923b3d0 | bullet 1: pass; bullet 9: pass; bullet 10: blocked (bullet is labeled blocked) | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.step-and-tool-spans | pass | ab93d923b3d0 | bullet 1: pass; bullet 9: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-01.log |
| S20.utility-operation-metadata | pass | ab93d923b3d0 | bullet 4: pass | /tmp/claude-0/scratch/runs2/D2S/sdk/S20/transcripts/S20-observability-04.log |
