FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los requirements e instala dependencias
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia la app completa
COPY ./app /app/app

# Comando de ejecución (Render expone el puerto automáticamente)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
