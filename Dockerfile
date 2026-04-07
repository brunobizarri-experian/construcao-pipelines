FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml ./
RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "calculadora_web.app", "run", "--host=0.0.0.0"]