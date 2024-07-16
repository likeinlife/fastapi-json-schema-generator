import typing as tp
from uuid import UUID

from fastapi import status

from .base import APIError


class APIAppNotFoundError(APIError):
    kind: str
    uuid: UUID
    status_code: int = status.HTTP_404_NOT_FOUND

    def get_message(self) -> dict[str, tp.Any]:
        return {
            "message": f"App with kind={self.kind} and uuid={self.uuid} not found",
            "uuid": self.uuid,
            "kind": self.kind,
        }
