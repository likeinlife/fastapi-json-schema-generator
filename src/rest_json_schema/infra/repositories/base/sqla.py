import typing as tp
import uuid
from dataclasses import dataclass

import sqlalchemy as sa
import structlog
from sqlalchemy import exc
from sqlalchemy.ext import asyncio as sa_async

from domain.entities.base import BaseEntity
from infra.db.base import Base
from infra.mappers.interfaces import ISQLAlchemyMapper
from infra.repositories.base.errors import SQLAWriteError

DTO = tp.TypeVar("DTO", bound=BaseEntity)
ORM = tp.TypeVar("ORM", bound=Base)


@dataclass(frozen=True, eq=False)
class BaseSQLAlchemyRepository(tp.Generic[DTO, ORM]):
    session: sa_async.AsyncSession
    orm: type[ORM]
    mapper: ISQLAlchemyMapper[DTO, ORM]

    _logger = structlog.get_logger()

    async def _fetch_list(self, limit: int, offset: int) -> list[DTO]:
        query = sa.select(self.orm).limit(limit).offset(offset)
        result = (await self.session.execute(query)).scalars()
        return [self.mapper.from_orm(row) for row in result]

    async def _fetch_by_id(self, id_: uuid.UUID) -> DTO | None:
        query = sa.select(self.orm).where(self.orm.id == id_)
        result = await self.session.scalar(query)
        if not result:
            return None
        return self.mapper.from_orm(result)

    async def _add(self, dto: DTO) -> DTO:
        orm = self.mapper.to_orm(dto)
        self.session.add(orm)
        try:
            await self.session.flush()
            await self.session.refresh(orm)
        except exc.IntegrityError:
            self._logger.exception("Integrity error", dto=type(dto))
            raise SQLAWriteError(entity_name=type(dto).__name__)

        return self.mapper.from_orm(orm)
