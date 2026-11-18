"""Offline checks for OpenHands/software-agent-sdk PR 6602 at 05a8f915."""

import json
import os
import sys
from pathlib import Path

import pytest


if __name__ == "__main__":
    os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
    if sys.platform == "darwin":
        # Browser-tool teardown otherwise reads the screen on headless macOS.
        sys.modules["AppKit"] = None

from openhands.agent_server.conversation_service import AutoTitleSubscriber
from openhands.agent_server.project_board import ConversationOutcomeSubscriber
from openhands.agent_server.project_wake import reconcile_coordinator_updates
from openhands.sdk.conversation.state import ConversationExecutionStatus
from openhands.sdk.event import MessageEvent
from openhands.sdk.event.ask_user import AskUserAnswerEvent
from openhands.sdk.llm import Message, TextContent
from openhands.tools.ask_user import AskUserAction, AskUserOption
from tests.agent_server import test_project_cards as cards
from tests.agent_server.conftest import _projects_feature_on as _projects_feature_on
from tests.agent_server.test_project_cards import (
    client as client,
    persistence_dir as persistence_dir,
    save_without_running as save_without_running,
    service as service,
    stores as stores,
)


@pytest.fixture(autouse=True)
def skip_model_titles_and_installed_plugins(monkeypatch):
    async def skip_title(self, event):
        pass

    monkeypatch.setattr(AutoTitleSubscriber, "__call__", skip_title)
    monkeypatch.setattr(
        "openhands.sdk.conversation.impl.local_conversation.load_available_plugins",
        lambda **kwargs: {},
    )


@pytest.mark.asyncio
async def test_stale_coordinator_card_answers_a_later_worker_question(
    client, service, tmp_path
):
    _, coordinator, worker = await cards._project(client, service, tmp_path)
    original_id, coordinator_card_id = await cards._ask_through(
        service, coordinator, worker
    )
    await cards._record(service, worker, cards._user("Use SQLite."))

    later_question = cards._ask(
        AskUserAction(
            question="Which color?",
            options=[
                AskUserOption(label="Blue", consequence="Ocean"),
                AskUserOption(label="Red", consequence="Rose"),
            ],
        )
    )
    await cards._record(service, worker, later_question, cards._shown(later_question))

    tap = AskUserAnswerEvent(
        ask_id=coordinator_card_id, option_index=0, option_label="Postgres"
    )
    await cards._record(service, coordinator, tap)
    await cards._passed_on(service, coordinator, worker)

    (answer,) = await cards._answers(service, worker)
    assert answer.ask_id != original_id
    assert answer.ask_id == later_question.id
    assert answer.text == "Postgres"
    print(
        "OBSERVED",
        json.dumps(
            {
                "case": "stale_card",
                "new_question": later_question.action.question,
                "saved_answer": answer.text,
                "saved_against_new_question": answer.ask_id == later_question.id,
            }
        ),
    )


@pytest.mark.asyncio
async def test_startup_reconciliation_delivers_an_abandoned_reply(
    client, service, tmp_path, monkeypatch
):
    async def miss_live_delivery(self, event):
        pass

    monkeypatch.setattr(ConversationOutcomeSubscriber, "__call__", miss_live_delivery)
    _, coordinator, worker = await cards._project(client, service, tmp_path)
    original = cards._user("My original task")
    abandoned = cards._user(
        "Abandoned coordinator task", f"conversation:{coordinator.hex}"
    )
    output = MessageEvent(
        source="agent",
        llm_message=Message(
            role="assistant", content=[TextContent(text="Abandoned result")]
        ),
    )
    await cards._record(service, worker, original, abandoned, output)
    member = await service.get_event_service(worker)
    state = await member.get_state()
    with state:
        state.execution_status = ConversationExecutionStatus.FINISHED
    await service.navigate_conversation(worker, event_id=original.id)
    assert state.leaf_event_id == original.id
    assert output.id not in {event.id for event in state.walk_back()}

    delivered = await reconcile_coordinator_updates(service)
    messages = [
        event
        for event in await cards._events(service, coordinator)
        if isinstance(event, MessageEvent)
    ]
    saved = messages[-1].llm_message.content[-1].text
    assert delivered == 1
    assert saved == "Abandoned result"
    print(
        "OBSERVED",
        json.dumps(
            {
                "case": "branch_replay",
                "reply_on_active_branch": output.id
                in {event.id for event in state.walk_back()},
                "updates_delivered": delivered,
                "saved_in_coordinator": saved,
            }
        ),
    )


if __name__ == "__main__":
    raise SystemExit(
        pytest.main(
            [
                "-c",
                "pyproject.toml",
                "-o",
                "addopts=",
                "-q",
                "-s",
                "--disable-warnings",
                str(Path(__file__).resolve()),
            ]
        )
    )
