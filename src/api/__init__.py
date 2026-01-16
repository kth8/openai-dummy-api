from .dashboard import router as dashboard_router
from .status import router as status_router
from .health import router as health_router
from .models import router as models_router
from .completions import router as completions_router

__all__ = [
    "dashboard_router",
    "status_router",
    "health_router",
    "models_router",
    "completions_router",
]
