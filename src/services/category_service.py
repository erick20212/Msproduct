from src.repositories.category_repository import CategoryRepository

repo = CategoryRepository()

def create_category(name):
    return repo.add(name)

def get_all_categories():
    return repo.get_all()

def get_category_by_id(category_id):
    return repo.get_by_id(category_id)
