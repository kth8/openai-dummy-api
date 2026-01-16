from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz")
async def health_check():
    return {"status": "healthy"}


@router.get("/healthz/detailed")
async def detailed_health_check():
    health = {"status": "healthy", "checks": {}}
    try:
        from ..state import dummy_state

        health["checks"]["state"] = "ok"
    except Exception as e:
        health["checks"]["state"] = f"error: {e}"
        health["status"] = "unhealthy"
    return health
