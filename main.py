import requests
from dotenv import load_dotenv
import os

def CargarConfiguracion():
    load_dotenv()
    api_key = os.getenv("API_KEY_SEARCH_GOOGLE")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    if not api_key or not search_engine_id:
        print("Error: Las variables de entorno no están configuradas correctamente.")
        exit()
    return api_key, search_engine_id
def ConstruirUrl(api_key, search_engine_id, query, page, lang):
    return f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"
def RealizarBusqueda(url):
    """Realiza la solicitud a la API y devuelve los resultados."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def procesar_resultados(resultados):
    if not resultados:
        print("No se encontraron resultados.")
        return

    for item in resultados:
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)

def main():
    api_key, search_engine_id = CargarConfiguracion()

    query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
    page = 1
    lang = "lang_es"

    url = ConstruirUrl(api_key, search_engine_id, query, page, lang)

    data = RealizarBusqueda(url)
    if data:
        resultados = data.get('items', [])
        procesar_resultados(resultados)

if __name__ == "__main__":
    main()