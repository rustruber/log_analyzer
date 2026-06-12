import statistics


def read_file_log(path_log_file: str, as_set: bool = False) -> list[str] | set[str]:
    """Собрать все строки из лога в список (по умолчанию) или множество уникальных."""
    with open(path_log_file) as f:
        lines = [line.rstrip("\n") for line in f]
    return set(lines) if as_set else lines


def check_url(path_log_file: str):
    """Выборка URL адресов из строк."""
    list_logs = {}
    set_logs_uniq = read_file_log(path_log_file, True)
    for set_log in set_logs_uniq:
        list_logs[set_log[6]] = set_log[-1]
    return list_logs


def parse_log_file(log_file: str) -> list[float]:
    """Прочитать файл и вернуть список времён"""
    times = []
    with open(log_file) as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            time = parts[-1]
            times.append(float(time))
    return times


def calculate_metrics(times: list[float]) -> dict:
    """Посчитать метрики по списку времён"""
    if not times:
        return {"error": "Нет данных"}

    times.sort()
    count = len(times)

    return {
        "count": count,
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "perc_95": times[int(0.95 * count)],
        "min": times[0],
        "max": times[-1],
    }


def do_something_useful(log_file: str, console) -> None:
    times = parse_log_file(log_file)
    metrics = calculate_metrics(times)
    for k, v in metrics.items():
        console.print(f"{k}: {v}")
