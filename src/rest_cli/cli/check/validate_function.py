from pathlib import Path

from pydantic import TypeAdapter

from .schemas import Model


def validate_json_schema(json_path: Path) -> None:
    with json_path.open() as file_obj:
        content = file_obj.read()

    TypeAdapter(Model).validate_json(content)
