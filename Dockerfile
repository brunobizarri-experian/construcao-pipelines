# Imagem base com Python 3.14
FROM python:3.14-slim

# Evita arquivos .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia apenas arquivos de dependência primeiro (melhor cache)
COPY pyproject.toml poetry.lock* /app/

# Configura Poetry para instalar dependências no sistema (sem virtualenv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o restante do projeto
COPY . /app/

# Expõe a porta do Flask
EXPOSE 5000

# Variáveis do Flask
ENV FLASK_APP=calculadora_web.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Comando para iniciar a aplicação
CMD ["flask", "run"]