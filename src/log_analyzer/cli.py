from rich.console import Console
from log_analyzer import utils

app = typer.Typer()
console = Console()

# Количество запросов — сколько всего строк с временем ответа
# Среднее время — сумма всех времён / количество
# Медиану — среднее значение в отсортированном списке
# 95-й персентиль — значение, ниже которого 95% всех времён
# Минимум — самое маленькое время
# Максимум — самое большое время
@app.command()
def main(log_file: str) -> None:
    utils.do_something_useful(log_file, console)


if __name__ == "__main__":
    app()

