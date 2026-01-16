from fastapi import APIRouter

router = APIRouter()


@router.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "gpt-3.5-turbo",
                "object": "model",
                "created": 1677610602,
                "owned_by": "openai",
            },
            {
                "id": "gpt-4",
                "object": "model",
                "created": 1687882411,
                "owned_by": "openai",
            },
        ],
    }
