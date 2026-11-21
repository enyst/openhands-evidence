# OpenHands bugs found in the 2026-11-21 map-maintenance pass

AI-generated on behalf of Engel Nyst by the daily verify-openhands routine. Source: OpenHands/OpenHands main 0f4cb6a, Agent Server 1.63.1, automation 1.34.1, driven with `control-openhands` (no model key; a placeholder key, shown masked as `****0000`, makes runs and conversations end in an auth error).

- `run-row-phone-overlap/`: automation Runs list at 390 px draws the start time over the cost (#19935). Also reproduced on 41a81f5 (before #19903).
- `mention-dashless-route/`: a conversation mention link opens `/conversations/<32-hex id>`; no sidebar row is current and "Initialized session" is missing, unlike the dashed route.
