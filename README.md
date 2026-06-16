# log_analyzer

[![PyPI version](https://img.shields.io/pypi/v/log-analyzer-cli.svg)](https://pypi.org/project/log-analyzer-cli/)
[![Python versions](https://img.shields.io/pypi/pyversions/log-analyzer-cli.svg)](https://pypi.org/project/log-analyzer-cli/)
[![License](https://img.shields.io/github/license/rustruber/log_analyzer.svg)](https://github.com/rustruber/log_analyzer/blob/main/LICENSE)
[![CI](https://github.com/rustruber/log_analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/rustruber/log_analyzer/actions/workflows/ci.yml)
[![Publish to PyPI](https://github.com/rustruber/log_analyzer/actions/workflows/publish.yml/badge.svg)](https://github.com/rustruber/log_analyzer/actions/workflows/publish.yml)

Cервис для формирования статистических отчетов на основе парсинга логов NGINX.

* [GitHub](https://github.com/rustruber/log_analyzer/) | [PyPI](https://pypi.org/project/log-analyzer-cli/) | [Documentation](https://rustruber.github.io/log_analyzer/)
* Created by [setter](https://lphp.ru) | GitHub [@rustruber](https://github.com/rustruber) | PyPI [@setter](https://pypi.org/user/setter/)

## Функции

* Парсинг access-логов NGINX
* Расчет ключевых метрик
* Выявление «подозрительных» URL по времени ответа
* CLI-интерфейс на Typer
* Формирует отчёт в виде таблицы HTML в директории report с сортировкой столбцов
* (TODO) Экспорт в JSON / CSV
* (TODO) Фильтрация по временному диапазону

## Установка

```bash
pip install log-analyzer-cli
```

## Использование

### Опции
```bash
log_analyzer --help
```

### С конфигом по-умолчанию
```bash
log_analyzer
```

## Файл конфига, как пример (config.toml):
```bash
REPORT_SIZE = 10
REPORT_DIR = "./reports"
LOG_DIR = "./logs"
LOG_PATTERN = 'nginx_access_ui\.log_(\d{8})-\d{6}-[a-f0-9]+(?:\.gz)?$'
```

### С конфигом при запуске в консоли
```bash
log_analyzer --config /путь/к/файлу.toml
```

## Файл лога
Пример входных строк NGINX-лог файла
```bash
1.159.236.144 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/3118447/statistic/conversion/?date_from=2007-01-01&date_to=2017-06-29 HTTP/1.1" 200 328 "-" "Mozilla/5.0" "-" "1498782497-708638932-4707-10488660" "0ae935e4e7a96" 5.246
1.195.44.0 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/internal/revenue_share/service/276/partner/77624766/statistic/v2?date_from=2017-06-24&date_to=2017-06-30&date_type=day HTTP/1.0" 200 2615 "-" "-" "-" "1498782502-1775774396-4707-10488742" "0d9e6ca2ba" 0.329
1.138.198.128 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/25187824/statistic/?date_from=2016-10-20&date_to=2017-06-30 HTTP/1.1" 200 8237 "-" "python-requests/2.8.1" "-" "1498782503-440360380-4707-10488745" "4e9627334" 0.059
1.169.137.128 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/5960595 HTTP/1.1" 200 992 "-" "Configovod" "-" "1498782503-2118016444-4707-10488744" "712e90144abee9" 0.147
1.199.4.96 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/17572305/statistic/?date_from=2017-06-30&date_to=2017-06-30 HTTP/1.1" 200 115 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498782503-3800516057-4707-10488747" "c5d7e306f36c" 0.083
1.138.198.128 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/25187824 HTTP/1.1" 200 1260 "-" "python-requests/2.8.1" "-" "1498782503-440360380-4707-10488749" "4e9627334" 0.203
1.195.44.0 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/internal/revenue_share/service/276/partner/77757278/statistic/v2?date_from=2017-06-24&date_to=2017-06-30&date_type=day HTTP/1.0" 200 12 "-" "-" "-" "1498782503-1775774396-4707-10488750" "0d9e6ca2ba" 0.144
1.138.198.128 -  - [30/Jun/2017:03:28:23 +0300] "GET /api/v2/banner/25949683 HTTP/1.1" 200 1261 "-" "python-requests/2.8.1" "-" "1498782502-440360380-4707-10488740" "4e9627334" 0.863
```

## Таблицы отчёта
  * count - сколько раз встречается URL, абсолютное значение
  * count_perc - сколько раз встречается URL, в процентах относительно общего числа запросов
  * time_avg - средний $request_time для данного URL’а
  * time_max - максимальный $request_time для данного URL’
  * time_med - медианный $request_time для данного URL’
  * time_perc - суммарный $request_time для данного URL’а, в процентах относительно общего $request_time всех запросов
  * time_sum - суммарный $request_time для данного URL’а, абсолютное значение




## Документация
Документация собирается с помощью Zensical и автоматически публикуется на GitHub Pages.

- [Сайт документации](https://rustruber.github.io/log_analyzer/)

**Локальный предпросмотр:** just docs-serve (http://localhost:8000)

**Сборка**: just docs-build

API-документация генерируется автоматически из docstring-функций с помощью mkdocstrings.

Примечание для maintainer'а: Для автоматической публикации документации перейдите в Settings → Pages вашего репозитория и установите источник GitHub Actions.

## Разработка
Подготовка окружения

### Клонируйте репозиторий
```bash
git clone git@github.com:rustruber/log_analyzer.git
cd log_analyzer
```

### Синхронизируйте зависимости
```bash
uv sync
```

### Поднять виртуальное окружение
> Если работаете в PyCharm не забудьте переключить интерпретатор на нужную версию python в директории .venv/bin
```bash
source .venv/bin/activate
```

### Установка в режиме разработки (editable)
После этого команда log_analyzer станет доступна глобально, а любые изменения в коде будут подхватываться сразу.
```bash
uv pip install -e .
```

### Проверка качества кода
Эта команда запускает форматирование (ruff format), линтинг (ruff check), проверку типов (ty) и тесты (pytest).
```bash
just qa
```

## Команды для разработки

| Команда | Что делает |
|---------|------------|
| `just qa` | Полная проверка (форматирование, линтинг, типы, тесты) |
| `just test` | Запустить тесты |
| `just docs-serve` | Посмотреть документацию локально |
| `just build` | Собрать пакет |
|`just type-check`|	Проверить типы|

### Запуск тестов
``` bash
uv run pytest
```

### Лицензия
**MIT License**

_Проект создан в 2026 году._

