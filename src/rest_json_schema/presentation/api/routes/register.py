from fastapi import APIRouter, FastAPI

from . import common


def register(app: FastAPI) -> None:
    """Register all routes."""
    router = APIRouter()
    common.register(router)

    app.include_router(router)
