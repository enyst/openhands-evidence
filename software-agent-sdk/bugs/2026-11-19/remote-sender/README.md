# RemoteConversation.send_message(sender=...) drops the sender (2026-11-19)

Checkout: OpenHands/software-agent-sdk main@141423921fdaeb08cd5f53464a69e860da70b66f (product code; the run's checkout carried only skill-file commits on top).

- `seam.py`: one program, one SDK. It sends `send_message("...", sender="goal")` to a LocalConversation and to a RemoteConversation against a fresh `control-agent-server launch --new` server, and prints the user MessageEvents' `(sender, text)`. No model is called.
- `probe.json`: the saved `control-agent-server exec` result (paths redacted to `<run>`/`<scratch>`). Its last stdout line:
  `SEAM_RESULT {"local": [["goal", "QA_SEAM_LOCAL"]], ..., "remote": [[null, "QA_SEAM_REMOTE"]]}`

Local keeps `sender: "goal"`; remote saves `sender: null`. The client posts `{"sender": "goal"}` to `POST /api/conversations/{id}/events`, whose body (`SendMessageRequest`) has no `sender` field (only `sender_conversation_id`), so the server ignores it with 200.
