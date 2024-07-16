import typing as tp
from types import TracebackType

from .activated import IActivatedUnitOfWork

Activated_co = tp.TypeVar("Activated_co", bound=IActivatedUnitOfWork, covariant=True)


class IUnitOfWork(tp.Generic[Activated_co], tp.Protocol):
    async def __aenter__(self) -> Activated_co: ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
