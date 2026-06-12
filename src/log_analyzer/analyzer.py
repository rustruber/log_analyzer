"""Анализатор логов."""

import statistics
from itertools import islice

from rich.console import Console

console = Console()


class LogAnalyzer:
    def __init__(
        self,
        log_file: str,
    ):
        # Путь к файлу логов.
        self.log_file = log_file

        # Все строки из лога в список
        self.lines: list[str] = []

        # Выборка URL адресов из лога
        self.list_logs = {}

        # Общее кол-во запросов в файле.
        self.total_lines = 0

        # Сколько раз встречается URL, абсолютное значение.
        self.count = 0.0

        # Список времён.
        self.times: list[float] = []

        # Суммарный $request_time для данного URL’а,
        # в процентах относительно общего $request_time всех
        # запросов (Часть / Целое * 100).
        self.count_perc = 0.0

        # Средний $request_time для данного URL’а.
        self.time_avg = 0.0

        # Максимальный $request_time для данного URL’а.
        self.time_max = 0.0

        # Медиана $request_time для данного URL’а.
        self.time_med = 0.0

        # Кол-во выбираемых элементов для показа.
        self.selected_items = 10

        # Сортировка вывода списка 0 - по возрастание, 1 - по убывание
        self.sorting = True

    def read_log(self):
        """Собрать все строки из лога в список (по умолчанию)."""
        with open(self.log_file) as f:
            self.lines = [line.rstrip("\n") for line in f]

    def check_url(self):
        """Выборка URL и времён из строк логов."""
        set_logs_uniq = self.lines
        for set_log in set_logs_uniq:
            parts = set_log.split()
            url = parts[6]
            try:
                req_time = float(parts[-1])
            except (ValueError, IndexError):
                continue

            if url in self.list_logs:
                self.list_logs[url]["times"].append(req_time)
                self.list_logs[url]["count"] += 1
            else:
                self.list_logs[url] = {
                    "count": 1,
                    "times": [req_time]
                }

        # Сортировка по суммарному времени (sum(times))
        self.list_logs = dict(sorted(
            self.list_logs.items(),
            key=lambda item: sum(item[1]["times"]),
            reverse=self.sorting
        ))

        # Обрезка
        self.list_logs = dict(islice(self.list_logs.items(), self.selected_items))

    def get_count(self):
        """Получить сколько раз встречается URL в выборки лога."""
        return len(self.list_logs)

    def sum_line(self):
        """Посчитать кол-во запросов в файле лога."""
        self.total_lines = len(self.lines)

    def get_total_lines(self) -> int:
        """Получить общее кол-во строк в файле лога."""
        self.sum_line()
        return self.total_lines

    def parse_log_file(self):
        """Вернуть список времён."""
        for line in self.lines:
            parts = line.split()
            time = parts[-1]
            self.times.append(float(time))

    def total_time(self) -> float:
        return sum(self.times)

    def get_selected_items(self):
        return self.selected_items

    def get_sorting(self):
        """Направление сортировки вывода списка URL-адресов."""
        return self.sorting

    def metrics(self):
        """
        Про отчет:
            • count - сколько раз встречается URL, абсолютное
            значение
            • count_perc - (количество_запросов_к_URL / общее_число_всех_запросов) * 100
            сколько раз встречается URL, в процентах
            относительно общего числа запросов
            • time_sum - суммарный $request_time для данного URL’а,
            абсолютное значение
            • time_perc - (время_на_URL / общее_время_всех_запросов) * 100
            суммарный $request_time для данного URL’а, в процентах относительно общего
            $request_time всех запросов
            • time_avg - средний $request_time для данного URL’а
            • time_max - максимальный $request_time для данного URL’
            • time_med - медианный $request_time для данного URL’
        """

        self.read_log()  # собрали все строки из лог-файла
        self.check_url()  # выбрали все URL из строк
        self.parse_log_file()
        metrica = {
            "total_lines": self.get_total_lines(),  # Общее кол-во запросов в файле лога
            "selected_items": self.get_selected_items(),  # Кол-во выбираемых элементов
            "sorting": self.get_sorting(),
            "count": self.get_count(),  # Сколько раз встречается URL, абсолютное значение
            "count_perc": self.count_perc,
            "mean": statistics.mean(self.times),
            "median": statistics.median(self.times),
            "perc_95": self.times[int(0.95 * self.get_count())],
            "min": self.times[0],
            "max": self.times[-1],
        }

        for k, v in metrica.items():
            console.print(f"{k}: {v}")

        console.print('\n---------\n')

        for k, v in islice(self.list_logs.items(), self.get_selected_items()):
            time_sum = sum(v["times"])
            time_avg = time_sum / v["count"]
            time_max = max(v["times"])
            time_med = statistics.median(v["times"])
            cp = (v["count"] / self.get_total_lines()) * 100
            tp = (sum(v["times"]) / self.total_time()) * 100
            console.print(
                f"{k}| count: {v['count']} | count_perc: {cp:.3f} | time_avg: {time_avg:.3f} | "
                f"time_max: {time_max} | time_med: {time_med} | time_perc: {tp:.3f} | "
                f"time_sum: {time_sum}")
