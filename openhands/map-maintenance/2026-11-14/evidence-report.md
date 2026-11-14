# Verification ledger — run 2026-11-14T0858-b4a69f

Revision `830c0459e2f6056ab81e020c22970e782ae1be75`, local mode, Agent Server 1.62.0, base http://127.0.0.1:18800.

Checks: 13 — pass 10, fail 0, blocked 2, not-run 1, xfail 0, xpass 0. Families: 9.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F01 | 1 | 0 | 0 | 0 | 0 | 0 |
| F02 | 1 | 0 | 0 | 0 | 0 | 0 |
| F04 | 3 | 0 | 0 | 0 | 0 | 0 |
| F07 | 2 | 0 | 0 | 0 | 0 | 0 |
| F13 | 0 | 0 | 1 | 0 | 0 | 0 |
| F17 | 0 | 0 | 0 | 1 | 0 | 0 |
| F18 | 2 | 0 | 0 | 0 | 0 | 0 |
| F25 | 0 | 0 | 1 | 0 | 0 | 0 |
| F26 | 1 | 0 | 0 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F13.mcp-scope | ACP Claude Code profile with OAuth MCP (#19139 closed) | ACP session reuses the OAuth token stored through Customize → not reachable | blocked | Needs an OAuth MCP provider account authorized via Customize > MCP Servers and an authenticated Claude Code ACP profile |  |
| F25.cloud | Cloud backend conversation delete (src/api/cloud/*) | Delete all on a Cloud backend deletes every page in the confirmed scope → not reachable | blocked | Needs an OpenHands Cloud backend/account; none available to this run |  |
| F17.enable-disable | /mcp installed card toggle hover | same remove-hover colours as skills (shared CirclePlusCheckToggle) → not driven this pass | not-run | Shared component verified on F18.toggle; MCP/plugin cards not re-driven in this delta pass |  |
| F01.telemetry-consent | First run consent modal | description >=4.5:1 in every theme; Escape keeps it; unchecked confirm saves false; gone after reload → description 5.58 Light+, 5.16 Solarized Light, 6.46 Neutral/Neo, 6.08 DeepSea, 5.42 Paper (#18539 fixed by #18540); Escape count 1; consent false; reload count 0 | pass |  | `evidence/F01.telemetry-consent/consent-light-plus-final.png` |
| F02.smoke | /settings/app, /settings/agents, /mcp, /plugins, /automations, /settings/secrets | pages render after dependency bumps (tanstack, zustand, framer-motion, vite, i18next, posthog, lucide, react-json-view) → all headings render, browser errors --app-only: 0 page/app errors | pass |  |  |
| F04.delete-all | View > Delete all (Light+) | count covers all stored conversations; all deleted → 26 stored, 20 rows loaded: dialog 'Are you sure you want to delete 26 conversations?' (description 5.58:1 Light+); Cancel kept 26; Confirm left 0 on server, empty state, Delete all disabled (#17919 fixed by #18367) | pass |  | `evidence/F04.delete-all/confirm-26-light-plus.png` |
| F04.delete-all | Phone 390x844, drawer > View > Delete all | dialog inside viewport, count covers all, deletes all → 24 stored (20 loaded): dialog says 24, insideViewport true, no overflow; Confirm left 0 | pass |  | `evidence/F04.delete-all/confirm-phone-24b.png` |
| F04.delete-all | View > Delete all, observed transitions | Loading... while remaining pages load, then full count → observe: at 103 ms 'Loading...', at 130 ms 'delete 26 conversations'; confirm left 0 | pass |  |  |
| F07.delete-confirm | Conversation ... menu > Delete / Stop | confirmation names the title; description >=4.5:1 in Light+/Solarized; Confirm removes it → Delete description 5.58 Light+, 5.16 Solarized Light; Stop confirmation 5.16 Solarized; Confirm Delete -> /conversations and ids lookup [null] (#18539 fixed) | pass |  | `evidence/F07.delete-confirm/confirm-solarized-light.png` |
| F07.hooks-modal | Conversation ... menu > Show Available Hooks | explanation names .openhands/hooks.json and ~/.openhands/hooks.json; workspace and user hooks merged, workspace first → text matches new wording; user file ($OH_PERSISTENCE_DIR/hooks.json = <run>/private/hooks.json in a control-openhands run, ~/.openhands for a normal install) lists 'Stop 1 hook'; with workspace hooks: 'Pre Tool Use 1 hook', 'Stop 2 hooks' (qa-ws-hook then qa-user-hook); hook_config at start has both | pass |  | `evidence/F07.hooks-modal/workspace-and-user-hooks.png` |
| F18.card | /skills, qa-nomodel card | Model invocation off pill >=4.5:1 in Neutral, Light+, Solarized Light → ink rgb(231,106,94) on 4% feedback-error tint over rgb(32,32,32) ~4.9:1 Neutral (was 7.2 with fixed #fca5a5 before #19485); 4.96 Light+; 5.05 Solarized; DeepSea 5.45 vs card | pass |  | `evidence/F18.card/nomodel-pill-openhands-neutral.png` |
| F18.toggle | /skills enabled card toggle, hovered | hover shows red remove X, theme-aware → Neutral: X rgb(231,106,94) on 24% tint (~3.6:1); Light+: white on rgb(193,42,28); Solarized: white on rgb(181,40,37); X stroke 2.5px (catalog-remove-icon-stroke, #19728) | pass |  | `evidence/F18.toggle/remove-hover-openhands-neutral.png` |
| F26.docker-image | ghcr.io/openhands/agent-canvas:sha-830c045 (published, revision label 830c045) | /canvas/ 200, Add a backend step, server_info = pinned agent-server, Debian snapshot 20261108T000000Z → /canvas/ 200 in ~14s; /canvas?qa=1#h -> /canvas/?qa=1#h; onboarding-step-check-backend visible; server_info 1.62.0 = pin; apt sources 20261108T000000Z (debian + security); zlib1g 1:1.3.dfsg+really1.3.1-1+deb13u1; EXTENSIONS_PATH ok; liveness exit 1 after agent-server kill | pass |  | `evidence/F26.docker-image/image-first-run.png` |
