# A non-loopback plain-HTTP origin for verify-openhands (2026-11-14)

Both screenshots are the run's browser at `http://lan.openhands.test:18800`,
a name the browser daemon resolves to 127.0.0.1. There `isSecureContext` is
`false` and `crypto.randomUUID` and `navigator.clipboard` are `undefined`.

- `before-19732-stuck-on-home.png`: main@e20691d0 (the commit before #19732).
  Sending the prompt leaves the page on Home with the prompt still in the
  composer; `browser toasts --history` recorded `crypto.randomUUID is not a
  function` (issue #19514). The same build at `http://127.0.0.1:18800` starts
  the conversation.
- `after-19732-conversation.png`: main@bca40384 (#19732 merged). The
  conversation starts and the reply streams in; `browser errors` shows no app
  error.

Also seen on main@bca40384 at this origin, twice: the message Copy button
copies nothing and raises `Cannot read properties of undefined (reading
'writeText')` (open issue #18582).
