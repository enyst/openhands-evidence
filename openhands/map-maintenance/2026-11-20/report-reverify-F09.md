# Verification ledger — run 2026-11-20T0918-52a2ca

Revision `428b3dc2a0e8d3d0f689a909e2607e33d973da76`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18830.

Checks: 28 — pass 25, fail 0, blocked 3, not-run 0, xfail 0, xpass 0. Families: 1.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F09 | 25 | 0 | 3 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F09.hidden-llm-redirect | hide_llm_settings | LLM link hidden, redirect → not reachable | blocked | frontend hardcodes hide_llm_settings: false |  |
| F09.locked-cloud-landing | /settings on locked Cloud canvas | /settings/app → not run | blocked | needs a Cloud host/account |  |
| F09.update-available | update dialog | Version x is available + npm/docker tabs → client 1.42.0 is npm latest (Up to date) | blocked | needs npm latest newer than client |  |
| F09.breakpoint-sweep | /settings and /settings/app at 767..1440 | hub <1024 (725/426/478/681 wide), redirect >=1024; app main widths 767/468/520/723/424/840, no overflow; main fills viewport and scrolls <1024 → exactly as expected; secrets main bottom 844/844,1024/1024,1180/1180,900/900; app main scrolls true below 1024; 1440: 282/1000, no inner scroll | pass |  | `evidence/F09.breakpoint-sweep/app-767.png` `evidence/F09.breakpoint-sweep/app-1024.png` |
| F09.cloud-links | local backend nav | integrations/cloud links count 0 (negative case) → 0 and 0 | pass | positive case blocked: needs a Cloud backend/account |  |
| F09.command-menu-coverage | Ctrl+K: Model Router / Agent Context | single option each, opens /settings/meta-llm and /settings/agent-context, menu closes → as expected, option texts match exactly; menu count 0 | pass |  |  |
| F09.desktop-nav | /settings/agents desktop nav | 9 links Agent..Secrets, Experimental last; button 'Agent Canvas Version …'; synced text; exactly one aria-current; pinned (navbar y 32 then 22 after scroll on /settings/app) → 9 links in map order, Experimental last (/settings/experimental); button reads 'Agent Canvas Up to date Version 1.42.0'; synced text 'These settings are synced from Local backend (http://127.0.0.1:18830)'; each of 9 clicks: aria-current page, count 1. Pinned: y 32 before, subtitle y -444 after scroll --by 1000, navbar y -16 (not 22): nav is sticky top 32px but its 512px height overruns its container bottom (496), so the 'Settings' label is pushed 16px above the viewport; all links remain visible | pass | map value y 22 stale: nav grew by one 38px link (Experimental); 22-38=-16 | `evidence/F09.desktop-nav/nav.png` `evidence/F09.desktop-nav/scrolled.png` |
| F09.entry-collapsed-rail | collapsed rail gear | /settings/agents, Agent highlighted → as expected; toggle restored to 'Collapse sidebar' | pass |  | `evidence/F09.entry-collapsed-rail/rail.png` |
| F09.entry-command-menu | Ctrl+K > Settings group | 10 options (Settings..Secrets settings, Experimental last) each opening its page; Experimental option text; LLM profiles filter shows 2; Condenser -> No commands found → all 10 targets reached; unfiltered group lists exactly the 10 in map order, Experimental last; Experimental option reads 'Experimental Experimental features you can turn on or off. Changes apply to conversations you start afterwards. Go'; Runtime option text matches; LLM profiles -> [LLM profiles selected, Model Router]; Condenser -> No commands found | pass |  | `evidence/F09.entry-command-menu/unfiltered.png` `evidence/F09.entry-command-menu/experimental.png` `evidence/F09.entry-command-menu/no-condenser.png` |
| F09.entry-deep-links | Home banner, checklist, composer LLM pill, + menu, agent-profile pill | /settings/llm or /settings/agents; popovers close → banner->/settings/llm, configure-llm->/settings/llm, customize-agent->/settings/agents; after llm preset deepseek --no-validate (dummy key): LLM Profiles->/settings/llm, +menu Manage agent profiles->/settings/agents, pill->/settings/agents; all popover counts 0; pill snapshot Available Profiles/default/Manage agent profiles | pass | composer links used preset with --no-validate and dummy key file |  |
| F09.entry-gear | sidebar gear | /settings/agents, aria-current page, data-active true/false on / → as expected | pass |  |  |
| F09.entry-gear | phone drawer gear | drawer gear opens hub, drawer closes → /settings, drawer detached within 5s | pass |  |  |
| F09.errors | browser errors --app-only after family | pageErrors 0 appErrors 0 → pageErrors 0, appErrors 0, warnings 0 (map expects i18n SCHEMA$TOOL_CONCURRENCY_LIMIT warnings from the profile editor; none seen) | pass | Agent Server 1.63.1 via --sdk-version |  |
| F09.hub-resize-redirect | resize phone<->desktop, tablet, 1023, 1024 | hub->/settings/agents on widen (replace); subpage keeps URL+Back; hub at 820/1023; redirect at 1024 → as expected | pass |  |  |
| F09.index-redirect | gear, goto /settings | redirect replaces history → back -> /, goto /settings -> /settings/agents | pass |  |  |
| F09.landmarks | /settings/agents, /settings/app, phone hub | role=main count 1, settings-screen DIV → 1,1,1; DIV | pass |  |  |
| F09.legacy-agent-redirect | goto /settings/agent | /settings/agents, back -> / → as expected | pass |  |  |
| F09.page-header | each nav click; header text | title + subline per map incl. Experimental 'Experimental features you can turn on or off. Changes apply to conversations you start afterwards.'; Secrets h2 count 0 → all 8 shell headers match exactly incl. Experimental; Secrets header h2 count 0 | pass |  | `evidence/F09.page-header/experimental.png` |
| F09.phone-back | phone hub > Verification > Back | Back label Settings returns to hub; drawer gear opens hub and drawer detaches → as expected | pass |  |  |
| F09.phone-hub | phone /settings | URL stays; heading Settings; nine links Agent..Secrets, Experimental; version button; synced text; subtitle 0; no overflow → exactly as expected (button 'Agent Canvas Up to date Version 1.42.0') | pass |  | `evidence/F09.phone-hub/hub.png` |
| F09.sidebar-version-tile | / sidebar | tile count 0 while Up to date → 0 | pass | positive case blocked: client is npm latest |  |
| F09.synced-badge | desktop nav footer | These settings are synced from Local backend (<origin>) → These settings are synced from Local backend (http://127.0.0.1:18830) | pass |  |  |
| F09.tablet-selector | tablet 820 /settings/app Settings selector | lists every visible destination, Application current; select Secrets navigates+closes; Tab/Escape returns focus; outside click dismisses; 768/1023 present, 767/1024 absent; /settings/llm/ trigger 'Settings: LLM'; nested URL Not Found → 9 links Agent..Secrets, Experimental; Application aria-current page; Secrets -> /settings/secrets, aria-expanded false; Tab focused Agent, Escape -> activeElement aria-expanded false; mouse-click outside closes; 768/1023 work, 767/1024 count 0; /settings hub count 0; /settings/llm/ trigger name 'Settings: LLM', h2 LLM, LLM current; /settings/llm/example not-found-screen 1 | pass | popover nav max-height 320px scrolls: at 820x1180 only 8 links show on open, Experimental needs a scroll inside the popover (reachable) | `evidence/F09.tablet-selector/open.png` `evidence/F09.tablet-selector/settings.png` |
| F09.unknown-subpath | /settings/does-not-exist | Page not found screen, no settings shell, sidebar stays, Home link → exact heading/paragraph/link; settings-screen 0, navbar 0, aside 1; Home -> / | pass |  | `evidence/F09.unknown-subpath/not-found.png` |
| F09.update-card | nav version card | card text Agent Canvas/Version/version + badge once npm check succeeds; opens dialog → 'Agent Canvas Up to date Version 1.42.0', badge count 1, dialog opens | pass |  |  |
| F09.update-modal | update dialog | re-check shows Checking for updates…, one GET registry latest, button re-enabled; Close and Escape close → observed 'Checking for updates…'; exactly 1 GET https://registry.npmjs.org/@openhands/agent-canvas/latest (200); enabled true; Close->0, Escape->0 | pass | failure text not producible: registry reachable (no mocks) |  |
| F09.update-modal-phone | phone hub version card | dialog 351@19.5, close 329.5 at 390; 288@16, close 263 at 320; inside, no overflow; Close/Escape close → exact values; all insideViewport true, no overflow; closes | pass |  | `evidence/F09.update-modal-phone/dialog.png` |
| F09.update-up-to-date | update dialog | You're running the latest version. What's new; releases link target _blank → exact; href https://github.com/OpenHands/OpenHands/releases target _blank | pass |  |  |
