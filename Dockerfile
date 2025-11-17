FROM python:3.13-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# системные зависимости (если нужны)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# устанавливаем последнюю версию poetry
RUN python -m pip install --upgrade pip \
    && python -m pip install "poetry==2.1.4"

# копируем только метафайлы для кэширования слоя
COPY pyproject.toml poetry.lock /app/

# установить зависимости (без указания групп)
RUN poetry install --no-interaction --no-ansi --no-root

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]