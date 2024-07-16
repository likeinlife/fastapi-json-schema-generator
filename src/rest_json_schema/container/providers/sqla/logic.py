from dishka import Provider, Scope, provide

from domain.protocols.uow import IActivatedAppUnitOfWork, IUnitOfWork
from logic.interactors.app import AppInteractor


class LogicProvider(Provider):
    scope = Scope.APP

    @provide(scope=Scope.REQUEST)
    def _interactor(self, uow: IUnitOfWork[IActivatedAppUnitOfWork]) -> AppInteractor:
        return AppInteractor(uow=uow)
