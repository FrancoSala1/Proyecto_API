import requests

class WSSerper:
    def __init__(self, api_key):
        self.api_key = api_key

    def buscar_en_google(self, consulta):
        url = "https://serpapi.com/search"
        params = {
            "q": consulta,
            "hl": "en",
            "gl": "us",
            "api_key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "No se pudo realizar la búsqueda"}
