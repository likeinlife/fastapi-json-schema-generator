import typing as tp
from pathlib import Path

import typer

from .cli import check, models, routes

TEMPLATE_DIR: tp.Final[Path] = Path(__file__).parent / "templates"
app = typer.Typer(
    name="rest-cli",
    help="REST CLI model generator",
    epilog="Generate pydantic models, REST FastAPI routes from JSON-schema",
    pretty_exceptions_enable=False,
)

app.add_typer(models.router, name="models")
app.add_typer(routes.router, name="routes")
app.add_typer(check.router, name="check")
