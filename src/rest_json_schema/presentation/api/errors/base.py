import abc
import typing as tp

from utils.wrap_dataclass import WrapKWDataclassMeta


@tp.dataclass_transform(kw_only_default=True)
class ABCDataclassMeta(WrapKWDataclassMeta, abc.ABCMeta): ...


class APIError(Exception, metaclass=ABCDataclassMeta):
    status_code: int

    @abc.abstractmethod
    def get_message(self) -> dict[str, tp.Any]: ...
