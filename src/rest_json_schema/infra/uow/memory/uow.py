from dataclasses import dataclass
from types import TracebackType

from domain.protocols.uow import IUnitOfWork

from .activated import ActivatedMemoryAppUnitOfWork


@dataclass(eq=False)
class MemoryAppUnitOfWork(IUnitOfWork[ActivatedMemoryAppUnitOfWork]):
    activated = ActivatedMemoryAppUnitOfWork()

    async def __aenter__(self) -> ActivatedMemoryAppUnitOfWork:
        return self.activated

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
