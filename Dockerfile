FROM python:3.11-slim

WORKDIR /app

# Copia los requirements e instala dependencias
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia toda la app
COPY ./app /app/app

# Comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
