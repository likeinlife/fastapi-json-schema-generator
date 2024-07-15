from pathlib import Path

import yaml
from pydantic import TypeAdapter

from .schemas import InputRoot, Root, Settings, Specification


def load_yaml_specification(yaml_path: Path) -> Root:
    with yaml_path.open() as file_obj:
        obj = yaml.load(stream=file_obj, Loader=yaml.SafeLoader)

    specification = TypeAdapter(Specification).validate_json(obj["configuration"]["specification"])
    settings = TypeAdapter(Settings).validate_json(obj["configuration"]["settings"])

    input_root = TypeAdapter(InputRoot).validate_python(obj)

    return Root.from_input(input_root, specification, settings)
