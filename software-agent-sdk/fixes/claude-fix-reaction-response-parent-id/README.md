# Fix: the reactions POST returns the event as stored

AI-generated on Engel Nyst's behalf. Branch `claude/fix-reaction-response-parent-id`, run with
`control-agent-server launch --new --checkout <that branch>` on 2026-11-12.

- `post-response.json`: the POST now answers with `"parent_id": "1ed5e09d-…"`, the reacted message.
- `search.json`: the stored ReactionEvent has the same `parent_id`.
