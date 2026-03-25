"""CLI entry point for HEACalculator."""

import typer

from HEACalculator.cli import app as cli_app

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(cli_app, name="search", help="Parameter search commands", no_args_is_help=True)


@app.command(name="gui")
def gui() -> None:
    """Starts the HEACalculator Graphical User Interface (GUI)."""
    from HEACalculator.app import run  # noqa: PLC0415

    run()


@app.callback(no_args_is_help=True, context_settings={"help_option_names": ["-h", "--help"]})
def main() -> None:
    """A tool for calculating High-Entropy Alloy (HEA) specific parameters and solid-solution predictions."""


if __name__ == "__main__":
    app()
