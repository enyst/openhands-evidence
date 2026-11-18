"""Exercise ACP and Projects-off child launches using the PR's sources."""

import asyncio
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from openhands.agent_server import tool_router  # noqa: F401 (register server-owned tools)
from openhands.agent_server.config import Config
from openhands.agent_server.conversation_service import ConversationService
from openhands.agent_server.experimental_features import PROJECT_TOOL_NAMES
from openhands.agent_server.models import (
    StartChildConversationRequest,
    StartConversationRequest,
)
from openhands.agent_server.persistence import (
    PersistedProjects,
    ProjectItem,
    ServerStores,
)
from openhands.agent_server.project_service import PROJECT_COORDINATOR_TOOLS
from openhands.sdk import Agent, LLM, Message, TextContent, Tool
from openhands.sdk.agent.acp_agent import ACPAgent
from openhands.sdk.context.prompts.presets import PromptPreset
from openhands.sdk.conversation.request import AgentLaunchAdditions
from openhands.sdk.profiles import ACPAgentProfile
from openhands.sdk.workspace import LocalWorkspace
from openhands.agent_server.event_service import EventService


async def launch(root: Path):
    workspace = root / "workspace"
    workspace.mkdir()
    stores = ServerStores.from_config(Config(conversations_path=root / "conversations"))
    profile = ACPAgentProfile(
        name="review", acp_server="custom", acp_command="synthetic-command-unused"
    )
    stores.agent_profiles.save(profile)
    project = ProjectItem(name="Review example")
    stores.projects.save(PersistedProjects(projects=[project]))
    marker = "Synthetic project memory for this probe."
    async with ConversationService(
        conversations_dir=root / "conversations", stores=stores, enable_browser=False
    ) as service:
        acp = await service.projects.start_coordinator(
            project.id.hex, str(workspace), agent_profile_id=profile.id
        )
        assert isinstance(acp.agent, ACPAgent)
        parent, _ = await service.start_conversation(
            StartConversationRequest(
                workspace=LocalWorkspace(working_dir=str(workspace)),
                agent=Agent(
                    llm=LLM(model="gpt-4o", usage_id="example"),
                    tools=[Tool(name=name) for name in PROJECT_COORDINATOR_TOOLS],
                ),
                tags={"project": project.id.hex},
                agent_launch_additions=AgentLaunchAdditions(
                    prompt_preset=PromptPreset.PROJECT_COORDINATOR,
                    project_context=marker,
                ),
            )
        )
        with (
            patch.dict(os.environ, {"OH_RUNTIME_EXPERIMENTAL_FEATURES": "{}"}),
            patch.object(EventService, "run", autospec=True),
        ):
            created = await service.start_child_conversation(
                parent.id,
                StartChildConversationRequest(task="Example", isolation="shared"),
            )
        assert created is not None
        child = await service.get_conversation(created.conversation_id)
        assert child is not None and isinstance(child.agent, Agent)
        assert child.agent.agent_context is not None
        print(
            json.dumps(
                {
                    "scenario": "child_after_projects_disabled",
                    "project_tag": child.tags.get("project"),
                    "project_tools": sorted(
                        {t.name for t in child.agent.tools} & set(PROJECT_TOOL_NAMES)
                    ),
                    "prompt_preset": child.agent.prompt_preset,
                    "memory_in_rendered_dynamic_context": marker
                    in (child.agent.dynamic_context or ""),
                },
                sort_keys=True,
            )
        )
        acp_service = await service.get_event_service(acp.id)
        assert acp_service is not None
        message = Message(
            role="user", content=[TextContent(text="Synthetic first message")]
        )
        await acp_service.send_message(message, False)
        try:
            await asyncio.to_thread(acp_service.get_conversation().run)
        except NotImplementedError as exc:
            error = f"{type(exc).__name__}: {exc}"
        else:
            error = None
        print(
            json.dumps(
                {
                    "scenario": "acp_coordinator_first_run",
                    "native_project_tools": len(acp.agent.tools),
                    "error": error,
                },
                sort_keys=True,
            )
        )


def main():
    with TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        with patch.dict(
            os.environ,
            {
                "OH_PERSISTENCE_DIR": str(root / "settings"),
                "OH_RUNTIME_EXPERIMENTAL_FEATURES": '{"projects":true}',
            },
        ):
            asyncio.run(launch(root))


if __name__ == "__main__":
    main()
