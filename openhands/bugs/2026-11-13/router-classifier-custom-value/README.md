# Model Router editor: a typed custom classifier is cleared immediately

- Repository: OpenHands/OpenHands (Agent Canvas UI)
- Found during the verify-openhands delta pass on main@754abee4f086, Agent Server 1.62.0.
- Feature: F12 Model Router → `F12.editor-validation`.

In Settings → Model Router, the editor's **Classifier model** field accepts a free-text
name (`allowsCustomValue`). Typing or filling a name that is not a saved LLM profile is
wiped immediately, Save stays disabled, and editing an existing router snaps the field
back to its previous profile. Picking a profile from the list works.

## Regression
Introduced by #16654 (`@heroui/react` 2.8.10 → 3.2.4, rewriting `settings-dropdown-input.tsx`
onto the HeroUI v3 ComboBox). Reproduced 2/2 at the merge commit `aceb6b1f3` and at HEAD;
not reproduced at `aceb6b1f3^`. Older than this pass's BASE..TARGET range.

- `before-16654-typed-kept.png` — at `aceb6b1f3^`, a typed custom classifier is kept.
- `merge-16654-typed-cleared.png` — at the #16654 merge commit, the typed value is cleared.
- `head-typed-cleared-attempt1.png` — at HEAD, the field is empty, list open, Save disabled.
- `head-pick-from-list-works.png` — picking a listed profile works and enables Save.
- `head-edit-existing-reverts.png` — editing a router, a typed custom name reverts to the old profile.

AI-generated on behalf of Engel Nyst (@enyst).
