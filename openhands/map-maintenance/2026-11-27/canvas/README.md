# Agent Canvas map maintenance 2026-11-27 (delta pass)

Range: OpenHands/OpenHands main 6deb332c3602329306180fd7a99b3534753909df .. 580c7f5dbfd0e2bc8607ffff1c2c7212cf9ba36f
(#20061 loopback Host/Origin guard, #19424 usage-panel cost, dependency bumps, the previous map PR #20096).

- reports/coordinator-ledger.md: coordinator run 2026-11-27T0859-658e4c (ports 18800-18803, --mars-web).
- reports/independent-check-ledger.md: independent re-run of every edited bullet, run 2026-11-27T0909-2b4afc.
- F26-lan-http-origin-before-harness-fix.png: $OH_VERIFY_LAN_URL answers "Forbidden" before control-openhands sets OH_ALLOWED_HOSTS.
- F26-lan-http-origin-after-fix.png, check-F26-lan-http-origin-copy.png: the LAN-origin conversation after the fix.
- F26-host-bind-lan-api-key-screen.png: --host 0.0.0.0 stack, API key screen.
- F27-usage-metrics-priced.png, F27-usage-by-model.png, check-F27-usage-by-model.png: Usage tab estimate note and By model rows.
- F07-display-cost-desktop.png / -phone.png: Display Usage and Cost at desktop and 390 px.

LLM: eval proxy (litellm_proxy/deepseek-v4-flash, openai/deepseek-v4-flash); no DeepSeek key in this session.
