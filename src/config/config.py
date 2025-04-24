import os
from dotenv import load_dotenv

load_dotenv()

# Verificar que la URL de la base de datos se está cargando correctamente
database_url = os.getenv('DATABASE_URL')
print(f"Database URL: {database_url}")  # Este print te ayudará a verificar si la URL se carga correctamente

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_url  # Asegúrate de que esta variable esté configurada correctamente
