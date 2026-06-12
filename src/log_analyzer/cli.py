import typer

from log_analyzer.analyzer import LogAnalyzer

app = typer.Typer()


config = {"REPORT_SIZE": 1000, "REPORT_DIR": "./reports", "LOG_DIR": "./log"}


@app.command()
def main(log_file: str) -> None:
    log: LogAnalyzer = LogAnalyzer(log_file)
    log.metrics()


if __name__ == "__main__":
    app()
