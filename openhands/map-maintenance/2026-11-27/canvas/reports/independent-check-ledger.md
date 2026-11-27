# Verification ledger — run 2026-11-27T0909-2b4afc

Revision `580c7f5dbfd0e2bc8607ffff1c2c7212cf9ba36f`, local mode, Agent Server 1.64.1, base http://127.0.0.1:18810.

Checks: 11 — pass 9, fail 0, blocked 0, not-run 2, xfail 0, xpass 0. Families: 2.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F26 | 6 | 0 | 0 | 0 | 0 | 0 |
| F27 | 3 | 0 | 0 | 2 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F27.usage-budget | source review: cost-section.tsx | no budget meter when unpriced → CostSection renders BudgetDisplay only when !isUnpricedUsage(cost, tokens); BudgetDisplay returns null without a cap (maxBudget null or <=0) | not-run | only the hide-when-unpriced claim reviewed, in source; not driven live |  |
| F27.usage-unpriced | source review | Total Cost —, unpriced note instead of estimate note, no budget meter, model row —, note also under a priced total when any model unpriced → source agrees: formatUsageCost returns — for cost 0 & tokens>0; cost-unpriced-note when isUnpriced\|\|hasUnpricedModel; estimate note only when !isUnpriced (and not ACP); BudgetDisplay hidden when unpriced; ModelBreakdown uses formatUsageCost per row; en string matches | not-run | not reachable live: every eval-proxy model reports a cost (openai/deepseek-v4-flash via proxy cost 0.0018235) |  |
| F26.allowed-hosts | LAN stack host 0.0.0.0 port 18960 | off loopback no Host/Origin check → Host evil.example 200, userinfo Host 200, POST Origin evil.example 401 (reaches agent server) | pass |  |  |
| F26.cli-help | node bin/agent-canvas.mjs --help | ENVIRONMENT VARIABLES lists OH_ALLOWED_HOSTS 'Comma-separated tunnel/proxy hostnames a loopback bind accepts', exit 0 → OH_ALLOWED_HOSTS  Comma-separated tunnel/proxy hostnames a loopback / bind accepts (e.g. abc.ngrok.app) (wrapped over 2 lines); exit 0 | pass | only OH_ALLOWED_HOSTS claim rechecked; text wraps after 'a loopback', so a one-line grep of the quoted phrase fails |  |
| F26.host-bind-lan | LAN stack host 0.0.0.0 port 18960 (server-side part) | not-loopback log lines; only AUTH_REQUIRED marker, key count 0; loopback run only SESSION_API_KEY; LAN:18960 200; Host evil.example 200; /mars/health ok; getAuthState 401/200; loopback run /mars/health 200, userinfo Host 403 → both [auth]/[static] lines; AUTH_REQUIRED only, 0; SESSION_API_KEY only; 192.0.2.2:18960 200 (own run 18810: 000 exit 7); evil Host 200 (also userinfo Host 200, static 18963 200, POST evil Origin 401); {ok:true,authRequired:true}; 401/200; 200/403 | pass | browser part skipped by instruction |  |
| F26.lan-http-origin | http://lan.openhands.test:18810 | insecure context, pong conversation finished, no app errors/error toasts; copy button Copied, clipboard has prompt → {secure:false,randomUUID:undefined,clipboard:undefined}; ok/finished at lan url conv 1811e67a; agent-message pong; appErrors 0; no error toast; aria-label 'Copied to clipboard'; pageErrors 0; loopback tab clipboard 'Reply with the single word: pong' | pass | model qa-flash (litellm_proxy/deepseek-v4-flash) substituted; onboard --skip --stay showed only onboarding (no consent step) on the LAN origin | `evidence/F26.lan-http-origin/conversation.png` `evidence/F26.lan-http-origin/copy.png` |
| F26.loopback-host-guard | curl ingress 18810 / static 18813 | 127.0.0.1 and localhost 200; evil.example on ingress and static, userinfo Host 403 body Forbidden → 200,200; 403,403,403; body Forbidden; also [::1], foo.localhost, 127.0.0.2 =200; /mars/health 200, userinfo 403 | pass |  |  |
| F26.loopback-origin-guard | curl ingress 18810 | POST foreign/null Origin 403; GET foreign Origin and POST localhost:5173 401; WS foreign Origin 403 Connection: close only; WS loopback Origin 403 from agent server with content-length 0 → 403,403,401,401; WS evil: 'HTTP/1.1 403 Forbidden' + 'Connection: close'; WS loopback: 'HTTP/1.1 403 ' + content-length: 0 + connection: close | pass |  |  |
| F27.usage-by-model | conv dabe4aa0 > /model qa-second > send > Usage | By model: two rows costliest first, each cost + Input/Output; sum = Total Cost; no condenser row; same after reload → openai/deepseek-v4-flash $0.0018 Input 15,193 · Output 2; litellm_proxy/deepseek-v4-flash $0.0008 Input 15,364 · Output 212; Total $0.0026 (API 0.0018235+0.00081334); condenser id present in usage_to_metrics with 0 tokens, no row; reload: identical rows | pass | second profile substituted (qa-second, openai/deepseek-v4-flash via proxy). After /model + conversation send the right panel was closed: the recipe's browser text 'testid=usage-model-breakdown' timed out until right-panel-toggle + conversation-tab-usage were clicked again | `evidence/F27.usage-by-model/by-model.png` |
| F27.usage-metrics | conv dabe4aa0 > Usage | Context Window, 1% used (99% left), <tokens>/1,000,000, Compact context, Token Usage rows, Total Cost $0.00… + estimate note, By model one row with Input/Output → 2% used (98% left) (fill 1.5259%), 15,259 / 1,000,000; Input 15,364 Cache Hit 0 Cache Write 0 Output 212 Total 15,576; Total Cost $0.0008; estimate note; By model: litellm_proxy/deepseek-v4-flash $0.0008 Input 15,364 · Output 212 | pass | percent label 2%/98% not the map's 1%/99% (prompt ~15.3k tokens on this model); model substituted | `evidence/F27.usage-metrics/usage.png` |
| F27.usage-provider-balance | conv dabe4aa0 > Usage | provider-balance-card count 0 → 0 | pass |  |  |
