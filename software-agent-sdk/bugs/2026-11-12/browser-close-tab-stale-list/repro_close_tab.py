"""Repro: browser_close_tab returns before browser_list_tabs stops listing the tab.

Usage: python repro_close_tab.py [N] [--switch-first] [--recording]
Each iteration: open a new tab (page2), optionally switch to tab 0, close the new
tab, then IMMEDIATELY list tabs. Also re-lists after polling to show it converges.
"""
import http.server, json, os, re, sys, tempfile, threading, time
from openhands.tools.browser_use.definition import (
    BrowserCloseTabAction, BrowserListTabsAction, BrowserNavigateAction,
    BrowserSwitchTabAction, BrowserStartRecordingAction,
)
from openhands.tools.browser_use.impl import BrowserToolExecutor

N = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 20
SWITCH = "--switch-first" in sys.argv
REC = "--recording" in sys.argv
if "--fix" in sys.argv:
    # Prototype fix: after browser-use's _close_tab returns, wait until the
    # SessionManager has processed Target.detachedFromTarget for that target.
    import asyncio
    from openhands.tools.browser_use.server import CustomBrowserUseServer
    _orig = CustomBrowserUseServer._close_tab
    async def _close_tab(self, tab_id, _orig=_orig):
        bs = self.browser_session
        target_id = await bs.get_target_id_from_tab_id(tab_id) if bs else None
        result = await _orig(self, tab_id)
        if target_id and bs and bs.session_manager:
            loop = asyncio.get_running_loop(); deadline = loop.time() + 3.0
            while bs.session_manager.get_target(target_id) is not None and loop.time() < deadline:
                await asyncio.sleep(0.01)
        return result
    CustomBrowserUseServer._close_tab = _close_tab

d = tempfile.mkdtemp()
open(os.path.join(d, "index.html"), "w").write("<html><title>one</title><body>one</body></html>")
open(os.path.join(d, "page2.html"), "w").write("<html><title>two</title><body>two</body></html>")
H = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=d, **k)
H.log_message = lambda *a: None
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=d, **k))
http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{srv.server_address[1]}"

ex = BrowserToolExecutor(headless=True)
ids = lambda txt: re.findall(r'"tab_id": "([^"]+)"', txt)
try:
    ex(BrowserNavigateAction(url=f"{base}/index.html"))
    if REC:
        print("recording:", ex(BrowserStartRecordingAction()).text[:80])
    fails, lags = 0, []
    for i in range(N):
        ex(BrowserNavigateAction(url=f"{base}/page2.html", new_tab=True))
        before = ids(ex(BrowserListTabsAction()).text)
        if len(before) != 2:
            print(f"iter {i}: setup expected 2 tabs, got {before}"); continue
        if SWITCH:
            ex(BrowserSwitchTabAction(tab_id=before[0]))
        close = ex(BrowserCloseTabAction(tab_id=before[-1])).text
        t0 = time.monotonic()
        after = ids(ex(BrowserListTabsAction()).text)
        ok = len(after) == 1
        lag = 0.0
        if not ok:
            fails += 1
            while len(after) != 1 and time.monotonic() - t0 < 10:
                time.sleep(0.01)
                after = ids(ex(BrowserListTabsAction()).text)
            lag = time.monotonic() - t0
            lags.append(lag)
        print(f"iter {i:2d}: {close[:40]!r} -> immediate list={'OK' if ok else 'STALE(2 tabs)'}"
              + ("" if ok else f", converged to {len(after)} after {lag*1000:.0f} ms"), flush=True)
    print(f"RESULT fix={'--fix' in sys.argv} switch_first={SWITCH} recording={REC} stale={fails}/{N}"
          + (f" max_lag_ms={max(lags)*1000:.0f}" if lags else ""))
finally:
    ex.close(); srv.shutdown()
