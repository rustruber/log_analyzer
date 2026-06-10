# log_analyzer

![PyPI version](https://img.shields.io/pypi/v/log_analyzer.svg)

Cервис, формирующий статистический отчет на основании парсинга логов NGINX

* [GitHub](https://github.com/rustruber/log_analyzer/) | [PyPI](https://pypi.org/project/log_analyzer/) | [Documentation](https://rustruber.github.io/log_analyzer/)
* Created by [setter](https://lphp.ru) | GitHub [@rustruber](https://github.com/rustruber) | PyPI [@setter](https://pypi.org/user/setter/)
* MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://rustruber.github.io/log_analyzer/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

<<<<<<< HEAD
Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.
=======
Docs deploy automatically on push to `main` via GitHub Actions.
To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

>>>>>>> 100705c671bc257c3c9f6364170f756ed69bce84

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/log_analyzer.git
cd log_analyzer

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `log_analyzer`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

log_analyzer was created in 2026 by setter.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
