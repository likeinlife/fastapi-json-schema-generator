import uuid
from dataclasses import dataclass

from domain.entities.app import App
from domain.enums import StateEnum
from domain.protocols.uow import IActivatedAppUnitOfWork, IUnitOfWork


@dataclass
class AppInteractor:
    uow: IUnitOfWork[IActivatedAppUnitOfWork]

    async def create(self, app: App) -> App:
        async with self.uow as activated:
            return await activated.app.create(app)

    async def fetch(self, kind: str, id_: uuid.UUID) -> App:
        async with self.uow as activated:
            return await activated.app.fetch(kind, id_)

    async def fetch_state(self, kind: str, id_: uuid.UUID) -> StateEnum:
        async with self.uow as activated:
            return (await activated.app.fetch(kind, id_)).state

    async def delete(self, kind: str, id_: uuid.UUID) -> None:
        async with self.uow as activated:
            await activated.app.delete(kind, id_)

    async def update_state(self, kind: str, id_: uuid.UUID, state: StateEnum) -> None:
        async with self.uow as activated:
            await activated.app.update_state(kind, id_, state)

    async def update_settings(self, kind: str, id_: uuid.UUID, settings: dict) -> None:
        async with self.uow as activated:
            return await activated.app.update_settings(kind, id_, settings)

    async def update_specification(self, kind: str, id_: uuid.UUID, specification: dict) -> None:
        async with self.uow as activated:
            return await activated.app.update_specification(kind, id_, specification)
