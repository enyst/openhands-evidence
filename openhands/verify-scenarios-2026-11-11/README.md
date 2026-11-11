# Message timestamps and the server's time zone (2026-11-11)

Evidence for a verify-openhands skill PR on OpenHands/OpenHands (branch
`claude/project-thread-z00wsv`), which adds the reproduced failure for
[OpenHands/OpenHands#19543](https://github.com/OpenHands/OpenHands/issues/19543)
to the feature map (`F06.message-timestamp`) and a `browser timezone` verb to
`control-openhands`.

Source under test: OpenHands/OpenHands `main` at `b759f8a7f4cf`, Agent Server
1.62.0, automation 1.32.1, Chromium at 1440x1000, model `deepseek/deepseek-flash`.

| File | Run | What it shows |
| --- | --- | --- |
| `server-utc-minus-3-tooltip.png` | `TZ=America/Sao_Paulo control-openhands launch --new`, browser in UTC | A message sent seconds earlier reads `3 hours ago`; its tooltip reads `Nov 11, 2026, 5:16 PM` at 23:16 UTC. The sidebar row for the same conversation reads `28s`. Reproduced on two conversations and after a reload. |
| `server-utc-browser-tokyo.png` | plain `control-openhands launch --new` (host in UTC), then `browser timezone Asia/Tokyo` and a reload | The same hover reads `Just now`: the browser's zone is not the cause. |

The events the server stored on the first run carry the host's local time with
no offset (`"timestamp": "2026-11-11T20:16:43.387579"`), and the page reads
that as UTC.

Steps, on each run: `control-openhands onboard --skip`, `llm preset deepseek`,
`conversation start --prompt "Reply with only the word hi. Do not run any tools." --wait`,
`browser hover 'testid=user-message'`, then read the `message-timestamp` text.

---

Written by Claude, an AI agent, on behalf of Engel Nyst.
