# Fix evidence: EnumFilterDropdown closes on Escape (OpenHands/OpenHands#19816)

AI-generated evidence (an agent helping Engel Nyst). Branch `claude/fix-enum-filter-escape`, local `control-openhands` stack built from the fix, Agent Server 1.62.0, Chromium. Each screenshot was taken right after pressing Escape with the menu open; compare with the before shots in `openhands/bugs/2026-11-17/enum-filter-escape/`.

- `group-by-desktop-after-escape.png`, `group-by-phone-after-escape.png`: Group by menu closed (menu count 0, trigger aria-expanded false, focus on the trigger).
- `filter-status-after-escape.png`: status menu closed, Filters popover still open.
- `mcp-section-filter-after-escape.png`: MCP section filter closed.
- `older-cutoff-after-first-escape.png`: cutoff menu closed, More options dialog still open (a second Escape then closed the dialog).
