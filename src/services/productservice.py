from src.models.productmodel import Product
from src.db import db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product, data):
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()
