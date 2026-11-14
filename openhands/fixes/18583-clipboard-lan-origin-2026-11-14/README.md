# PR #18583 driven live outside a secure context (2026-11-14)

Build: main@4bbea81d merged locally with PR #18583 head 741f41f4 (clean merge,
not pushed). Page: `http://lan.openhands.test:18800`, the verify run's
non-loopback origin, where `isSecureContext` is `false` and
`navigator.clipboard` is `undefined`.

- `copy-clicked-no-error.png`: the reply's Copy button was clicked. No page
  error and no error toast (on main the same click raises `Cannot read
  properties of undefined (reading 'writeText')`).
- `pasted-back-into-composer.png`: Control+V in the composer pastes the
  reply text, `copied-over-http-18582`, so the fallback really wrote the
  clipboard.
