import typing as tp
from dataclasses import dataclass, field

from pydantic import BaseModel

from domain.enums import StateEnum
from domain.protocols.schemas import RootProtocol

from .base import BaseEntity


@dataclass(eq=False)
class App(BaseEntity):
    kind: str
    name: str
    version: str
    description: str
    specification: tp.Mapping[str, tp.Any]
    settings: tp.Mapping[str, tp.Any]
    state: StateEnum = field(default=StateEnum.new)

    @classmethod
    def from_root(cls, kind: str, root: RootProtocol) -> "App":
        specification = root.configuration.specification
        settings = root.configuration.settings
        specification_dumped = (
            specification.model_dump(mode="json") if isinstance(specification, BaseModel) else (specification)
        )
        settings_dumped = settings.model_dump(mode="json") if isinstance(settings, BaseModel) else (settings)
        return cls(
            kind=kind,
            name=root.name,
            version=root.version,
            description=root.description,
            specification=specification_dumped,
            settings=settings_dumped,
            state=StateEnum.new,
        )
