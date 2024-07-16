from fastapi import APIRouter

from . import format


def register(router: APIRouter) -> None:
    _to_be_included_router = APIRouter(prefix="/api/v1")

    routers: list[APIRouter] = [
        format.router,
    ]

    for _router in routers:
        _to_be_included_router.include_router(_router)

    router.include_router(_to_be_included_router)
