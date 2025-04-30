FROM python:3.11-slim

WORKDIR /app

# Instala dependencias
COPY ./api-dti/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia la aplicación
COPY ./api-dti/app /app/app

# Expone y ejecuta el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]

