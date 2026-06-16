import tomllib
from pathlib import Path

import typer
from log_analyzer import __version__
from log_analyzer.analyzer import DEFAULT_CONFIG, LogAnalyzer

app = typer.Typer()


@app.command()
def main(config_file: Path | None = typer.Option(None, "--config", help="Path to the config file"),
         version: bool = typer.Option(False, "--version", help="Show version and exit")):

    if version:
        from log_analyzer import __version__
        typer.echo(f"log-analyzer-cli {__version__}")
        raise typer.Exit()

    config = DEFAULT_CONFIG.copy()

    if config_file and config_file.exists():
        with open(config_file, "rb") as f:
            user_config = tomllib.load(f)
        config.update(user_config)

    log = LogAnalyzer(config=config)
    log.metrics()


if __name__ == "__main__":
    app()
