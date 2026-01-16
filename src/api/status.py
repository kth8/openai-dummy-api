from fastapi import APIRouter

router = APIRouter()


@router.get("/api/status")
async def get_status():
    from ..state import dummy_state

    return dummy_state
