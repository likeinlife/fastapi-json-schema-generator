from dishka import Provider, Scope, provide
from sqlalchemy.ext import asyncio as sa_async

from core.settings import get_settings
from infra.db.base import create_async_engine, create_session_maker
from infra.db.uow import UnitOfWork


class InfraProvider(Provider):
    scope = Scope.APP

    @provide
    def _engine(self) -> sa_async.AsyncEngine:
        return create_async_engine(get_settings().db.get_url())

    @provide
    def _sessionmaker(self, engine: sa_async.AsyncEngine) -> sa_async.async_sessionmaker:
        return create_session_maker(engine)

    @provide(scope=Scope.REQUEST)
    def _uow(self, session_maker: sa_async.async_sessionmaker) -> UnitOfWork:
        return UnitOfWork(session_maker)
