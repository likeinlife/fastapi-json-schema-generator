from __future__ import annotations

import typing as tp
from typing import Any, Mapping

if tp.TYPE_CHECKING:
    from pydantic import BaseModel


class ConfigurationProtocol(tp.Protocol):
    specification: Mapping[str, Any] | BaseModel
    settings: Mapping[str, Any] | BaseModel


class RootProtocol(tp.Protocol):
    kind: str
    name: str
    version: str
    description: str
    configuration: ConfigurationProtocol
