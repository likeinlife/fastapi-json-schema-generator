from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from domain.errors import DomainError
from domain.protocols.repositories.errors import AppNotFoundError
from presentation.api.errors.app import APIAppNotFoundError


async def domain_error_handler(_: Request, exc: DomainError) -> ORJSONResponse:
    if isinstance(exc, AppNotFoundError):
        api_error = APIAppNotFoundError(kind=exc.kind, uuid=exc.uuid)
        return ORJSONResponse(status_code=api_error.status_code, content=api_error.get_message())

    return ORJSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=exc.message)


def register(app: FastAPI) -> None:
    app.exception_handler(DomainError)(domain_error_handler)
