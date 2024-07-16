import abc
from dataclasses import dataclass

from sqlalchemy.ext import asyncio as sa_async

from domain.protocols.uow import IActivatedAppUnitOfWork, IActivatedUnitOfWork
from infra.repositories.app.sqla import AppSQLARepository


@dataclass(eq=False)
class BaseActivatedUnitOfWork(abc.ABC, IActivatedUnitOfWork):
    session: sa_async.AsyncSession

    def __post_init__(self) -> None:
        self._activate()

    @abc.abstractmethod
    def _activate(self) -> None: ...


@dataclass(eq=False)
class ActivatedSQLAAppUnitOfWork(BaseActivatedUnitOfWork, IActivatedAppUnitOfWork):
    def _activate(self) -> None:
        self.app = AppSQLARepository(session=self.session)
