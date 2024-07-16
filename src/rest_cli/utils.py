import typing as tp
from abc import ABCMeta
from dataclasses import dataclass


@tp.dataclass_transform()
class WrapDataclassMeta(ABCMeta):
    def __new__(  # noqa: ANN204
        cls,
        name: str,
        bases: tuple[type],
        namespace: dict[str, tp.Any],
    ):
        created = super().__new__(cls, name, bases, namespace)
        return dataclass(eq=False)(created)


@tp.dataclass_transform()
class WrapFrozenDataclassMeta(ABCMeta):
    def __new__(  # noqa: ANN204
        cls,
        name: str,
        bases: tuple[type],
        namespace: dict[str, tp.Any],
    ):
        created = super().__new__(cls, name, bases, namespace)
        return dataclass(frozen=True, eq=False)(created)
