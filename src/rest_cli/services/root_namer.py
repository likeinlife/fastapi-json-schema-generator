import typing as tp


class RootNamerService:
    root_suffix: tp.ClassVar[str] = "IsRoot"

    @classmethod
    def create_name(cls, name: str) -> str:
        return name + cls.root_suffix

    @classmethod
    def check_name(cls, name: str) -> bool:
        return name.endswith(cls.root_suffix)

    @classmethod
    def get_original_name(cls, name: str) -> str:
        return name.removesuffix(cls.root_suffix)
