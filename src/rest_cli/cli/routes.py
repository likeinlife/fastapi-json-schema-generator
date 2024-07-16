import typing as tp
from pathlib import Path

import jinja2
import typer

TEMPLATE_DIR: tp.Final[Path] = Path(__file__).parent.parent / "templates"
router = typer.Typer(help="Route generator")


def _generate_rest_route(template: jinja2.Template, model_path: Path, rest_route_dir: Path) -> None:
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)
    template = environment.get_template("routes.jinja2")
    kind = model_path.stem
    output_path = rest_route_dir / f"{kind}.py"

    confirm_generate = True
    if output_path.exists():
        confirm_generate = typer.confirm(f"Overwrite existing file: `{output_path}`?")
    if not confirm_generate:
        raise typer.Abort

    rest_route_dir.mkdir(parents=True, exist_ok=True)
    rendered = template.render(kind=kind)
    with output_path.open("w") as file_obj:
        file_obj.write(rendered)
    typer.echo(f"Generated: {output_path}")


@router.command("single", help="Generate FastAPI routes for specific model file")
def _routes(
    model_path: tp.Annotated[Path, typer.Option("--model-path", "-i")],
    rest_routes: tp.Annotated[Path, typer.Option("--routes", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/routes/json_schemas_rest/",
    ),
) -> None:
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)
    template = environment.get_template("routes.jinja2")

    _generate_rest_route(template, model_path, rest_routes)


@router.command("batch", help="Generate FastAPI routes for directory with models")
def _routes_all(
    models_path: tp.Annotated[Path, typer.Option("--models-path", "-i")] = Path(
        "./src/rest_json_schema/presentation/api/schemas/",
    ),
    rest_routes: tp.Annotated[Path, typer.Option("--routes", "-o")] = Path(
        "./src/rest_json_schema/presentation/api/routes/json_schemas_rest/",
    ),
) -> None:
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)
    template = environment.get_template("routes.jinja2")
    for current_model_path in models_path.glob("*.py"):
        if current_model_path.stem.startswith("_"):
            continue

        _generate_rest_route(template, current_model_path, rest_routes)
