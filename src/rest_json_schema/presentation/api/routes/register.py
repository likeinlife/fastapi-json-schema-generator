from fastapi import APIRouter, FastAPI

from . import common, json_schemas_rest


def register(app: FastAPI) -> None:
    """Register all routes."""
    router = APIRouter()
    common.register(router)
    json_schemas_rest.register(router)

    app.include_router(router)
