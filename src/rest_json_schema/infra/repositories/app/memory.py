import typing as tp
import uuid
from collections import defaultdict
from dataclasses import dataclass, field

from domain.entities import App
from domain.enums import StateEnum
from domain.protocols.repositories.app import IAppRepository
from domain.protocols.repositories.errors import AppNotFoundError

_AppDictType: tp.TypeAlias = dict[str, dict[uuid.UUID, App]]


@dataclass(eq=False)
class AppMemoryRepository(IAppRepository):
    apps: _AppDictType = field(default_factory=lambda: defaultdict(dict))

    async def create(self, dto: App) -> App:
        self.apps[dto.kind][dto.id] = dto
        return dto

    async def fetch(self, kind: str, id_: uuid.UUID) -> App:
        result = self.apps[kind].get(id_)
        if not result:
            raise AppNotFoundError(kind, id_)
        return result

    async def update_state(self, kind: str, id_: uuid.UUID, state: StateEnum) -> None:
        result = await self.fetch(kind, id_)
        result.state = state

    async def delete(self, kind: str, id_: uuid.UUID) -> None:
        await self.fetch(kind, id_)
        del self.apps[kind][id_]

    async def update_specification(self, kind: str, id_: uuid.UUID, specification: dict) -> None:
        result = await self.fetch(kind, id_)
        result.specification = specification

    async def update_settings(self, kind: str, id_: uuid.UUID, settings: dict) -> None:
        result = await self.fetch(kind, id_)
        result.settings = settings
