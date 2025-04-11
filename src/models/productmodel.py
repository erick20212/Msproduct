# src/models/productmodel.py
from src.db import db  # Ahora importamos db desde db.py
from src.models.basemodel import BaseModelMixin  # Importar la mezcla del modelo base

class Product(db.Model, BaseModelMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock