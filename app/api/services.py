import requests
from flask import current_app

# Definimos las excepciones personalizadas para manejar errores especificos de la API.
class ApiServiceError(Exception):
    # Excepcion para manejar errores de servicio de la API.
    pass

class CategoryNotFoundError(Exception):
    # Excepcion para manejar categorias no encontradas.
    pass


def obtener_categoria():
    # Esta funcion obtiene la lista de categorias disponibles desde la API de Chuck Norris.
    url = current_app.config["CHUCK_NORRIS_API_URL"] + "/categories"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ApiServiceError(f"Error de comunicacion con la API externa: {e}")


def broma_por_categoria(category):
    # Verifica si la categoria es valida.
    categorias_disponibles = obtener_categoria()
    if category.lower() not in categorias_disponibles:
        raise CategoryNotFoundError(f"La categoria '{category}' no es valida.")

    # Construimos la URL para obtener un chiste de la categoria especificada.
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

def buscar_broma_por_termino(query):
    url = current_app.config["CHUCK_NORRIS_API_URL"] + "/search"
    params = {"query": query}

    try:
        response = requests.get(url, params=params)
        
        # La API de Chuck Norris devuelve un error 422 si la busqueda es invalida o el termino es demasiado corto.
        # Lo capturamos para dar un mensaje de error mas claro.
        if response.status_code == 422:
            raise ValueError("El termino de busqueda es invalido o demasiado corto.")

        # Lanza una excepcion para otros errores HTTP
        response.raise_for_status()
        
        search_results = response.json()
        jokes_encontrados = search_results.get("result", [])

        # Transformamos cada chiste al formato consistente de nuestra API
        chistes_formateados = []
        for joke in jokes_encontrados:
            chistes_formateados.append({
                "id": joke.get("id"),
                "url": joke.get("url"),
                # La busqueda puede devolver chistes de varias categorias, asi que usamos una lista
                "categorias": joke.get("categories", []),
                "broma": joke.get("value")
            })
        
        return chistes_formateados

    except requests.exceptions.RequestException as e:
        raise ApiServiceError(f"Error al buscar en la API externa: {e}")