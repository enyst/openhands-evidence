# Verification ledger — run 2026-11-20T0913-2e4ab9

Revision `428b3dc2a0e8d3d0f689a909e2607e33d973da76`, local mode, Agent Server 1.63.1, base http://127.0.0.1:18800.

Checks: 21 — pass 17, fail 0, blocked 4, not-run 0, xfail 0, xpass 0. Families: 3.

## Families

| Family | pass | fail | blocked | not-run | xfail | xpass |
|---|---|---|---|---|---|---|
| F05 | 1 | 0 | 0 | 0 | 0 | 0 |
| F09 | 14 | 0 | 0 | 0 | 0 | 0 |
| F30 | 2 | 0 | 4 | 0 | 0 | 0 |

## Checks

| Feature/check | Entry point | Expected → actual | Result | Note | Evidence |
|---|---|---|---|---|---|
| F30.agent-reacts | conversation | per map → not driven | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset in this session) |  |
| F30.flag-off | conversation | per map → not driven | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset in this session) |  |
| F30.picker-placement | conversation | per map → not driven | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset in this session) |  |
| F30.user-reacts | conversation | per map → not driven | blocked | needs a working LLM key (DEEPSEEK_API_KEY unset in this session) |  |
| F05.slash-menu | composer '/' | map: 40 with extensions 0.42.0 → 41 options, @openhands/extensions 0.43.0 (#19879), no skill fixtures | pass | count drift from the extensions bump; map updated | `evidence/F02.slash-menu/count.png` |
| F09.cloud-links | local backend | no Integrations / Cloud links → count 0 | pass |  |  |
| F09.command-menu-coverage | Command menu | every nav page reachable from menu → all 9 nav pages including Experimental listed in Settings group | pass |  |  |
| F09.desktop-nav | Settings desktop nav | map: 8 links Agent..Secrets → 9 links: Agent, LLM, Model Router, Agent Context, Verification, Runtime, Application, Secrets, Experimental (last, #19881); one aria-current=page on each, incl. Experimental | pass | map drift: Experimental (#19503, #19881) missing from list; map updated | `evidence/F09.desktop-nav/nav-experimental.png` |
| F09.entry-command-menu | Command menu > Settings group | Settings group opens matching page → Group lists ... Secrets settings, Experimental (last); 'Experimental' + Enter opens /settings/experimental; Secrets settings, Settings verified | pass | map drift: Experimental option missing from the map's list | `evidence/F09.entry-command-menu/experimental.png` |
| F09.entry-gear | sidebar gear | /settings/agents; back skips /settings → as expected | pass |  |  |
| F09.landmarks | /settings/agents | one main → count 1 | pass |  |  |
| F09.legacy-agent-redirect | /settings/agent | /settings/agents → /settings/agents | pass |  |  |
| F09.page-header | Settings > Experimental | title + subline per page → Experimental: 'Experimental features you can turn on or off. Changes apply to conversations you start afterwards.'; other 7 sublines match; Secrets has no shell h2 | pass |  | `evidence/F09.page-header/experimental.png` |
| F09.phone-back | phone hub > Experimental | Back chevron labelled Settings returns to hub → aria-label Settings; returns to /settings, hub visible | pass |  | `evidence/F09.phone-back/experimental-phone.png` |
| F09.phone-hub | /settings at 390x844 | map: eight links → nine links ending with Experimental, version button, synced text; no subtitle; no horizontal overflow | pass | map drift: count/list updated | `evidence/F09.phone-hub/hub-experimental.png` |
| F09.synced-badge | settings nav footer | synced from Local backend (<origin>) → These settings are synced from Local backend (http://127.0.0.1:18800) | pass |  |  |
| F09.tablet-selector | /settings/app at 820x1180 | selector lists every visible destination → lists 9 incl. Experimental; selecting it navigates, trigger reads 'Settings Experimental' | pass |  | `evidence/F09.tablet-selector/experimental.png` |
| F09.unknown-subpath | /settings/does-not-exist | Not found, no settings shell → not-found-screen 1, settings-screen 0 | pass |  |  |
| F09.update-up-to-date | version card dialog | latest version status → You're running the latest version. What's new (registry reachable) | pass |  |  |
| F30.open | /settings/experimental | one switch per server feature in API order, notice below → 5 switches (Agent Server 1.63.1): conversation_reactions, ask_user (Decision cards), conversation_mentions, message_edits, factories; notice text matches | pass | Factories switch (new in Agent Server 1.63.1) shows no sidebar entry on Canvas when on: UI in flight (#19800, #19845); main pins 1.63.0 which lists no such flag? | `evidence/F30.open/desktop.png` |
| F30.toggle | /settings/experimental | saves at once; survives reload → body.0.enabled false->true; checked after reload | pass |  | `evidence/F30.toggle/on-after-reload.png` |
