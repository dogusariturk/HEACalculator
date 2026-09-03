"""CLI entry point for HEACalculator."""

from importlib.metadata import version as _get_version

import typer

from HEACalculator.cli import app as cli_app

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(cli_app, name="search", help="Parameter search commands", no_args_is_help=True)


def _version_callback(value: bool) -> None:
    """Print the installed HEACalculator version and exit.

    Args:
        value (bool): Whether ``--version``/``-V`` was passed.
    """
    if value:
        typer.echo(f"HEACalculator {_get_version('HEACalculator')}")
        raise typer.Exit()


@app.command(name="gui")
def gui() -> None:
    """Starts the HEACalculator Graphical User Interface (GUI)."""
    from HEACalculator.app import run  # noqa: PLC0415

    run()


@app.callback(no_args_is_help=True, context_settings={"help_option_names": ["-h", "--help"]})
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show the HEACalculator version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    """A tool for calculating High-Entropy Alloy (HEA) specific parameters and solid-solution predictions."""


if __name__ == "__main__":
    app()
