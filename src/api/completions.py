import time
import json
import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ..models import ChatCompletionRequest

router = APIRouter()


async def stream_generator(model_name: str, state):
    from ..config import HOST, PORT

    response_id = f"chatcmpl-{int(time.time())}"
    text = f"""
Request received at http://{HOST}:{PORT}
System prompt tokens: {state["system_prompt_tokens"]}
User prompt tokens: {state["user_prompt_tokens"]}
Tool definition tokens: {state["tools_tokens_compact"]}
Total tokens: {state["total_tokens"]}
Number of tools: {len(state["tools_defined"])}
{", ".join([tool["function"]["name"] for tool in state["tools_defined"]])}
"""

    tokens = text.split(" ")

    for i, token in enumerate(tokens):
        content_chunk = token + (" " if i < len(tokens) - 1 else "")
        chunk_data = {
            "id": response_id,
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model_name,
            "choices": [
                {"index": 0, "delta": {"content": content_chunk}, "finish_reason": None}
            ],
        }
        yield f"data: {json.dumps(chunk_data)}\n\n"
        await asyncio.sleep(0.02)

    final_chunk = {
        "id": response_id,
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model_name,
        "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
    }
    yield f"data: {json.dumps(final_chunk)}\n\n"
    yield "data: [DONE]\n\n"


@router.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    from ..tokenizer import get_content_string
    from ..config import encoder
    from ..state import dummy_state

    system_prompt_str = "No system prompt found."
    for msg in request.messages:
        if msg.role == "system":
            system_prompt_str = get_content_string(msg.content)
            if not system_prompt_str:
                system_prompt_str = "[Empty System Prompt]"
            break

    user_prompt_str = "No user prompt found."
    for msg in reversed(request.messages):
        if msg.role == "user":
            user_prompt_str = get_content_string(msg.content)
            if not user_prompt_str:
                user_prompt_str = "[Empty User Prompt]"
            break

    captured_tools = request.tools if request.tools else []

    sys_tokens_count = len(encoder.encode(system_prompt_str))
    user_tokens_count = len(encoder.encode(user_prompt_str))

    if captured_tools:
        json_compact = json.dumps(captured_tools, separators=(",", ":"))
        tokens_compact = len(encoder.encode(json_compact))

        json_indented = json.dumps(captured_tools, indent=2)
        tokens_indented = len(encoder.encode(json_indented))
    else:
        tokens_compact = 0
        tokens_indented = 0

    dummy_state.update(
        {
            "latest_system_prompt": system_prompt_str,
            "system_prompt_tokens": sys_tokens_count,
            "latest_user_prompt": user_prompt_str,
            "user_prompt_tokens": user_tokens_count,
            "tools_defined": captured_tools,
            "tools_tokens_compact": tokens_compact,
            "tools_tokens_indented": tokens_indented,
            "total_tokens": sys_tokens_count + user_tokens_count + tokens_compact,
            "model_requested": request.model,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    print(f"Captured: Model={request.model}")

    if request.stream:
        return StreamingResponse(
            stream_generator(request.model, dummy_state),
            media_type="text/event-stream",
        )

    from ..config import HOST, PORT

    return {
        "id": f"chatcmpl-{int(time.time())}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": f"""Request received at http://{HOST}:{PORT}
System prompt tokens: {sys_tokens_count}
User prompt tokens: {user_tokens_count}
Tool definition tokens: {tokens_compact}
Total tokens: {sys_tokens_count + user_tokens_count + tokens_compact}
Number of tools: {len(captured_tools)}
{", ".join([tool["function"]["name"] for tool in captured_tools])}""",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": sys_tokens_count + user_tokens_count + tokens_compact,
            "completion_tokens": 0,
            "total_tokens": sys_tokens_count + user_tokens_count + tokens_compact,
        },
    }
