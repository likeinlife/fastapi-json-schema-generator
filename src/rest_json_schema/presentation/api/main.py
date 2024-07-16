import typing as tp
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core import configure_logging
from core.settings import get_settings
from core.settings.base import Settings

from . import error_handlers, middlewares, routes


def create_app(settings: Settings) -> FastAPI:
    @asynccontextmanager
    async def lifespan(_: FastAPI) -> tp.AsyncIterator[None]:
        configure_logging(settings.log.level, settings.log.json_format)
        yield

    app = FastAPI(
        title=settings.app.name,
        version=settings.app.version,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )

    error_handlers.register(app)
    middlewares.register(app)
    routes.register(app)
    return app


def default_app() -> FastAPI:
    settings = get_settings()
    return create_app(settings)
