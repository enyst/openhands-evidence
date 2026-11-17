# EnumFilterDropdown menus ignore Escape (2026-11-17)

AI-generated evidence (an agent helping Engel Nyst) for the Agent Canvas bug "menus built on the shared EnumFilterDropdown do not close on Escape".
Source: OpenHands/OpenHands main@5ed4ffa5ac2509e479acc12b83247fbb4c3612c8, local `control-openhands` stack, Agent Server 1.62.0, Chromium.
Each screenshot was taken right after pressing Escape with the menu open (two attempts per menu, same result):

- `group-by-desktop-after-escape.png`: Automations dashboard, Group by menu still open (1440x1000).
- `group-by-phone-after-escape.png`: same at 390x844.
- `filter-status-after-escape.png`: Filters popover with the status menu still open.
- `mcp-section-filter-after-escape.png`: MCP Servers page section filter still open.
- `older-cutoff-after-escape.png`: More options dialog, Hide old conversations cutoff menu still open.
