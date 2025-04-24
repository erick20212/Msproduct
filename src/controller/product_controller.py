from flask import Blueprint, request, jsonify
from src.models.product_model import Product
from src.services.product_service import get_all_products
from src.services.category_service import get_category_by_id
from src.db import db  # Asegúrate de importar db correctamente

product_bp = Blueprint('product_bp', __name__)

# 📦 GET /products
@product_bp.route('/', methods=['GET'])
def listar_productos():
    productos = get_all_products()
    return jsonify([p.to_dict() for p in productos])  # ✅ Solo category_id

# 🧾 POST /products
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()

    required_fields = ('name', 'price', 'description', 'stock', 'category_id')
    if not all(key in data for key in required_fields):
        return jsonify({'message': 'Faltan datos en la solicitud'}), 400

    # Validar categoría
    category = get_category_by_id(data['category_id'])
    if not category:
        return jsonify({'message': 'La categoría no existe'}), 400

    # Crear producto con la relación de categoría solo por ID
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        stock=data['stock'],
        image_url=data.get('image_url'),
        is_active=data.get('is_active', True),
        category_id=data['category_id']  # Solo asignamos el ID de la categoría, no el objeto completo
    )

    try:
        db.session.add(new_product)
        db.session.commit()

        # Verificación de los datos antes de responder
        print("🧪 VERIFICACIÓN FINAL:", new_product.to_dict())  # Esto debería devolver solo category_id

        return jsonify({
            "message": "Producto creado exitosamente!",
            "product": new_product.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al crear el producto', 'error': str(e)}), 500

# ✏️ PUT /products/<id>
@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404

    data = request.get_json()

    # Validar si se quiere cambiar la categoría
    if 'category_id' in data:
        categoria = get_category_by_id(data['category_id'])
        if not categoria:
            return jsonify({'message': 'La categoría no existe'}), 400
        product.category_id = data['category_id']  # Actualiza solo el ID de la categoría

    # Actualizar otros campos
    for key in ['name', 'price', 'description', 'stock', 'image_url', 'is_active']:
        if key in data:
            setattr(product, key, data[key])

    try:
        db.session.commit()
        return jsonify({
            "message": "Producto actualizado",
            "product": product.to_dict()  # Esto devolverá solo los campos básicos del producto
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al actualizar', 'error': str(e)}), 500
