from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from presentation.api.errors.base import APIError


async def api_error_handler(_: Request, exc: APIError) -> ORJSONResponse:
    return ORJSONResponse(status_code=exc.status_code, content=exc.get_message())


def register(app: FastAPI) -> None:
    app.exception_handler(APIError)(api_error_handler)
