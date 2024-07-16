import typing as tp
from pathlib import Path

import typer
from pydantic import TypeAdapter, ValidationError

from .schemas import Model

router = typer.Typer(help="Check json-schema")


def _check_json_schema(json_path: Path) -> None:
    with json_path.open() as file_obj:
        content = file_obj.read()

    TypeAdapter(Model).validate_json(content)


@router.command("single", help="Check single json-schema")
def _check(
    json_path: tp.Annotated[Path, typer.Option("--json-schema", "-i")],
    verbose: tp.Annotated[bool, typer.Option("--verbose", "-v")] = False,
) -> None:
    try:
        _check_json_schema(json_path)
    except ValidationError as e:
        typer.secho(f"Invalid JSON-schema: {json_path}", fg=typer.colors.RED)
        if verbose:
            typer.echo(e)


@router.command("batch", help="Check batch of json-schemas")
def _check_batch(
    json_dir: tp.Annotated[Path, typer.Option("--json-dir", "-i")],
    verbose: tp.Annotated[bool, typer.Option("--verbose", "-v")] = False,
) -> None:
    for current_json_path in json_dir.glob("*.json"):
        try:
            _check_json_schema(current_json_path)
        except ValidationError as e:  # noqa: PERF203
            typer.secho(f"Invalid JSON-schema: {current_json_path}", fg=typer.colors.RED)
            if verbose:
                typer.echo(e)
