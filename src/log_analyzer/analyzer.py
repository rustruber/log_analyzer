"""Анализатор логов."""

import json
import logging
import re
import statistics
from datetime import datetime as dt
from itertools import islice
from pathlib import Path
from typing import Any

from rich.console import Console

console = Console()


logger = logging.getLogger(__name__)


class LogAnalyzer:
    def __init__(
        self,
        config: dict[str, Any],
    ):
        self.config = config

        # скомпилированный в объект шаблон имени файла.
        self._log_pattern = re.compile(config["LOG_PATTERN"])

        # Дата последнего лога
        self._log_date: dt | None = None

        # Путь к файлу логов.
        self._log_file: Path | None = None

        self._log_dir = Path(self.config["LOG_DIR"])

        self._log_pattern = re.compile(self.config["LOG_PATTERN"])

        # Все строки из лога в список
        self._lines: list[str] = []

        # Выборка URL адресов из лога
        self._list_logs = {}

        # Общее кол-во запросов в файле.
        self._total_lines = 0

        # Список времён.
        self._times: list[float] = []

        # Кол-во выбираемых элементов для показа.
        self._selected_items = self.config["REPORT_SIZE"]

        # Сортировка вывода списка False - по возрастание, True - по убывание
        self._sorting = True

    def _find_latest_date(self) -> dt | None:
        """Найти последнюю дату."""
        latest_date = None
        for file in self._log_dir.iterdir():
            match = self._log_pattern.match(file.name)
            if match:
                date_str = match.group(1)
                file_date = dt.strptime(date_str, "%Y%m%d")
                if latest_date is None or file_date > latest_date:
                    latest_date = file_date
        return latest_date

    def _find_latest_log(self):
        """Найти последний лог-файл. Инициализировать атрибуты."""
        latest_file: Path | None = None
        latest_date: dt | None = None

        for file in self._log_dir.iterdir():
            match = self._log_pattern.match(file.name)
            if not match:
                continue

            # Извлекаем дату из первой группы
            date_str = match.group(1)  # "20170630"
            try:
                file_date = dt.strptime(date_str, "%Y%m%d")
            except ValueError:
                continue

            # Сравниваем
            if latest_date is None or file_date > latest_date:
                latest_date = file_date
                latest_file = file

        self._log_file = latest_file
        self._log_date = latest_date

    def _read_log(self):
        """Собрать все строки из лога в список (по умолчанию)."""
        if self._log_file is None:
            self._find_latest_log()
        if self._log_file is None:
            raise FileNotFoundError("Лог-файл не найден")
        with open(self._log_file) as f:
            self._lines = [line.rstrip("\n") for line in f]

    def _check_url(self):
        """Выборка URL и времён из строк логов."""
        set_logs_uniq = self._lines
        for set_log in set_logs_uniq:
            parts = set_log.split()
            url = parts[6]
            try:
                req_time = float(parts[-1])
            except (ValueError, IndexError):
                continue

            if url in self._list_logs:
                self._list_logs[url]["times"].append(req_time)
                self._list_logs[url]["count"] += 1
            else:
                self._list_logs[url] = {"count": 1, "times": [req_time]}

        # Сортировка по суммарному времени (sum(times))
        self._list_logs = dict(
            sorted(self._list_logs.items(), key=lambda item: sum(item[1]["times"]), reverse=self._sorting)
        )

        # Обрезка
        self._list_logs = dict(islice(self._list_logs.items(), self._selected_items))

    def _get_count(self):
        """Получить сколько раз встречается URL в выборки лога."""
        return len(self._list_logs)

    def _sum_line(self):
        """Посчитать кол-во запросов в файле лога."""
        self._total_lines = len(self._lines)

    def _get_total_lines(self) -> int:
        """Получить общее кол-во строк в файле лога."""
        self._sum_line()
        return self._total_lines

    def _parse_log_file(self):
        """Вернуть список времён."""
        for line in self._lines:
            parts = line.split()
            try:
                time = float(parts[-1])
            except (ValueError, IndexError):
                continue  # пропускаем битые строки
            self._times.append(time)

    def _total_time(self) -> float:
        return sum(self._times)

    def save_report(self, report_data: list):
        """Сохраняет HTML-отчёт."""
        # Папка для отчётов
        report_dir = Path(self.config["REPORT_DIR"])
        report_dir.mkdir(parents=True, exist_ok=True)

        if self._log_date is None:
            raise ValueError("Дата лога не установлена")

        # Имя файла: report-2025.12.31.html
        report_name = f"report-{self._log_date.strftime('%Y.%m.%d')}.html"
        report_path = report_dir / report_name

        # Шаблон (лежит в корне проекта)
        template_path = Path(self.config["TEMPLATE_PATH"])
        if not template_path.exists():
            raise FileNotFoundError("Шаблон report.html не найден")

        # Читаем шаблон
        with open(template_path, encoding="utf-8") as f:
            template = f.read()

        # Заменяем $table_json на данные
        html = template.replace("$table_json", json.dumps(report_data, indent=2))

        # Сохраняем
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(html)

        logger.info(f"Отчёт сохранён: {report_path}")

    def metrics(self):
        """
        Про отчет:
            • count - сколько раз встречается URL, абсолютное
            значение
            • count_perc - (количество_запросов_к_URL / общее_число_всех_запросов) * 100
            сколько раз встречается URL, в процентах
            относительно общего числа запросов
            • time_avg - средний $request_time для данного URL’а
            • time_max - максимальный $request_time для данного URL’
            • time_med - медианный $request_time для данного URL’
            • time_perc - (время_на_URL / общее_время_всех_запросов) * 100
            суммарный $request_time для данного URL’а, в процентах относительно общего
            $request_time всех запросов
            • time_sum - суммарный $request_time для данного URL’а,
            абсолютное значение
        """
        self._find_latest_log()  # установили значение последнего (актуального) лог-файла
        self._read_log()  # собрали все строки из лог-файла
        self._check_url()  # выбрали все URL из строк
        self._parse_log_file()

        # Собираем данные для отчёта
        report_data = []

        for url, info in self._list_logs.items():
            time_sum = sum(info["times"])
            report_data.append(
                {
                    "url": url,
                    "count": info["count"],
                    "count_perc": (info["count"] / self._get_total_lines()) * 100,
                    "time_avg": time_sum / info["count"],
                    "time_max": max(info["times"]),
                    "time_med": statistics.median(info["times"]),
                    "time_perc": (time_sum / self._total_time()) * 100,
                    "time_sum": time_sum,
                }
            )

        # Сохраняем HTML-отчёт
        self.save_report(report_data)

        metrica = {
            "log_file": self._log_file,  # Путь к файлу логов
            "log_date": self._log_date,  # Дата последнего лога
            "total_lines": self._get_total_lines(),  # Общее кол-во запросов в файле лога
            "selected_items": self._selected_items,  # Кол-во выбираемых элементов
            "sorting": self._sorting,  # Сортировка вывода списка 0 - по возрастание, 1 - по убывание
            "count": self._get_count(),  # Сколько раз встречается URL, абсолютное значение
            "mean": statistics.mean(self._times),  # Среднее время ответа сервера в секундах.
            # median - показывает, что большинство запросов (50%) укладываются в
            # statistics.median(self._times) мс.
            "median": statistics.median(self._times),
            # 95% запросов быстрее perc_95 мс.
            "perc_95": self._times[int(0.95 * self._get_count())],
            "min": min(self._times),
            "max": max(self._times),
        }

        for k, v in metrica.items():
            console.print(f"{k}: {v}")

        console.print("\n---------\n")

        for k, v in islice(self._list_logs.items(), self._selected_items):
            time_sum = sum(v["times"])
            time_avg = time_sum / v["count"]
            time_max = max(v["times"])
            time_med = statistics.median(v["times"])
            cp = (v["count"] / self._get_total_lines()) * 100
            tp = (sum(v["times"]) / self._total_time()) * 100
            console.print(
                f"{k}| count: {v['count']} | count_perc: {cp:.3f} | time_avg: {time_avg:.3f} | "
                f"time_max: {time_max:.3f} | time_med: {time_med:.3f} | time_perc: {tp:.3f} | "
                f"time_sum: {time_sum:.3f}"
            )
