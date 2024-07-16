import typing as tp

from dishka import Container
from fastapi import Depends

from logic.interactors.app import AppInteractor

from .container import get_activated_container


async def get_interactor(
    container: tp.Annotated[Container, Depends(get_activated_container)],
) -> AppInteractor:
    return container.get(AppInteractor)
