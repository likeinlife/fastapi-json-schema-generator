from dishka import Provider, Scope, provide

from domain.protocols.uow import IActivatedAppUnitOfWork, IUnitOfWork
from infra.uow.memory.uow import MemoryAppUnitOfWork
from logic.interactors.app import AppInteractor


class MemoryProvider(Provider):
    scope = Scope.APP

    @provide
    def _uow(self) -> IUnitOfWork[IActivatedAppUnitOfWork]:
        return MemoryAppUnitOfWork()

    @provide
    def _interactor(self, uow: IUnitOfWork[IActivatedAppUnitOfWork]) -> AppInteractor:
        return AppInteractor(uow=uow)
