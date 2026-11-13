# Canvas version feedback

OpenHands/OpenHands [PR #19722](https://github.com/OpenHands/OpenHands/pull/19722) · 13 November 2026

| Build | Source |
| --- | --- |
| Before | c11557132fcff450f942cd1560315555c8c4c022 |
| After | ffde708b7779999817bb14d8a9c42e71958f522d |

Both isolated production builds used Local Agent Server 1.62.0 and Google Chrome through `control-openhands`. For the captures, both builds reported installed Canvas version 1.39.0 so the real npm registry response for 1.40.0 would open the update state. This local setup did not change the PR's package version. The update flow required no model calls.

1. Launch each build and dismiss onboarding and consent.
2. In Settings → Application, choose OpenHands Neutral or Light+. Open the Agent Canvas update card at 1440 × 1000. At 390 × 844, open it from the Settings hub.
3. On Home at desktop width, open the sidebar's New Version Available tile.
4. Compare the computed badge and notice colors, dialog height cap, release-note hover color, sidebar icon, and version dialog copy.

All six paired render states produced identical [measurements](measurements.json). In Neutral, the update notice kept RGB (59, 130, 246) text and RGB (30, 58, 95) fill. The height cap was 800 px on desktop and 675.2 px on phone. The long npm command extends past its row on phone in both captures. The comparison covers standalone Local Canvas and the two selected themes.

[Download the before/after MP4](before-after.mp4)

| View | Before | After |
| --- | --- | --- |
| Neutral desktop update card | [PNG](before-neutral-desktop-settings.png) | [PNG](after-neutral-desktop-settings.png) |
| Neutral phone update card | [PNG](before-neutral-phone-settings.png) | [PNG](after-neutral-phone-settings.png) |
| Neutral desktop sidebar dialog | [PNG](before-neutral-desktop-sidebar.png) | [PNG](after-neutral-desktop-sidebar.png) |
| Light+ desktop update card | [PNG](before-light-desktop-settings.png) | [PNG](after-light-desktop-settings.png) |
| Light+ phone update card | [PNG](before-light-phone-settings.png) | [PNG](after-light-phone-settings.png) |
| Light+ desktop sidebar dialog | [PNG](before-light-desktop-sidebar.png) | [PNG](after-light-desktop-sidebar.png) |

Captured and documented by Codex on Engel Nyst's behalf.
