from flask import Blueprint, jsonify, request
from src.services.category_service import create_category, get_all_categories

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/', methods=['GET'])
def get_categories():
    categorias = get_all_categories()
    return jsonify([c.to_dict() for c in categorias])

@category_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Falta el nombre'}), 400

    categoria = create_category(data['name'])
    return jsonify(categoria.to_dict()), 201
