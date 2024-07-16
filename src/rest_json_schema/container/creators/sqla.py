from functools import lru_cache

from dishka import Container, make_container

from container.providers.sqla import InfraProvider, LogicProvider


@lru_cache(1)
def get_sqla_container() -> Container:
    return make_container(InfraProvider(), LogicProvider())
