from dataclasses import dataclass
from types import TracebackType

from sqlalchemy.ext import asyncio as sa_async

from domain.protocols.uow import IUnitOfWork

from .activated import ActivatedSQLAAppUnitOfWork


@dataclass(eq=False)
class SQLAAppUnitOfWork(IUnitOfWork[ActivatedSQLAAppUnitOfWork]):
    session_maker: sa_async.async_sessionmaker[sa_async.AsyncSession]

    async def __aenter__(self) -> ActivatedSQLAAppUnitOfWork:
        self._session = self.session_maker()
        return ActivatedSQLAAppUnitOfWork(session=self._session)

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            await self._session.rollback()
        else:
            await self._session.commit()
        await self._session.close()
