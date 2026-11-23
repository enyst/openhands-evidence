# verify-openhands map maintenance, 2026-11-23 (delta pass)

AI-generated on behalf of Engel Nyst by the daily verify-openhands routine.

- Range: OpenHands/OpenHands main 6fa7686d..c5e47c4b (the baseline had not moved since 2026-11-18, because earlier passes had no model key), Agent Server 1.63.1, automation 1.34.1.
- Model: litellm_proxy/deepseek-v4-flash (and deepseek-v4-pro for second-profile checks) through the All Hands eval proxy, set with `control-openhands llm set` under the profile names `deepseek-flash`/`deepseek-pro` in place of `llm preset deepseek`. Model-backed checks that 2026-11-19..21 left blocked were driven today.
- `reports/` holds the `control-openhands evidence report` of every run: five worker runs (chat-composer F05/F07, chat-activity F06, automations F21/F22/F23/F28, settings-shell F01/F02/F09/F10/F12/F14/F18/F25/F26/F30 plus public, version-gate and locked-Cloud runs, smoke/rotation F08/F15/F29/F27 + smoke + bug intake), an independent repro of the two new defects (#20003, #20004), and two independent re-verification runs of every edited row.
- Screenshots are named `<feature>-<what>[-<issue>].png`; they come from those runs.
