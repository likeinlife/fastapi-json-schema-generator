import uuid
from dataclasses import dataclass, field

from sqlalchemy.ext import asyncio as sa_async

from domain.entities import App
from domain.enums import StateEnum
from domain.protocols.repositories.app import IAppRepository
from infra.db.models import AppModel
from infra.mappers.app import SQLAAppMapper
from infra.mappers.interfaces import ISQLAlchemyMapper


@dataclass(frozen=True, eq=False)
class AppSQLARepository(IAppRepository):
    session: sa_async.AsyncSession
    orm: type[AppModel] = field(init=False, default=AppModel)
    mapper: ISQLAlchemyMapper[App, AppModel] = field(init=False, default_factory=SQLAAppMapper)

    async def create(self, kind: str, dto: App) -> App:
        raise NotImplementedError

    async def fetch(self, kind: str, id_: uuid.UUID) -> App:
        raise NotImplementedError

    async def update_state(self, kind: str, id_: uuid.UUID, state: StateEnum) -> None:
        raise NotImplementedError

    async def delete(self, kind: str, id_: uuid.UUID) -> None:
        raise NotImplementedError

    async def update_specification(self, kind: str, id_: uuid.UUID, specification: dict) -> None:
        raise NotImplementedError

    async def update_settings(self, kind: str, id_: uuid.UUID, settings: dict) -> None:
        raise NotImplementedError
