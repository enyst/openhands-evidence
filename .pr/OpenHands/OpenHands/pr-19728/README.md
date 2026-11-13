# Catalog remove icon stroke

[OpenHands PR #19728](https://github.com/OpenHands/OpenHands/pull/19728) · 13 November 2026

| Build | Canvas commit |
| --- | --- |
| Before | 54a2b1948d77988df5212111908d8440f5fca494 |
| After | 13812c1cdc40bb6446255bfac07c31a9241e4796 |

Use the standalone production build with Local Agent Server 1.62.0. Launch with `control-openhands`, open Skills, and enable Add Javadoc. Hover the selected toggle to reveal its remove icon. Repeat at desktop and phone widths in Neutral and Light+. The phone-width hover uses Chrome's pointer. Click the hovered toggle, reload, and confirm the skill is disabled.

The four paired views produced identical [computed styles](measurements.json), including the 2.5 px SVG stroke, foreground, and background. The toggle state survived reload. This verification exercised the shared toggle in Skills. No model or account was needed.

[Download the before/after MP4](before-after.mp4)

| View | Before | After |
| --- | --- | --- |
| Neutral desktop | [PNG](before-neutral-desktop.png) | [PNG](after-neutral-desktop.png) |
| Neutral phone width | [PNG](before-neutral-phone.png) | [PNG](after-neutral-phone.png) |
| Light+ desktop | [PNG](before-light-desktop.png) | [PNG](after-light-desktop.png) |
| Light+ phone width | [PNG](before-light-phone.png) | [PNG](after-light-phone.png) |

Captured and documented by Codex on Engel Nyst's behalf.
