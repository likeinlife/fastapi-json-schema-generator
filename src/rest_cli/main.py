import typing as tp
from pathlib import Path

import jinja2
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
    out_dir: tp.Annotated[Path, typer.Option("--out-dir", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/schemas/",
    ),
) -> None:
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


@app.command("routes", help="Generate FastAPI routes for specific model file")
def _routes(
    models_path: tp.Annotated[Path, typer.Option("--models-path", "-i")],
    rest_routes: tp.Annotated[Path, typer.Option("--routes", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/routes/json_schemas_rest/",
    ),
) -> None:
    environment = jinja2.Environment(loader=jinja2.PackageLoader("templates"), autoescape=True)
    template = environment.get_template("routes.jinja2")
    kind = models_path.stem
    output_path = rest_routes / f"{kind}.py"

    confirm_generate = True
    if output_path.exists():
        confirm_generate = typer.confirm("Overwrite existing file?")
    if not confirm_generate:
        raise typer.Abort

    rest_routes.mkdir(parents=True, exist_ok=True)
    rendered = template.render(kind=kind)
    with output_path.open("w") as file_obj:
        file_obj.write(rendered)
    typer.echo(f"Generated: {output_path}")


@app.command("routes", help="Generate FastAPI routes for specific model file")
def _routes_all(
    models_path: tp.Annotated[Path, typer.Option("--models-path", "-i")] = Path(
        "./src/rest_json_schema/presentation/api/schemas/",
    ),
    rest_routes: tp.Annotated[Path, typer.Option("--routes", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/routes/json_schemas_rest/",
    ),
) -> None:
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("src/rest_cli/templates"), autoescape=True)
    template = environment.get_template("routes.jinja2")
    kind = models_path.stem
    output_path = rest_routes / f"{kind}.py"

    confirm_generate = True
    if output_path.exists():
        confirm_generate = typer.confirm("Overwrite existing file?")
    if not confirm_generate:
        raise typer.Abort

    rest_routes.mkdir(parents=True, exist_ok=True)
    rendered = template.render(kind=kind)
    with output_path.open("w") as file_obj:
        file_obj.write(rendered)
    typer.echo(f"Generated: {output_path}")
