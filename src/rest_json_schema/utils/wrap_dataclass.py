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
class WrapKWDataclassMeta(ABCMeta):
    def __new__(  # noqa: ANN204
        cls,
        name: str,
        bases: tuple[type],
        namespace: dict[str, tp.Any],
    ):
        created = super().__new__(cls, name, bases, namespace)
        return dataclass(eq=False, kw_only=True)(created)
