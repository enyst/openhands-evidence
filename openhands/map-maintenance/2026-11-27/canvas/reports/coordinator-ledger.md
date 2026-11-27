# Verification ledger — run 2026-11-27T0859-658e4c

Revision `580c7f5dbfd0e2bc8607ffff1c2c7212cf9ba36f`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18800.

Checks: 14 — pass 11, fail 1, blocked 2, not-run 0, xfail 0, xpass 0. Families: 4.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F07 | 1 | 0 | 0 | 0 | 0 | 0 |
| F26 | 7 | 1 | 0 | 0 | 0 | 0 |
| F27 | 3 | 0 | 1 | 0 | 0 | 0 |
| F29 | 0 | 0 | 1 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F26.lan-http-origin | browser goto $OH_VERIFY_LAN_URL/ (lan.openhands.test) | Home loads outside a secure context → page body is 'Forbidden' (403): the loopback Host guard from #20061 rejects lan.openhands.test | fail | harness drift: the launcher needs OH_ALLOWED_HOSTS=lan.openhands.test | `evidence/F26.lan-http-origin/lan-forbidden.png` |
| F27.usage-unpriced | Usage tab, model with no reported cost | Total Cost — + 'Usage with no reported cost ... is not included in the total.' → not reached | blocked | Prerequisite: a working model whose provider reports no cost. Every working eval-proxy model returned x-litellm-response-cost > 0 (deepseek-v4-flash, glm-5.3-flash, qwen3-coder-next, devstral-2512, openai/ prefix too); free/unpriced ids refused (401/402/403/404/500). |  |
| F29.usage | ACP (Codex) conversation Usage tab | ACP usage keeps its plan-usage note, no generic estimate note; live stats carry usage_breakdown → not driven | blocked | Prerequisite: an approved Codex login (CODEX_AUTH_JSON) or a DeepSeek Responses-API key; neither is in this session (DEEPSEEK_API_KEY unset). The changed code (usage_breakdown on the live stats event) is shared with non-ACP conversations and passed there (F27.usage-by-model, live before reload). |  |
| F07.display-cost | Conversation ... > Display Usage and Cost (desktop + phone 390) | Usage panel opens (drawer at desktop, /panel at phone) with Total Cost, estimate note, By model → drawer at desktop (aria-pressed true, URL unchanged); /panel at phone, panel 390 wide inside viewport, no overflow; estimate note and By model shown | pass |  | `evidence/F07.display-cost/desktop.png` `evidence/F07.display-cost/phone.png` |
| F26.allowed-hosts | run launched with OH_ALLOWED_HOSTS=lan.openhands.test | a listed name passes the loopback guard, other names still 403 → Host lan.openhands.test:18800 200 and the full LAN conversation works; Host evil.example 403 | pass |  |  |
| F26.cli-help | node bin/agent-canvas.mjs --help | ENVIRONMENT VARIABLES lists OH_ALLOWED_HOSTS → OH_ALLOWED_HOSTS  Comma-separated tunnel/proxy hostnames a loopback bind accepts (e.g. abc.ngrok.app); exit 0 | pass |  |  |
| F26.host-bind-lan | launcher --host 0.0.0.0 --port 18960 (recipe literal) | warnings, AUTH_REQUIRED marker only, no key; reachable on LAN; API-key screen; guard off off-loopback → both warnings; only __AGENT_CANVAS_AUTH_REQUIRED__, key count 0; LAN 200; key:false authRequired:true; Next disabled; Skip -> API key screen, no toasts; submit -> root-layout; Host evil.example 200 (no loopback guard off-loopback) | pass |  | `evidence/F26.host-bind-lan/api-key-screen.png` |
| F26.lan-http-origin | browser goto $OH_VERIFY_LAN_URL/ after the harness sets OH_ALLOWED_HOSTS (restart) | not a secure context; conversation streams pong; copy works; no errors → secure false; conversation finished at lan url, agent-message pong, appErrors 0, no toasts; Copied to clipboard; clipboard holds the prompt | pass |  | `evidence/F26.lan-http-origin/conversation.png` |
| F26.loopback-host-guard | curl against the run's loopback ingress (P) and static server (P+3) | foreign Host and userinfo-spoofed Host get 403 Forbidden; loopback/localhost Host serve 200 → 127.0.0.1 200, localhost 200; Host evil.example 403 on ingress and static; Host evil.example@127.0.0.1 403 | pass |  |  |
| F26.loopback-origin-guard | curl POST and WebSocket upgrade on the loopback ingress | unsafe methods and WS upgrades with a foreign or null Origin get the guard's 403; GET with a foreign Origin and loopback cross-port Origin pass the guard → POST Origin evil 403, Origin null 403; WS Origin evil 403 (guard: no body headers); GET Origin evil 401 and POST Origin localhost:5173 401 (reach the Agent Server, which wants the key); the app's own sockets stream in the browser | pass |  |  |
| F26.mars-web-bridge | LAN stack /mars/* and loopback --mars-web run | health authRequired on LAN, rpc 401/200; loopback health 200, userinfo-spoofed Host 403 → {ok:true,authRequired:true}; 401 without key, 200 with; loopback /mars/health 200, Host evil.example@127.0.0.1 403 | pass |  |  |
| F27.usage-budget | Usage tab, max_budget_per_run 1 via API (arrange), priced conversation | budget meter $cost / $1.0000 (pct used) under Token Usage → $0.0017 / $1.0000 (0.17% used), bar width 0.169466% (Paper theme colour) | pass |  | `evidence/F27.usage-budget/budget.png` |
| F27.usage-by-model | Usage tab after /model switch to a second model; live and after reload | one row per model, sorted by cost, unused condenser id dropped, rows sum to total → rows litellm_proxy/deepseek-v4-flash $0.0014 (Input 15,152 · Output 246) then openai/deepseek-v4-flash $0.0003 (Input 15,060 · Output 2), total $0.0017; condenser (0 tokens) absent; same after reload | pass |  | `evidence/F27.usage-by-model/by-model-open.png` |
| F27.usage-metrics | Usage tab, priced model (litellm_proxy/deepseek-v4-flash) | Total Cost $x.xxxx + 'Estimated from model pricing — may differ from what your provider bills.' + By model row → Total Cost $0.0014, estimate note, By model: litellm_proxy/deepseek-v4-flash $0.0014, Input 15,152 · Output 246 | pass |  | `evidence/F27.usage-metrics/usage-priced.png` |
