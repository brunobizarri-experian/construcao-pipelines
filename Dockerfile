FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 5000

ENV FLASK_APP=calculadora_web.app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]