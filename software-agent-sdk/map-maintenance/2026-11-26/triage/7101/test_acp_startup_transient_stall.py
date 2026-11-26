import sys
import time
from pathlib import Path

import pytest

from openhands.sdk import Conversation
from openhands.sdk.agent import ACPAgent
from openhands.sdk.event.conversation_error import ConversationErrorEvent

SERVER = str(Path(__file__).with_name("flaky_acp_server.py"))


def _conversation(tmp_path, monkeypatch, stall_method, always=False):
    log = tmp_path / "requests.log"
    monkeypatch.setenv("FLAKY_MARKER", str(tmp_path / "launched"))
    monkeypatch.setenv("FLAKY_LOG", str(log))
    monkeypatch.setenv("FLAKY_STALL_METHOD", stall_method)
    if always:
        monkeypatch.setenv("FLAKY_STALL_ALWAYS", "1")
    events: list = []
    conv = Conversation(
        agent=ACPAgent(acp_command=[sys.executable, SERVER], acp_startup_timeout=3),
        workspace=str(tmp_path),
        persistence_dir=str(tmp_path / "conv"),
        callbacks=[events.append],
        visualizer=None,
    )
    conv.send_message("say hello")
    return conv, events, log


def test_transient_pre_session_stall_is_retried_and_turn_starts(tmp_path, monkeypatch):
    conv, events, log = _conversation(tmp_path, monkeypatch, "initialize")
    try:
        conv.run()  # the server stalls once on `initialize`, then is healthy
    finally:
        print("\nrequests seen by the ACP server:\n" + log.read_text())
        print("errors:", [(e.code, e.detail) for e in events
                          if isinstance(e, ConversationErrorEvent)])
    requests = log.read_text().splitlines()
    assert sum(r.endswith("session/new") for r in requests) == 1
    assert sum(r.endswith("session/prompt") for r in requests) == 1


def test_startup_timeout_names_the_stalled_phase(tmp_path, monkeypatch):
    conv, events, log = _conversation(tmp_path, monkeypatch, "session/new", always=True)
    with pytest.raises(TimeoutError):
        conv.run()
    [error] = [e for e in events if isinstance(e, ConversationErrorEvent)]
    print("\nerror:", error.code, repr(error.detail))
    assert error.code == "ACPStartupTimeout"
    assert "session/new" in error.detail


def test_permanent_stall_still_terminates(tmp_path, monkeypatch):
    conv, events, log = _conversation(tmp_path, monkeypatch, "initialize", always=True)
    start = time.monotonic()
    with pytest.raises(TimeoutError):
        conv.run()
    assert time.monotonic() - start < 30
    assert [e.code for e in events if isinstance(e, ConversationErrorEvent)] == [
        "ACPStartupTimeout"
    ]
