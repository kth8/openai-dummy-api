from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def dashboard():
    from ..web.templates import DASHBOARD_HTML

    return HTMLResponse(content=DASHBOARD_HTML)
