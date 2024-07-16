from functools import lru_cache

from .base import Settings


@lru_cache(1)
def get_settings() -> Settings:
    return Settings()


__all__ = ("Settings", "get_settings")
