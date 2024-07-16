from functools import lru_cache

from dishka import Container, make_container

from container.providers.memory import MemoryProvider


@lru_cache(1)
def get_memory_container() -> Container:
    return make_container(MemoryProvider())
