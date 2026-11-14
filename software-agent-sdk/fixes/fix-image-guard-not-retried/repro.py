"""Native DeepSeek image-loss guard: error class, retries and requests sent.

A real `LLM` talks to a local OpenAI-compatible endpoint; no key is needed.
"""

import asyncio
import json
import time

from S02.fake_provider import FakeProvider
from sdk_verify import emit

from openhands.sdk import LLM
from openhands.sdk.llm import ImageContent, Message, MessageToolCall, TextContent


IMAGE = (
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAA"
    "C0lEQVR42mP8/x8AAusB9Wl6XioAAAAASUVORK5CYII="
)
USER = [
    Message(
        role="user",
        content=[TextContent(text="describe"), ImageContent(image_urls=[IMAGE])],
    )
]
TOOL = [
    Message(role="user", content=[TextContent(text="take a screenshot")]),
    Message(
        role="assistant",
        content=[TextContent(text="")],
        tool_calls=[
            MessageToolCall(id="c1", name="shot", arguments="{}", origin="completion")
        ],
    ),
    Message(
        role="tool",
        tool_call_id="c1",
        name="shot",
        content=[TextContent(text="shot"), ImageContent(image_urls=[IMAGE])],
    ),
]


def run(model: str, shape: str, use_async: bool) -> dict:
    retries: list[int] = []
    with FakeProvider([{"text": "ok"}] * 8) as server:
        llm = LLM(
            model=model,
            api_key="local-test",
            base_url=server.url,
            num_retries=3,
            retry_min_wait=0,
            retry_max_wait=0,
            retry_listener=lambda attempt, total, error: retries.append(attempt),
        )
        msgs = USER if shape == "user" else TOOL
        started = time.monotonic()
        try:
            if use_async:
                asyncio.run(llm.acompletion(msgs))
            else:
                llm.completion(msgs)
            error = cause = None
        except Exception as exc:
            error = f"{type(exc).__name__}: {str(exc)[:110]}"
            cause = type(exc.__cause__).__name__ if exc.__cause__ else None
        return {
            "model": model,
            "image_in": shape,
            "api": "acompletion" if use_async else "completion",
            "vision_is_active": llm.vision_is_active(),
            "error": error,
            "cause": cause,
            "retries": len(retries),
            "requests_sent": len(server.requests),
            "images_in_sent_body": json.dumps(
                [r["body"] for r in server.requests]
            ).count('"image_url"')
            // 2
            if server.requests
            else None,
            "seconds": round(time.monotonic() - started, 2),
        }


rows = [
    run(model, shape, use_async)
    for model in ("deepseek/deepseek-v4.1-flash", "deepseek/deepseek-chat")
    for shape in ("user", "tool")
    for use_async in (False, True)
]
for row in rows:
    print(json.dumps(row))
emit({"rows": rows})
