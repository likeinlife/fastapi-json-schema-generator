import typing as tp

from domain.protocols.repositories import IAppRepository

from .base import IActivatedUnitOfWork


class IActivatedAppUnitOfWork(IActivatedUnitOfWork, tp.Protocol):
    app: IAppRepository
