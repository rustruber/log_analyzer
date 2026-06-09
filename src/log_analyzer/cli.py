"""Console script for log_analyzer."""

import typer
from rich.console import Console

from log_analyzer import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for log_analyzer."""
    console.print("Replace this message by putting your code into log_analyzer.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
