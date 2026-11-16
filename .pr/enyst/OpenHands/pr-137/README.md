# Decision cards: Canvas fork PR #137

AI-generated review evidence, published by Amp on Engel Nyst's behalf.
Moved on 2026-11-16 from [enyst/OpenHands#137](https://github.com/enyst/OpenHands/pull/137)
at evidence commit `6b2bb9412e98a6b1b6a3b617a766db45f5e5d0fa`.
The HTML and eight screenshots are byte-for-byte copies of that snapshot;
paths mentioned inside the HTML describe its original location.

- [Self-contained design and verification note](decision-cards.html)
- [Eight inspected running-Canvas screenshots](decision-cards/)
- Tested Canvas product revision: `ce93903694a8267c6502aa224aa2af53b2a8feeb`.
- SDK initial coverage: `c5239d7c3ed9f8671400e9e1bdb2123578b1c6df`;
  focused follow-up and live restart/answer check: `9b42766aad861b91175a5fa6fa0464cf536466c1`.
  Later upstream SDK changes are not covered by this evidence.
- Source SDK PR: [OpenHands/software-agent-sdk#6852](https://github.com/OpenHands/software-agent-sdk/pull/6852).
- Source issue: [OpenHands/OpenHands#19773](https://github.com/OpenHands/OpenHands/issues/19773),
  mirrored as [enyst/OpenHands#136](https://github.com/enyst/OpenHands/issues/136).

## Reproduction and observations

Build the TypeScript client from the tested SDK revision and install it locally
without changing committed dependency pins. Launch an isolated Canvas stack with
`control-openhands launch --new --sdk-path "$SDK_CHECKOUT" --build always`.
Enable experimental Decision cards and use a privately configured real-model
profile. Ask for Train/Bus choices with consequences and a recommendation, submit
a choice with a note, and verify the answered card persists after reload without
a duplicate machine answer bubble. Repeat with a text-only answer, offline
failure/retry, ordinary chat closure, feature-off readability and restart.
See the PR description and design note for the commands and full reproduction.

Final focused Canvas checks: 72 files / 932 tests passed. Lint/typecheck,
app/library builds and translation completeness passed with the locally built
client. The initial full suite had 10,708 passing / 16 failing tests in Docker
shell/environment tests and the independent verification-map check. That full
suite was not rerun after the final answer-bubble filter fix.

The committed published-client pin lacks the required APIs, so clean-install CI
is blocked until a compatible SDK/client release and dependency update. This
move does not resolve that gate. Cloud decision-card interactions, ACP-native
asks and delegated/planning-agent answers are not claimed as verified. No
package release, upstream push, merge or deployment is implied.
