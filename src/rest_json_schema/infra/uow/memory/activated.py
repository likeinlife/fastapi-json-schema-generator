import abc
from dataclasses import dataclass

from domain.protocols.uow import IActivatedAppUnitOfWork, IActivatedUnitOfWork
from infra.repositories.app.memory import AppMemoryRepository


@dataclass(eq=False)
class BaseActivatedUnitOfWork(abc.ABC, IActivatedUnitOfWork):
    def __post_init__(self) -> None:
        self._activate()

    @abc.abstractmethod
    def _activate(self) -> None: ...


@dataclass(eq=False)
class ActivatedMemoryAppUnitOfWork(BaseActivatedUnitOfWork, IActivatedAppUnitOfWork):
    def _activate(self) -> None:
        self.app = AppMemoryRepository()
