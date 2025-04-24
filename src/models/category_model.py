from src.db import db
from src.models.base_model import BaseModelMixin

class Category(db.Model, BaseModelMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relación inversa con productos
    products = db.relationship('Product', back_populates='category')
