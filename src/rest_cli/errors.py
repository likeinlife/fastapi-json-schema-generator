from abc import abstractmethod
from pathlib import Path

from rest_cli.utils import WrapDataclassMeta


class BaseError(Exception, metaclass=WrapDataclassMeta):
    """Base error.

    Note: use WrapDataclassMeta to wrap dataclass.
    """

    @property
    @abstractmethod
    def message(self) -> str: ...

    def __str__(self) -> str:
        """Return error message."""
        return self.message


class InputFilePathNotFoundError(BaseError):
    """File not found error."""

    file_path: Path

    @property
    def message(self) -> str:
        return f"File {self.file_path} not found"
