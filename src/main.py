from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import HOST, PORT

app = FastAPI(title="OpenAI Dummy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/web/static"), name="static")

from .api.dashboard import router as dashboard_router
from .api.status import router as status_router
from .api.health import router as health_router
from .api.models import router as models_router
from .api.completions import router as completions_router

app.include_router(dashboard_router)
app.include_router(status_router)
app.include_router(health_router)
app.include_router(models_router)
app.include_router(completions_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
