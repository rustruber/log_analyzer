import tomllib
from pathlib import Path

import typer

from log_analyzer.analyzer import DEFAULT_CONFIG, LogAnalyzer

app = typer.Typer()


@app.command()
def main(config_file: Path | None = typer.Option(None, "--config", help="Путь к файлу конфига")):
    config = DEFAULT_CONFIG.copy()

    if config_file and config_file.exists():
        with open(config_file, "rb") as f:
            user_config = tomllib.load(f)
        config.update(user_config)

    log = LogAnalyzer(config=config)
    log.metrics()


if __name__ == "__main__":
    app()
