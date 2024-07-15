from rest_cli.constants import ROOT_NAME


class RootNamerService:
    @classmethod
    def check_name(cls, name: str) -> bool:
        return name == ROOT_NAME
