"""Reproduce three Projects API results using local ASGI and temporary stores."""

import asyncio
import logging
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from uuid import UUID

from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient


async def run(root: Path) -> None:
    # The app module builds default stores at import. Set their location first.
    os.environ["OH_PERSISTENCE_DIR"] = str(root / "store")
    os.environ["OPENHANDS_SUPPRESS_BANNER"] = "1"
    os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
    logging.disable(logging.CRITICAL)

    from openhands.agent_server.api import add_domain_error_handler
    from openhands.agent_server.config import Config
    from openhands.agent_server.conversation_router import conversation_router
    from openhands.agent_server.conversation_service import ConversationService
    from openhands.agent_server.persistence import ServerStores
    from openhands.agent_server.projects_router import projects_router
    from openhands.sdk.profiles.agent_profile import OpenHandsAgentProfile
    from tests.agent_server.conftest import install_test_context, update_test_context

    config = Config(
        conversations_path=root / "conversations",
        static_files_path=None,
        session_api_keys=[],
    )
    stores = ServerStores.from_config(config)
    async with ConversationService(
        conversations_dir=config.conversations_path,
        stores=stores,
        enable_browser=False,
    ) as service:
        app = FastAPI()
        app.include_router(conversation_router, prefix="/api")
        app.include_router(projects_router, prefix="/api")
        add_domain_error_handler(app)
        install_test_context(app, config, conversation_service=service)
        update_test_context(app, stores=stores)

        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test", trust_env=False
        ) as client:

            async def check(label, method, path, expected, **kwargs):
                response = await client.request(method, path, **kwargs)
                assert response.status_code == expected, (label, response.status_code)
                print(f"{label} -> HTTP {response.status_code}")
                return response.json()

            os.environ["OH_RUNTIME_EXPERIMENTAL_FEATURES"] = "{}"
            await check("List projects while disabled", "GET", "/api/projects", 404)
            start = {
                "workspace": {"working_dir": str(root)},
                "agent": {
                    "kind": "Agent",
                    "tools": [],
                    "llm": {
                        "model": "gpt-4o",
                        "usage_id": "probe",
                        "api_key": "dummy",
                        "base_url": "http://127.0.0.1:1/v1",
                        "num_retries": 0,
                    },
                },
            }
            refused = await check(
                "Create ordinary conversation with project=billing",
                "POST",
                "/api/conversations",
                422,
                json={**start, "tags": {"project": "billing"}},
            )
            assert "Tags set by the server only: project" in refused["detail"]
            conversation = await check(
                "Create same conversation without tag",
                "POST",
                "/api/conversations",
                201,
                json=start,
            )
            conversation_id = conversation["id"]

            os.environ["OH_RUNTIME_EXPERIMENTAL_FEATURES"] = '{"projects":true}'
            project = await check(
                "Attach existing conversation as coordinator",
                "POST",
                "/api/projects",
                201,
                json={"name": "First", "coordinator_conversation_id": conversation_id},
            )
            await check(
                "Delete project", "DELETE", f"/api/projects/{project['id']}", 200
            )
            refused = await check(
                "Start a child from surviving coordinator",
                "POST",
                f"/api/conversations/{conversation_id}/children",
                409,
                json={"task": "Test"},
            )
            assert "Only the project's coordinator" in refused["detail"]

            profile = OpenHandsAgentProfile(name="probe", llm_profile_ref="probe")
            stores.agent_profiles.save(profile)
            project = await check(
                "Create second project without worker profile",
                "POST",
                "/api/projects",
                201,
                json={"name": "Second"},
            )
            assert project["worker_agent_profile_id"] is None
            project_path = f"/api/projects/{project['id']}"
            set_tag = service.projects.set_conversation_tag

            async def delete_before_tag(candidate_id, *args, **kwargs):
                # Schedule a real deletion between validation and the membership write.
                assert await service.delete_conversation(candidate_id)
                return await set_tag(candidate_id, *args, **kwargs)

            with patch.object(
                service.projects, "set_conversation_tag", delete_before_tag
            ):
                await check(
                    "Change coordinator and worker profile while coordinator disappears",
                    "PATCH",
                    project_path,
                    404,
                    json={
                        "coordinator_conversation_id": conversation_id,
                        "worker_agent_profile_id": str(profile.id),
                    },
                )
            after = await check(
                "Read project after failed PATCH", "GET", project_path, 200
            )
            assert after["coordinator_conversation_id"] is None
            assert UUID(after["worker_agent_profile_id"]) == profile.id
            print(
                "Failed PATCH left coordinator unset and persisted new worker profile"
            )


if __name__ == "__main__":
    with TemporaryDirectory(prefix="project-data-probe-") as scratch:
        asyncio.run(run(Path(scratch)))
