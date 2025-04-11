# Dockerfile
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar las dependencias e instalar
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "run.py"]
