## Conflicting attempts

- S14.glob: pass at 2026-11-22T08:27:17+00:00, fail at 2026-11-22T08:31:43+00:00, fail at 2026-11-22T08:32:44+00:00

## Checks

| Feature | Result | Revision | Note | Transcript |
|---|---|---|---|---|
| S14.glob | fail | 74f198df3650 | bullet 1: pass; bullet 13: pass; bullet 14: pass; bullet 15: fail (block 1 exited 1) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14-glob/transcripts/S14-core-tools-15.log |
| S14.terminal-backend-select | fail | 74f198df3650 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-06.log |
| S14.terminal-exec | fail | 74f198df3650 | bullet 1: pass; bullet 2: pass; bullet 3: pass; bullet 8: fail (block 1 exited 1); bullet 16: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)); bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-08.log |
| S14.terminal-input-encoding | fail | 74f198df3650 | bullet 2: pass; bullet 3: pass; bullet 5: fail (block 1 exited 1) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14-edit/transcripts/S14-core-tools-05.log |
| S14.terminal-reset | fail | 74f198df3650 | bullet 2: pass; bullet 3: pass; bullet 6: fail (block 1 exited 1) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-06.log |
| S14.terminal-timeout | fail | 74f198df3650 | bullet 2: pass; bullet 3: pass; bullet 7: fail (block 1 exited 1) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-07.log |
| S14.terminal-windows | blocked | 74f198df3650 | bullet 11: blocked (bullet is labeled blocked) |  |
| S14.apply-patch | pass | 74f198df3650 | bullet 1: pass; bullet 13: pass; bullet 15: pass; bullet 17: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)); bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-01.log |
| S14.file-editor-edit | pass | 74f198df3650 | bullet 12: pass; bullet 16: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)); bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-12.log |
| S14.file-editor-validation | pass | 74f198df3650 | bullet 12: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-12.log |
| S14.file-editor-view | pass | 74f198df3650 | bullet 12: pass; bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-12.log |
| S14.gemini-file-tools | pass | 74f198df3650 | bullet 15: pass; bullet 17: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)); bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-15.log |
| S14.grep | pass | 74f198df3650 | bullet 1: pass; bullet 13: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-01.log |
| S14.preset-default | pass | 74f198df3650 | bullet 15: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-15.log |
| S14.preset-gpt5-gemini | pass | 74f198df3650 | bullet 15: pass; bullet 17: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-15.log |
| S14.shared-working-dir | pass | 74f198df3650 | bullet 1: pass; bullet 16: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-01.log |
| S14.terminal-cleanup | pass | 74f198df3650 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-env | pass | 74f198df3650 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-interactive | pass | 74f198df3650 | bullet 2: pass; bullet 4: pass; bullet 18: blocked (1 model-backed block(s) skipped (no DEEPSEEK_API_KEY or LLM_API_KEY)) | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-metadata | pass | 74f198df3650 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-observation-wait-cap | pass | 74f198df3650 | bullet 9: pass; bullet 10: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-09.log |
| S14.terminal-output-truncation | pass | 74f198df3650 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-pane-pool | pass | 74f198df3650 | bullet 3: pass; bullet 4: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-03.log |
| S14.terminal-secret-masking | pass | 74f198df3650 | bullet 2: pass; bullet 3: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-02.log |
| S14.terminal-shell-exit | pass | 74f198df3650 | bullet 9: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-09.log |
| S14.tool-output-masking | pass | 74f198df3650 | bullet 12: pass; bullet 13: pass | /tmp/claude-0/-home-user/9ddc1e52-a476-546b-b999-20d8b63470ad/scratchpad/sdk/s14/transcripts/S14-core-tools-12.log |
