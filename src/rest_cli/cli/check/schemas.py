from __future__ import annotations

from typing import Any

from pydantic import BaseModel

# ruff: noqa: N815


class Kind(BaseModel):
    type: str


class Name(BaseModel):
    type: str


class Version(BaseModel):
    type: str


class Description(BaseModel):
    type: str


class Specification(BaseModel):
    type: str
    properties: dict[str, Any]
    required: list[str]


class Settings(BaseModel):
    type: str
    properties: dict[str, Any]
    required: list[str]


class Properties1(BaseModel):
    specification: Specification
    settings: Settings


class Configuration(BaseModel):
    type: str
    properties: Properties1
    required: list[str]


class Properties(BaseModel):
    kind: Kind
    name: Name
    version: Version
    description: Description
    configuration: Configuration


class Model(BaseModel):
    properties: Properties
    required: list[str]
