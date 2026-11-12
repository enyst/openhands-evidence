# browser_list_tabs still lists a tab that browser_close_tab just closed

AI-generated on Engel Nyst's behalf, 2026-11-12, OpenHands/software-agent-sdk main@9bf835c
(browser-use 0.11.9, headless Chromium).

- `repro_close_tab.py`: opens a second tab, switches to the first, closes the second, then lists tabs
  at once; `--fix` applies the wait-until-detached prototype.
- `main-9bf835c-switch-first.txt`: `repro_close_tab.py 20 --switch-first` on main: 17/20 immediate
  lists still show 2 tabs; each converges within about 16 ms.
- `sdk-map-S15-browser-01.log`: the verify-sdk bullet that found it (`tabs_left eq 1` fails with 2).
