from flask import Flask
from src.controller.product_controller import product_bp
from src.db import db
from src.config.config import Config  # Import the Config class (corrección aquí)
from src.controller.category_controller import category_bp
from flask_cors import CORS
def create_app():
    app = Flask(__name__)

    # Cargar la configuración
    app.config.from_object(Config())  # Instantiate the Config class

    # Inicializar la base de datos con la configuración
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


    # Crear las tablas (esto debería hacerse solo una vez, como parte de la inicialización)
    with app.app_context():
        db.create_all()
        print("✅ Tablas creadas correctamente.")

    # Registrar el blueprint
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(category_bp, url_prefix='/categories')

    return app
