# Clipboard copy refactor: live check at a non-secure origin

Source: OpenHands/OpenHands branch `claude/project-thread-j9ci7m` at 01872e4
(issue #19843, follow-up to #18583). Date: 2026-11-18. AI-generated on Engel's behalf.

Setup: `control-openhands launch --new` from that checkout (Agent Server 1.62.0),
page opened at `http://lan.openhands.test:18800` (the verify skill's
`F26.lan-http-origin`: plain HTTP, `isSecureContext` false, `navigator.clipboard`
undefined), Chromium headless.

Steps and results:

1. Arrange the clipboard to `SENTINEL` (from the loopback origin).
2. At the LAN origin: Customize > Skills > **Add skill**. The modal has a focus trap.
3. Click the example's copy button (`add-skill-modal-example-copy`).
   The button turns into a checkmark (`lan-add-skill-modal-copied.png`); page errors 0,
   app errors 0, no toasts.
4. Read the clipboard from the loopback origin:
   `/add-skill https://github.com/OpenHands/extensions/tree/main/skills/code-review`.

Not covered live: Safari / iOS Safari (no Safari available here), and the failure
toast wording (covered by unit tests).
