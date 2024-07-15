from functools import lru_cache

from dishka import Container, make_container

from .infra import InfraProvider


@lru_cache(1)
def get_container() -> Container:
    return make_container(InfraProvider())


__all__ = ("get_container",)
