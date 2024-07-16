import typing as tp


class IActivatedUnitOfWork(tp.Protocol):
    def _activate(self) -> None:
        """Activate repositories."""
