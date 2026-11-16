# Rally

Django 6.1 app, managed with uv.

## Requirements

Python 3.13 (see `.python-version`) and [uv](https://docs.astral.sh/uv/).

## Run

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver     # http://localhost:8000
```

## Test

```bash
uv run pytest
```
