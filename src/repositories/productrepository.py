from src.db import db # Importar instancia FlaskSQLAlchemy para acceder a db.session
from src.models.productmodel import Product

class ProductRepository:

    def add(self, data):
        """Crea una nueva instancia de Product y la guarda en la DB."""
        new_product = Product(**data) # Desempaqueta el diccionario en el constructor
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def get(self, product_id):
        """Obtiene un producto por su ID."""
        # Product.query es un atajo de Flask-SQLAlchemy para db.session.query(Product)
        # .get() es eficiente para búsqueda por PK
        return Product.query.get(product_id)

    def get_all(self):
        """Obtiene todos los productos."""
        return Product.query.all()

    def update(self, product, data):
        """Actualiza una instancia de Product existente."""
        for key, value in data.items():
            # Actualiza solo los campos presentes en 'data'
            if hasattr(product, key):
                setattr(product, key, value)
        db.session.commit()
        return product

    def delete(self, product):
        """Elimina una instancia de Product de la DB."""
        db.session.delete(product)
        db.session.commit()