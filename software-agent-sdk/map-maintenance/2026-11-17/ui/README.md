# Agent Canvas UI check, 2026-11-17

Agent Canvas (OpenHands/OpenHands 5ed4ffa) launched with `control-openhands launch --new --sdk-path <software-agent-sdk at 0275e714> --build always`; doctor ok; DeepSeek flash.

- `F07.conversation-page.png`: a conversation runs and renders on the TARGET agent server (session socket snapshots no longer carry skill bodies, #6881).
- `F07.skills-modal.png`: Show Available Skills still lists the conversation's 15 public skills after #6881 (Canvas reads them from `POST /api/skills`, not the snapshot).
- `F18.page.png`: the Skills page catalog (public catalog enabled, default of #6739).
- `F17.library-catalog.png`: MCP Servers page on the TARGET server.
- `F07.mention-link.png`: an agent message containing a conversation mention `[Build notes](conversation:0123456789abcdef0123456789abcdef)` (#6851's mention format). Canvas renders "Build notes" as a link whose `href` is empty (`""`; DOM read via `browser eval`), so the mention leads nowhere.
