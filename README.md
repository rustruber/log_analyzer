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
* Расчет ключевых метрик: количество запросов, среднее время, медиана, 95-й персентиль
* Выявление «подозрительных» URL по времени ответа
* CLI-интерфейс на Typer
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

### с конфигом по-умолчанию
```bash
log_analyzer
```

## Файл конфига, как пример (config.toml):
```bash
REPORT_SIZE = 10
REPORT_DIR = "./reports"
TEMPLATE_PATH = "./templates/report.html"
LOG_DIR = "./logs"
LOG_PATTERN = 'nginx_access_ui\.log_(\d{8})-\d{6}-[a-f0-9]+(?:\.gz)?$'
```

### с конфигом при запуске в консоли
```bash
log_analyzer --config /путь/к/файлу.toml
```


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

## Test: Branch protection is working!
