from utils.wrap_dataclass import WrapDataclassMeta


class BaseError(Exception, metaclass=WrapDataclassMeta):
    """Base error."""

    @property
    def message(self) -> str:
        return "Base error message"

    def __str__(self) -> str:
        """Return error message."""
        return self.message


class DomainError(BaseError):
    """Domain error."""

    @property
    def message(self) -> str:
        return "Domain error message"
