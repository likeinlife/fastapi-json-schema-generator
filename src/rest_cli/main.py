import typing as tp
from pathlib import Path

import typer
from datamodel_code_generator import DataModelType, InputFileType, PythonVersion, generate

from .constants import ROOT_NAME
from .errors import InputFilePathNotFoundError

# ruff: noqa: ARG001
app = typer.Typer(
    name="rest-cli",
    help="REST CLI model generator",
    epilog="Generate pydantic models, REST FastAPI routes from JSON-schema",
    pretty_exceptions_enable=False,
)


@app.command("models", help="Generate pydantic models")
def _models(
    json_path: tp.Annotated[Path, typer.Option("--json-schema", "-i")],
    out_dir: tp.Annotated[Path, typer.Option("--out-dir", "-o")],
) -> None:
    if not json_path.exists():
        raise InputFilePathNotFoundError(json_path)
    output_path = out_dir / f"{json_path.stem}.py"
    if output_path.exists():
        confirm_generate = typer.confirm("Overwrite existing file?")
    out_dir.mkdir(parents=True, exist_ok=True)

    confirm_generate = True
    if not confirm_generate:
        raise typer.Abort

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


@app.command("routes", help="Generate FastAPI routes")
def _routes(
    models: tp.Annotated[Path, typer.Option("--models", "-i")],
    rest_routes: tp.Annotated[Path, typer.Option("--routes", "-o")],
) -> None:
    raise NotImplementedError
