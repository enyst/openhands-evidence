"""Same request with the default retry settings: how long does the caller wait?"""

import time

from S02.fake_provider import FakeProvider
from sdk_verify import emit

from openhands.sdk import LLM
from openhands.sdk.llm import ImageContent, Message, TextContent


IMAGE = (
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAA"
    "C0lEQVR42mP8/x8AAusB9Wl6XioAAAAASUVORK5CYII="
)
retries: list[int] = []
with FakeProvider([{"text": "ok"}] * 8) as server:
    llm = LLM(
        model="deepseek/deepseek-v4.1-flash",
        api_key="local-test",
        base_url=server.url,
        retry_listener=lambda attempt, total, error: retries.append(attempt),
    )
    started = time.monotonic()
    try:
        llm.completion(
            [
                Message(
                    role="user",
                    content=[
                        TextContent(text="describe"),
                        ImageContent(image_urls=[IMAGE]),
                    ],
                )
            ]
        )
        error = None
    except Exception as exc:
        error = type(exc).__name__
    emit(
        {
            "num_retries": llm.num_retries,
            "error": error,
            "retries": len(retries),
            "requests_sent": len(server.requests),
            "seconds": round(time.monotonic() - started, 1),
        }
    )
