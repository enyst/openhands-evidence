# POST /api/conversations/{id}/reactions returns parent_id null

AI-generated on Engel Nyst's behalf. Reproduced 2026-11-12 on OpenHands/software-agent-sdk main@9bf835c
(run of the verify-agent-server map pass, `control-agent-server launch --new`, conversation_reactions on).

- `post-response.json`: the POST answers the ReactionEvent `f63f0ac6-…` with `"parent_id": null`.
- `search.json`, `get-one.json`, `socket.json`: the same event as stored and streamed carries
  `"parent_id": "ce34722e-…"`, the message it reacted to (the active leaf).
