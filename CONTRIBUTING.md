
# Development

> **Note:** This project is currently maintained by a single developer (`@rustruber`).
> The guide below reflects the actual workflow. Forks and complex PR workflows are not required.

## Prerequisites

- Python 3.12–3.14
- [`uv`](https://docs.astral.sh/uv/) – fast package manager
- [`just`](https://github.com/casey/just) – command runner

## Setup

```bash
git clone git@github.com:rustruber/log_analyzer.git
cd log_analyzer
uv sync
```

## Quality checks (must pass before commit)

```bash
just qa
```

This runs:
- `ruff format` – code formatter
- `ruff check` – linter + auto‑fixes
- `ty check` – static type checker
- `pytest` – unit tests

## Running tests

| Command | Description |
|---------|-------------|
| `just test` | Run tests on Python 3.14 |
| `just testall` | Run tests on 3.12, 3.13, 3.14 |
| `just coverage` | Run tests + coverage report (HTML) |

## Documentation

```bash
just docs-serve   # local preview at http://localhost:8000
just docs-build   # static site in `site/`
```

> Due to Python 3.14 compatibility, docs commands currently use **Python 3.12** (enforced inside `justfile`).

## Package naming (important!)

| Purpose | Name |
|---------|------|
| PyPI package name (what you `pip install`) | `log-analyzer-cli` |
| CLI command (what you type in terminal) | `log_analyzer` (with underscore!) |

### Install
```bash
pip install log-analyzer-cli
```
### Using
```bash
log_analyzer --config /path/config.toml
```

## Making a release

1. Update version in `pyproject.toml`
2. Create and push a tag:
   ```bash
   git tag vX.Y.Z
   git push --tags
   ```
3. GitHub Actions will automatically:
    - Publish to **TestPyPI** (draft release)
    - Wait for approval → publish to **PyPI**

> Use pre‑release tags like `v0.2.0a1` for test versions.
> Regular `git push` (without a tag) never triggers a release.

## Cleanup

```bash
just clean   # removes build artifacts, cache, and coverage files
```

## License

MIT – see `LICENSE` file for details.


## Что изменилось и почему профи оценят

| Что было | Что стало | Почему |
|----------|-----------|--------|
| "Fork the repo", "Pull Request", "Open an issue" | Убрано или помечено как `> Note` | Честно: нет команды, нет форков, пулл-реквестов. |
| Размытое "Write documentation" | Конкретные команды `just docs-serve/build` + предупреждение про Python 3.14 | Профи ценят, когда документация не врёт. |
| Инструкция по релизу через `uv version` (которой нет) | Чётко: `pyproject.toml` → тег → CI | Отражает реальный процесс. |
| Упоминание Code of Conduct | Убрано (файл удалён) | Не храним мёртвые ссылки. |
| "Contributions welcome" в начале | Заменено на "currently maintained by a single developer" | Честно и не создаёт ложных ожиданий. |
| Скрытые нюансы (команда vs пакет) | Вынесено в отдельную секцию "Package naming (important!)" | Профи прочитают один раз и не ошибутся. |

