import uuid
from dataclasses import dataclass, field

import sqlalchemy as sa
from sqlalchemy.ext import asyncio as sa_async

from domain.entities import App
from domain.enums import StateEnum
from domain.protocols.repositories.app import IAppRepository
from domain.protocols.repositories.errors import AppNotFoundError
from infra.db.models import AppModel
from infra.mappers.app import SQLAAppMapper
from infra.mappers.interfaces import ISQLAlchemyMapper


@dataclass(frozen=True, eq=False)
class AppSQLARepository(IAppRepository):
    session: sa_async.AsyncSession
    orm: type[AppModel] = field(init=False, default=AppModel)
    mapper: ISQLAlchemyMapper[App, AppModel] = field(init=False, default_factory=SQLAAppMapper)

    async def create(self, dto: App) -> App:
        orm = self.mapper.to_orm(dto)

        self.session.add(orm)
        await self.session.flush()

        return dto

    async def fetch(self, kind: str, id_: uuid.UUID) -> App:
        query = sa.select(self.orm).where(self.orm.kind == kind, self.orm.id == id_)
        result = (await self.session.execute(query)).scalar_one_or_none()
        if not result:
            raise AppNotFoundError(kind=kind, uuid=id_)
        return self.mapper.from_orm(result)

    async def update_state(self, kind: str, id_: uuid.UUID, state: StateEnum) -> None:
        query = sa.update(self.orm).where(self.orm.kind == kind, self.orm.id == id_).values(state=state)
        (await self.session.execute(query))

    async def delete(self, kind: str, id_: uuid.UUID) -> None:
        query = sa.delete(self.orm).where(self.orm.kind == kind, self.orm.id == id_)
        (await self.session.execute(query))

    async def update_specification(self, kind: str, id_: uuid.UUID, specification: dict) -> None:
        query = sa.update(self.orm).where(self.orm.kind == kind, self.orm.id == id_).values(specification=specification)
        (await self.session.execute(query))

    async def update_settings(self, kind: str, id_: uuid.UUID, settings: dict) -> None:
        query = sa.update(self.orm).where(self.orm.kind == kind, self.orm.id == id_).values(settings=settings)
        (await self.session.execute(query))
