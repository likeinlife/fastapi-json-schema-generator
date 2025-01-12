# generated by datamodel-codegen:
#   filename:  format.json
#   timestamp: 2024-07-16T13:57:03+00:00

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class Specification(BaseModel):
    param_a: UUID


class Settings(BaseModel):
    param_b: UUID


class Configuration(BaseModel):
    specification: Specification
    settings: Settings


class Root(BaseModel):
    kind: Annotated[str, Field(max_length=32)]
    name: Annotated[str, Field(max_length=64)]
    version: Annotated[str, Field(max_length=10)]
    description: Annotated[str, Field(max_length=2000)]
    configuration: Configuration
