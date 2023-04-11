FROM python:3.9-slim-buster

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos necesarios para instalar dependencias
COPY ./app /app
COPY ./app/requirements.txt /app/requirements.txt

# Instalar dependencias
RUN apt-get update && apt-get install -y libssl-dev \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir certifi \
    && pip install uvicorn \
    && apt-get remove -y libssl-dev \
    && apt-get autoremove -y
# Copiar todos los archivos del repositorio dentro del contenedor
COPY . .

# Exponer el puerto que usa tu aplicación
EXPOSE 8000

# Establecer variables de entorno necesarias
ENV CON_STRING_CLOUD='mongodb+srv://ChrisAqM:9yBkG1RQTxKRZZ45@cluster0.jp8ivfz.mongodb.net/?retryWrites=true&w=majority'
ENV CON_CLIENT='IDS347'
ENV LOG_FILE='log.txt'

# Ejecutar comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]