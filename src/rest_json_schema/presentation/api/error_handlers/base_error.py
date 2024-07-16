from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from domain.errors import BaseError


async def app_error_handler(_: Request, exc: BaseError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": exc.message,
        },
    )


def register(app: FastAPI) -> None:
    app.exception_handler(BaseError)(app_error_handler)
