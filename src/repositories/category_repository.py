from src.db import db
from src.models.category_model import Category

class CategoryRepository:

    def add(self, name):
        categoria = Category(name=name)
        db.session.add(categoria)
        db.session.commit()
        return categoria

    def get_all(self):
        return Category.query.all()

    def get_by_id(self, category_id):
        return Category.query.get(category_id)
