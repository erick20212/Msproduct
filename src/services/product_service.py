from src.models.product_model import Product
from src.db import db
from src.services.category_service import get_category_by_id  # ✅ Asegúrate de tenerlo

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    category_id = data.get('category_id')

    if category_id:
        categoria = get_category_by_id(category_id)
        if not categoria:
            raise Exception("La categoría no existe")

