import sqlalchemy as sa
from sqlalchemy.ext import asyncio as sa_async

from .models import Base


def create_async_engine(url: str, echo: bool = False) -> sa_async.AsyncEngine:
    return sa_async.create_async_engine(url, echo=echo)


def create_sync_engine(url: str, echo: bool = False) -> sa.Engine:
    return sa.create_engine(url, echo=echo)


def create_async_session_maker(engine: sa_async.AsyncEngine) -> sa_async.async_sessionmaker:
    return sa_async.async_sessionmaker(bind=engine)


def create_tables(url: str) -> None:
    engine = create_sync_engine(url)
    Base.metadata.create_all(engine)
