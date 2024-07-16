import typing as tp
from pathlib import Path

import typer
from datamodel_code_generator import DataModelType, InputFileType, PythonVersion, generate

from rest_cli.constants import ROOT_NAME
from rest_cli.errors import InputFilePathNotFoundError

router = typer.Typer(help="Generate pydantic models")


def _generate_models(json_path: Path, out_dir: Path) -> None:
    if not json_path.exists():
        raise InputFilePathNotFoundError(json_path)
    output_path = out_dir / f"{json_path.stem}.py"

    confirm_generate = True
    if output_path.exists():
        confirm_generate = typer.confirm("Overwrite existing file?")
    if not confirm_generate:
        raise typer.Abort
    out_dir.mkdir(parents=True, exist_ok=True)

    with json_path.open() as file_obj:
        content = file_obj.read()

    generate(
        content,
        input_file_type=InputFileType.JsonSchema,
        input_filename=json_path.name,
        output=output_path,
        output_model_type=DataModelType.PydanticV2BaseModel,
        snake_case_field=True,
        use_annotated=True,
        use_generic_container_types=True,
        target_python_version=PythonVersion.PY_312,
        field_constraints=True,
        use_field_description=True,
        class_name=ROOT_NAME,
    )
    typer.echo(f"Generated: {output_path}")


@router.command("single", help="Generate pydantic models from single json-schema")
def _models(
    json_path: tp.Annotated[Path, typer.Option("--json-schema", "-i")],
    out_dir: tp.Annotated[Path, typer.Option("--out-dir", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/schemas/",
    ),
) -> None:
    _generate_models(json_path, out_dir)


@router.command("batch", help="Generate pydantic models from batch json-schema")
def _models_batch(
    json_dir: tp.Annotated[Path, typer.Option("--json-dir", "-i")],
    out_dir: tp.Annotated[Path, typer.Option("--out-dir", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/schemas/",
    ),
) -> None:
    for current_json_path in json_dir.glob("*.json"):
        _generate_models(current_json_path, out_dir)
