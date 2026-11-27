# software-agent-sdk map maintenance, 2026-11-27

Daily delta pass over both feature maps (verify-agent-server, verify-sdk), main@7cfef13a (BASE d7263334).
The range holds only dependency bumps (#7148-#7154: google-cloud-aiplatform, authlib, filelock, cachetools;
TypeScript client @openrouter/sdk, vitest) plus the previous map PR (#7158). `map owners` / `sdk-map owners`
list no family; the bumped libraries' users were driven instead: F20, F22, F23, F24, F31, F34 and S03, S04, S14, S19.
Model access was the eval LiteLLM proxy only (no direct DEEPSEEK_API_KEY), so recipes that hard-code
`deepseek/*` models or `$DEEPSEEK_API_KEY` fail for that reason (environment, not product); see the reports.

New in the maps: open bug #7160 (condense while an action awaits confirmation runs it), on both surfaces.

- `agent-server-report.md`: `control-agent-server evidence report` over every recorded run of the pass.
- `sdk-report.md`: `sdk-map report` over S03, S04, S14, S19 and S06.
- `F10.condense-pending-action/target/`: main@7cfef13a, POST /condense answers 200 `{"success": true}`
  (`condense.json`) and one ObservationEvent is recorded right after (`observations.json`, body 1): the
  pending command ran. `map-run-main.json`: the bullet's xfail row.
- `sdk-transcripts/S06-context-condensers-13-target.log`: S06.condense-pending-action on main:
  ran_after true, observations_after 1, condensations 0.
- `fix-7161/`: the same two bullets against fix PR #7161 (head db4c3c87): F10 xpass twice
  (`F10-map-run-pr7161.log`, observation count 0 in `F10-observations-pr7161.json`) vs xfail twice on main
  (`F10-map-run-main.log`); SDK program facts on the PR (`S06-pending-pr7161.json`): ran_after false,
  observations_after 0, condensations 1, runs_after_approve 1.
