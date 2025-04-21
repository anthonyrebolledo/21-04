
import requests

from dotenv import load_dotenv

import os



load_dotenv()

API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")

SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")



# configuracion de la consulta y los parametros de busqueda

query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'

page = 1

lang = "lang_es"

# Construcción de la URL para la API de Google Custom Search

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"

# Realizar la solicitud a la API

response = requests.get(url)

data = response.json()



result= data.get('items', [])

if not result:

    print("No se encontraron resultados.")

else:

    for item in result:

        title = item.get('title')

        link = item.get('link')

        snippet = item.get('snippet')

        print(f"Title: {title}")

        print(f"Link: {link}")

        print(f"Snippet: {snippet}")

        print("-" * 80)

        



