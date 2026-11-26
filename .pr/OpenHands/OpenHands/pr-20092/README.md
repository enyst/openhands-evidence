# Home launcher spacing

PR: https://github.com/OpenHands/OpenHands/pull/20092

Date: 2026-11-26. AI-generated verification report on Engel Nyst's behalf.

Baseline: `6deb332c3602329306180fd7a99b3534753909df`. After: `e16ff390f58683f5e38e2f4374d39fa7bc2d6a72`. Current head `1dd2d2a4ad` adds only a comment placement correction after capture; the tested CSS and product behavior are unchanged. Both captured revisions built and launched with the repository's read-only `verify-openhands` skill and `control-openhands`, Google Chrome, Local Agent Server 1.64.1. The screenshots show the Paper palette.

This refactor names `padding-top: max(4rem, 28vh)` and enables `shadcn/no-arbitrary-values` as an error for its owner. It preserves the formula and surrounding classes.

## Observed results

Desktop 1440x1000, phone 390x844, short phone 390x600. Before and after measurement JSON is identical. Idle Home composer was filled and cleared without submitting a conversation. Top padding was 280px, 236.32px, and 168px respectively.

[Home launcher spacing: Before / After video](before-after.mp4) uses actual desktop recordings with clear labels and a quiet generated ambience tone. PNGs cover all three sizes.

Focused tests: 109 passed, including the compiled library CSS contract and lint enforcement. `npm run lint`: zero errors, 124 warnings (baseline 125). Production app build passed. Both batches also merge cleanly in a local merge-tree check.

## Reproduce and limits

Use `npm ci`, `npm run make-i18n`, `npm run lint`, and `npx vitest run __tests__/scripts/arbitrary-values-lint.test.ts __tests__/vite-config.test.ts` at the stated head. Launch baseline and head separately with `control-openhands launch --headless`, run `doctor`, skip onboarding for disposable state, and open /. Resize with `browser viewport`; compare computed style, scroll dimensions, and screenshots. For settings, seed disposable rows with `api PUT /api/settings/secrets --write` and scroll the list; inspect `thead` position.

Evidence covers standalone Local Canvas with the shown theme and fixed 16px root font. Cloud, embedded Canvas, other themes, and live model execution were not exercised. This is a style refactor, not a behavior change. Repository verification skills were not modified. Raw run state and credentials are excluded.
