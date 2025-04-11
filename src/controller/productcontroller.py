from flask import Blueprint, request, jsonify
from src.models.productmodel import Product
from src.db import db  # Asegúrate de importar db correctamente

product_bp = Blueprint('product_bp', __name__)

# Ruta para obtener todos los productos (GET)
@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()  # Obtiene todos los productos
    return jsonify([product.to_dict() for product in products])  # Devuelve todos los productos en formato JSON

# Ruta para crear un nuevo producto (POST)
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

    # Verifica si los campos necesarios están en la solicitud
    if not all(key in data for key in ('name', 'price', 'description', 'stock')):
        return jsonify({'message': 'Faltan datos en la solicitud'}), 400

    # Crear un nuevo producto con los datos recibidos
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        stock=data['stock']
    )

    try:
        # Agregar y confirmar el nuevo producto a la base de datos
        db.session.add(new_product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Revierte cualquier cambio si ocurre un error
        return jsonify({'message': 'Error al crear el producto', 'error': str(e)}), 500

    return jsonify({
        "message": "Producto creado exitosamente!",
        "product": new_product.to_dict()
    }), 201  # Devuelve el nuevo producto creado

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404

    data = request.get_json()
    for key in ['name', 'price', 'description', 'stock']:
        if key in data:
            setattr(product, key, data[key])

    try:
        db.session.commit()
        return jsonify({"message": "Producto actualizado", "product": product.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al actualizar', 'error': str(e)}), 500

# Ruta para eliminar un producto (DELETE)
@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Producto eliminado'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al eliminar', 'error': str(e)}), 500