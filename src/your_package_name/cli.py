"""Command-line interface for your awesome package.

This module provides a modern CLI using Typer framework with built-in help,
validation, and type hints for excellent developer experience.

Examples:
    Run the hello command:

    >>> your-package-name hello Alice
    Hello Alice! 👋

    Show version information:

    >>> your-package-name version
    your-package-name version: 0.0.0+unknown
"""

from typing import Annotated

import typer

try:
    from . import __version__
except ImportError:
    __version__ = "0.0.0+unknown"

app = typer.Typer(
    name="your-package-name",
    help="🚀 Your package description here",
    add_completion=False,
    rich_markup_mode="rich",
)


@app.command()
def hello(
    name: Annotated[
        str,
        typer.Argument(help="Name to greet"),
    ] = "World",
) -> None:
    """Say hello to someone.

    A simple greeting command to demonstrate Typer CLI framework.
    This command accepts a name and outputs a friendly greeting message.

    Args:
        name: The name of the person to greet. Defaults to 'World'.

    Returns:
        None
    """
    typer.secho(f"Hello {name}! 👋", fg=typer.colors.GREEN, bold=True)


@app.command()
def version() -> None:
    """Show version information.

    Display the current version of the your-package-name application.

    Returns:
        None
    """
    typer.echo(f"your-package-name version: {__version__}")


def main() -> None:
    """Entry point for the CLI application.

    This function serves as the main entry point and is called when the
    package is invoked as a command-line tool. It initializes and runs
    the Typer application.

    Returns:
        None
    """
    app()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
