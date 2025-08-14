from flask import Blueprint, jsonify

from .services import obtener_categoria, broma_por_categoria, ApiServiceError, CategoryNotFoundError
# Creamos un Blueprint para las rutas de la API
api_bp = Blueprint('api', __name__)
# Definimos las rutas del API
@api_bp.route('/categories', methods=['GET'])
def categories_endpoint():
    try:
        # Obtenemos la lista de categorías
        categorias = obtener_categoria()
        return jsonify(categorias), 200
    except ApiServiceError as e:
        return jsonify({"error": str(e)}), 502

@api_bp.route('/joke/<string:category>', methods=['GET'])
def joke_endpoint(category):
    try:
        # Obtenemos un chiste para la categoría especificada
        broma = broma_por_categoria(category)
        return jsonify(broma), 200
    except CategoryNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ApiServiceError as e:
        return jsonify({"error": str(e)}), 502