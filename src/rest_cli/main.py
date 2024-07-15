import typing as tp
from pathlib import Path

from typer import Option, Typer

# ruff: noqa: ARG001
app = Typer(
    name="rest-cli",
    help="REST CLI model generator",
    epilog="Generate pydantic models, REST FastAPI routes from JSON-schema",
)


@app.command("models", help="Generate pydantic models")
def _models(
    json_schema: tp.Annotated[Path, Option("--json-schema", "-i")],
    out_dir: tp.Annotated[Path, Option("--out-dir", "-o")],
) -> None:
    raise NotImplementedError


@app.command("routes", help="Generate FastAPI routes")
def _routes(
    models: tp.Annotated[Path, Option("--models", "-i")],
    rest_routes: tp.Annotated[Path, Option("--routes", "-o")],
) -> None:
    raise NotImplementedError
