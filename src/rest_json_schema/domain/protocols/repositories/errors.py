from uuid import UUID

from domain.errors import DomainError


class AppNotFoundError(DomainError):
    kind: str
    uuid: UUID

    @property
    def message(self) -> str:
        return f"App with kind={self.kind} and uuid={self.uuid} not found"
