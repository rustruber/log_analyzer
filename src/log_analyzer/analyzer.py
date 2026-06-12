"""Анализатор логов."""


class LogAnalyzer:
    def __init__(
        self,
        log_file: str,
    ):
        # путь к файлу логов
        self.log_file = log_file

        # общее кол-во строк в файле
        self.total_lines = 0

        # сколько раз встречается URL, абсолютное значение
        self.count = 0.0

        # суммарный $request_time для данного URL’а,
        # в процентах относительно общего $request_time всех
        # запросов (Часть / Целое * 100)
        self.count_perc = 0.0

        # средний $request_time для данного URL’а
        self.time_avg = 0.0

        # максимальный $request_time для данного URL’а
        self.time_max = 0.0

        # медиана $request_time для данного URL’а
        self.time_med = 0.0

    def sum_line(self, path_log: str) -> int:
        """Всего кол-во строк в файле лога."""
        with open(path_log) as f:
            return sum(1 for _ in f)
