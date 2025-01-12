# generated by datamodel-codegen:
#   filename:  specific_format.json
#   timestamp: 2024-07-16T13:57:04+00:00

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class Specification(BaseModel):
    a: int


class Settings(BaseModel):
    b: int


class Configuration(BaseModel):
    specification: Specification
    settings: Settings


class Root(BaseModel):
    kind: Annotated[str, Field(max_length=32)]
    name: Annotated[str, Field(max_length=64)]
    version: Annotated[str, Field(max_length=10)]
    description: Annotated[str, Field(max_length=2000)]
    configuration: Configuration
