from flask import Blueprint, jsonify, request

from .services import (
    obtener_categoria,
    broma_por_categoria,
    buscar_broma_por_termino,
    ApiServiceError,
    CategoryNotFoundError
)

# Creamos un Blueprint para las rutas de la API
api_bp = Blueprint('api', __name__)
# Definimos las rutas del API
@api_bp.route('/categories', methods=['GET'])
def categories_endpoint():
    try:
        # Obtenemos la lista de categorias
        categorias = obtener_categoria()
        return jsonify(categorias), 200
    except ApiServiceError as e:
        return jsonify({"error": str(e)}), 502

@api_bp.route('/joke/<string:category>', methods=['GET'])
def joke_endpoint(category):
    try:
        # Obtenemos un chiste para la categoria especificada
        broma = broma_por_categoria(category)
        return jsonify(broma), 200
    except CategoryNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ApiServiceError as e:
        return jsonify({"error": str(e)}), 502
    
@api_bp.route('/search', methods=['GET'])
def search_endpoint():
    # Obtenemos el parametro de busqueda de la consulta
    query = request.args.get('query')

    # Verificamos si el parametro 'query' esta presente
    if not query:
        return jsonify({
            "error": "Parametro 'query' faltante.",
            "message": "Debes proporcionar un termino de busqueda, ej: /search?query=python"
        }), 400 

    try:
        resultados = buscar_broma_por_termino(query)
        # Si no se encuentran chistes, devolvemos una lista vacia
        return jsonify(resultados), 200
    except ValueError as e:
        # Captura el error de busqueda invalida de nuestro servicio
        return jsonify({"error": str(e)}), 400 
    except ApiServiceError as e:
        # Captura errores de comunicacion con la API externa
        return jsonify({"error": str(e)}), 502
