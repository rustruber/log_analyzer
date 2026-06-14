import tomllib  # Python 3.11+, если версия ниже — используй tomli
from pathlib import Path

import typer

from log_analyzer.analyzer import DEFAULT_CONFIG, LogAnalyzer

app = typer.Typer()


@app.command()
def main(config_file: Path | None = None):
    config = DEFAULT_CONFIG.copy()

    if config_file and config_file.exists():
        with open(config_file, "rb") as f:
            user_config = tomllib.load(f)
        config.update(user_config)  # обновляем значения из файла

    log = LogAnalyzer(config=config)
    log.metrics()


if __name__ == "__main__":
    app()
