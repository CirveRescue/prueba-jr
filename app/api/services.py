import requests
from flask import current_app

# Definimos las excepciones personalizadas para manejar errores específicos de la API.
class ApiServiceError(Exception):
    # Excepción para manejar errores de servicio de la API.
    pass

class CategoryNotFoundError(Exception):
    # Excepción para manejar categorías no encontradas.
    pass


def obtener_categoria():
    # Esta función obtiene la lista de categorías disponibles desde la API de Chuck Norris.
    url = current_app.config["CHUCK_NORRIS_API_URL"] + "/categories"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ApiServiceError(f"Error de comunicación con la API externa: {e}")


def broma_por_categoria(category):
    # Verifica si la categoría es válida.
    categorias_disponibles = obtener_categoria()
    if category.lower() not in categorias_disponibles:
        raise CategoryNotFoundError(f"La categoría '{category}' no es válida.")

    # Construimos la URL para obtener un chiste de la categoría especificada.
    url = current_app.config["CHUCK_NORRIS_API_URL"] + "/random"
    try:
        response = requests.get(url, params={"category": category})
        response.raise_for_status()
        joke_data = response.json()
        
        # Retornamos un diccionario con los datos relevantes del chiste.
        return {
            "id": joke_data.get("id"),
            "url": joke_data.get("url"),
            "Categoria": category,
            "Broma": joke_data.get("value")
        }
    except requests.exceptions.RequestException as e:
        raise ApiServiceError(f"Error al obtener el chiste desde la API externa: {e}")