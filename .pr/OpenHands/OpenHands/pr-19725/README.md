# Onboarding slide height

[OpenHands PR #19725](https://github.com/OpenHands/OpenHands/pull/19725) · 13 November 2026

| Build | Canvas commit |
| --- | --- |
| Before | 93e6c4d2da4aa1ca9c9ee69c5db32c042893eeba |
| After | 5565ad34f68a551464172b783e68fceaffa8bde3 |

Use the standalone production build with Local Agent Server 1.62.0. Launch with `control-openhands`, skip first-run onboarding, then open `/?previewOnboardingStep=2` for LLM setup and `/?previewOnboardingStep=3` for Say hello. This uses the normal slide components through the existing preview route. No model or credentials are needed to check the layout.

Measure each slide at 1440 × 1000, 390 × 844, and 390 × 600. The computed maximum height, slide size, content geometry, and footer control states matched in all six pairs. At 390 × 600 the cap was 428 px, and scrolling the LLM form moved its content while the footer buttons stayed within the viewport. The [MP4](before-after.mp4) shows that scroll in both builds. See the [computed measurements](measurements.json).

| View | Before | After |
| --- | --- | --- |
| Desktop LLM setup | [PNG](before-desktop-llm.png) | [PNG](after-desktop-llm.png) |
| Desktop Say hello | [PNG](before-desktop-hello.png) | [PNG](after-desktop-hello.png) |
| Phone LLM setup | [PNG](before-phone-llm.png) | [PNG](after-phone-llm.png) |
| Phone Say hello | [PNG](before-phone-hello.png) | [PNG](after-phone-hello.png) |
| Short phone LLM setup | [PNG](before-390x600-llm.png) | [PNG](after-390x600-llm.png) |
| Short phone Say hello | [PNG](before-390x600-hello.png) | [PNG](after-390x600-hello.png) |

Captured and documented by Codex on Engel Nyst's behalf.
