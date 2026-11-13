# Fix: Model Router editor keeps a typed custom classifier

Fix for the bug under `../../bugs/2026-11-13/router-classifier-custom-value/`.

`SettingsDropdownInput` gains an optional `inputValue` prop so a caller can control the
ComboBox text alongside the selection; the Model Router editor passes
`inputValue={config.classifier_model}` and a `selectedKey` that is non-null only when the
text names a listed profile. A typed name that matches no profile is then kept instead of
being reset to the selected item's text.

Verified live on main@754abee with the fix built in, Agent Server 1.62.0:
- `fix-typed-custom-kept.png` — a typed `qa-classifier` is kept and Save enables.
- `fix-edit-existing-custom-kept.png` — editing a router, a typed custom name is kept.
- `fix-typed-phone.png` — the same at phone width (390px).

Also re-verified: template prefill (`minimax-m3`) is kept, and picking a listed profile
still selects it. Unit tests added in `__tests__/.../meta-profile-editor.test.tsx`.

AI-generated on behalf of Engel Nyst (@enyst).
