"""Анализатор логов."""

import statistics

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

        # Общее кол-во строк в файле.
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

    def read_log(self):
        """Собрать все строки из лога в список (по умолчанию)."""
        with open(self.log_file) as f:
            self.lines = [line.rstrip("\n") for line in f]

    def check_url(self):
        """Выборка URL адресов из строк логов."""
        set_logs_uniq = set(self.lines)
        for set_log in set_logs_uniq:
            self.list_logs[set_log[6]] = set_log[-1]

    def get_count(self):
        """Получить сколько раз встречается URL в выборки лога."""
        return len(self.list_logs)

    def sum_line(self):
        """Посчитать кол-во строк в файле лога."""
        with open(self.log_file) as f:
            self.total_lines = sum(1 for _ in f)

    def get_total_lines(self) -> int:
        """Получить общее кол-во строк в файле лога."""
        self.sum_line()
        return self.total_lines

    def parse_log_file(self):
        """Прочитать файл и вернуть список времён."""
        with open(self.log_file) as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                time = parts[-1]
                self.times.append(float(time))
        self.times.sort()

    def metrics(self):
        self.read_log()
        self.parse_log_file()
        metrica = {
            "total_lines": self.get_total_lines(),  # Общее кол-во строк в файле лога
            "count": self.get_count(),  # Сколько раз встречается URL, абсолютное значение
            "mean": statistics.mean(self.times),
            "median": statistics.median(self.times),
            "perc_95": self.times[int(0.95 * self.get_count())],
            "min": self.times[0],
            "max": self.times[-1],
        }

        for k, v in metrica.items():
            console.print(f"{k}: {v}")
