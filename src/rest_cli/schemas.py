import typing as tp

from pydantic import BaseModel, computed_field

from rest_cli.services import RootNamerService


class Specification(BaseModel):
    properties: dict[str, tp.Any]

    @computed_field
    def required(self) -> list[str]:
        return list(self.properties.keys())


class Settings(BaseModel):
    properties: dict[str, tp.Any]

    @computed_field
    def required(self) -> list[str]:
        return list(self.properties.keys())


class Properties(BaseModel):
    settings: Settings
    specification: Specification


class InputRoot(BaseModel):
    kind: str
    name: str
    version: str
    description: str


class Root(BaseModel):
    properties: Properties
    title: str

    @classmethod
    def from_input(
        cls,
        input_root: InputRoot,
        specification: Specification,
        settings: Settings,
    ) -> "Root":
        return cls(
            title=RootNamerService.create_name(input_root.kind),
            properties=Properties(settings=settings, specification=specification),
        )

    @computed_field
    def required(self) -> list[str]:
        return ["settings", "specification"]
