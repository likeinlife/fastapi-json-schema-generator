import typing as tp

from dishka import Container
from fastapi import Depends

from container.creators import get_container


async def get_activated_container(
    container: tp.Annotated[Container, Depends(get_container)],
) -> tp.AsyncIterator[Container]:
    with container() as active:
        yield active
