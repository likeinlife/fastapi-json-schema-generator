from dataclasses import dataclass

from domain.errors import BaseError


@dataclass(frozen=True, eq=False)
class SQLAWriteError(BaseError):
    entity_name: str

    @property
    def message(self) -> str:
        return f"Error on writing {self.entity_name}"
