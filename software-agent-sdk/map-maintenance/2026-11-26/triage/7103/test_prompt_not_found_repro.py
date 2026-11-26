"""Repro: render_template reports *any* template load/compile failure as
"Prompt file ... not found", even when the file exists.

The templates are the real packaged ones; nothing in prompt.py is mocked.
"""

import asyncio
import errno
import os
import stat
from pathlib import Path

import pytest
from pydantic import SecretStr

import openhands.sdk.context.condenser.llm_summarizing_condenser as cond_mod
import openhands.sdk.llm.llm as llm_mod
from openhands.sdk.agent import Agent
from openhands.sdk.context.condenser import LLMSummarizingCondenser
from openhands.sdk.context.prompts import prompt as prompt_mod
from openhands.sdk.context.prompts.prompt import render_template
from openhands.sdk.conversation import Conversation
from openhands.sdk.conversation.exceptions import ConversationRunError
from openhands.sdk.event import MessageEvent
from openhands.sdk.llm import LLM, Message, TextContent
from tests.sdk.context.view.conftest import (
    create_action_event,
    create_observation_event,
)


CONDENSER_PROMPTS = os.path.join(os.path.dirname(cond_mod.__file__), "prompts")
FULL_DIR = os.environ.get("OH_FULL_DIR")


@pytest.fixture(autouse=True)
def fresh_jinja(tmp_path, monkeypatch):
    monkeypatch.setenv("OH_PERSISTENCE_DIR", str(tmp_path / "oh"))
    prompt_mod._get_env.cache_clear()
    prompt_mod._get_template.cache_clear()
    yield
    prompt_mod._get_env.cache_clear()
    prompt_mod._get_template.cache_clear()


def _report(exc: BaseException, path: str) -> None:
    print(f"\n  file exists: {os.path.isfile(path)}")
    print(f"  raised: {type(exc).__name__}: {exc}")
    print(f"  __cause__: {exc.__cause__!r}  __context__: {exc.__context__!r}")


def test_malformed_custom_template_reported_as_missing(tmp_path):
    tpl = tmp_path / "custom_system_prompt.j2"
    tpl.write_text("You are helpful. {% if %}\n")
    with pytest.raises(FileNotFoundError) as ei:
        render_template(str(tmp_path), str(tpl))
    _report(ei.value, str(tpl))
    assert tpl.is_file() and "not found" in str(ei.value)


@pytest.mark.skipif(os.getuid() == 0, reason="root ignores directory modes")
def test_unwritable_bytecode_cache_reported_as_missing(tmp_path):
    cache = tmp_path / "oh" / "cache" / "jinja"
    cache.mkdir(parents=True)
    cache.chmod(stat.S_IRUSR | stat.S_IXUSR)  # read-only cache dir
    try:
        with pytest.raises(FileNotFoundError) as ei:
            render_template(CONDENSER_PROMPTS, "summarizing_system.j2")
    finally:
        cache.chmod(stat.S_IRWXU)
    path = os.path.join(CONDENSER_PROMPTS, "summarizing_system.j2")
    _report(ei.value, path)
    assert os.path.isfile(path)


@pytest.mark.skipif(not FULL_DIR, reason="needs OH_FULL_DIR on a small tmpfs")
@pytest.mark.parametrize("mode", ["sync", "async"])
def test_full_disk_condensation_ends_run_with_prompt_not_found(
    tmp_path, monkeypatch, mode
):
    full = Path(FULL_DIR)
    for p in full.iterdir():
        p.unlink() if p.is_file() else None
    monkeypatch.setenv("OH_PERSISTENCE_DIR", str(full / f"oh-{mode}"))
    llm_calls = []

    def completion(*a, **k):
        llm_calls.append(k)
        raise AssertionError("LLM must not be reached")

    async def acompletion(*a, **k):
        return completion(*a, **k)

    monkeypatch.setattr(llm_mod, "litellm_completion", completion)
    monkeypatch.setattr(llm_mod, "litellm_acompletion", acompletion)

    llm = LLM(model="gpt-4o", api_key=SecretStr("k"), usage_id="a", num_retries=0)
    condenser = LLMSummarizingCondenser(
        llm=llm.model_copy(update={"usage_id": "c"}), max_size=20, keep_first=2
    )
    conv = Conversation(  # in-memory event store: only the jinja cache hits disk
        agent=Agent(llm=llm, tools=[], condenser=condenser),
        workspace=str(tmp_path),
        visualizer=None,
        stuck_detection=False,
    )
    conv._ensure_agent_ready()
    conv.state.append_event(
        MessageEvent(
            source="user",
            llm_message=Message(role="user", content=[TextContent(text="go")]),
        )
    )
    for i in range(15):  # 31 events > max_size=20 -> SOFT event-count condensation
        a = create_action_event(f"r{i}", f"c{i}")
        o = create_observation_event(f"c{i}", content=f"out {i}")
        conv.state.append_event(a)
        conv.state.append_event(o.model_copy(update={"action_id": a.id}))

    with open(full / "filler.bin", "wb") as f:  # disk is now full
        try:
            while True:
                f.write(b"\0" * 4096)
                f.flush()
        except OSError as e:
            assert e.errno == errno.ENOSPC
    try:
        with pytest.raises(ConversationRunError) as ei:
            conv.run() if mode == "sync" else asyncio.run(conv.arun())
    finally:
        (full / "filler.bin").unlink()
    path = os.path.join(CONDENSER_PROMPTS, "summarizing_system.j2")
    print(f"\n[{mode}] status={conv.state.execution_status.value} llm_calls={len(llm_calls)}")
    _report(ei.value.__cause__, path)
    assert isinstance(ei.value.__cause__, FileNotFoundError)
    assert os.path.isfile(path) and not llm_calls
