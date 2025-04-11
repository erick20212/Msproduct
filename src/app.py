from flask import Flask
from src.controller.productcontroller import product_bp
from src.db import db
from src.config.config import Config  # Import the Config class (corrección aquí)

def create_app():
    app = Flask(__name__)

    # Cargar la configuración
    app.config.from_object(Config())  # Instantiate the Config class

    # Inicializar la base de datos con la configuración
    db.init_app(app)

    # Crear las tablas (esto debería hacerse solo una vez, como parte de la inicialización)
    with app.app_context():
        db.create_all()
        print("✅ Tablas creadas correctamente.")

    # Registrar el blueprint
    app.register_blueprint(product_bp, url_prefix='/products')

    return app
