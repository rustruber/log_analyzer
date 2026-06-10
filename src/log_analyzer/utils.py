import statistics


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

    # print("Количество запросов (всего обработано запросов):", count)
    # print("Среднее время:", sum_all / count)
    # print(f"Медиана (половина пользователей получила ответ быстрее {median} миллисекунды)")
    #
    # # Минимум и максимум
    # print(f"Минимум (самый быстрый запрос): {times[0]}")
    # print(f"Максимум (самый медленный запрос): {times[-1]}")
    #
    # # 95-й персентиль
    # time_perc = times[int(0.95 * count)]
    # print(f"95-й персентиль (5% самых медленных запросов были медленнее {time_perc} секунд)")
