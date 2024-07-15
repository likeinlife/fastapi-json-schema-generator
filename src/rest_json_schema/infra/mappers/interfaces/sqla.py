import abc
import typing as tp

from domain.entities.base import BaseEntity
from infra.db.base import Base

DTO = tp.TypeVar("DTO", bound=BaseEntity)
ORM = tp.TypeVar("ORM", bound=Base)


class ISQLAlchemyMapper(abc.ABC, tp.Generic[DTO, ORM]):
    @abc.abstractmethod
    def from_orm(self, orm: ORM) -> DTO: ...

    @abc.abstractmethod
    def to_orm(self, dto: DTO) -> ORM: ...
