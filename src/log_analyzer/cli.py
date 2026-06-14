from typing import Any

import typer

from log_analyzer.analyzer import LogAnalyzer

app = typer.Typer()

config: dict[str, Any] = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./logs",
    "LOG_PATTERN": r"nginx_access_ui\.log_(\d{8})-\d{6}-[a-f0-9]+(?:\.gz)?$",
}


@app.command()
def main() -> None:
    log: LogAnalyzer = LogAnalyzer(config=config)
    log.metrics()


if __name__ == "__main__":
    app()
