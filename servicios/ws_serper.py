import requests

class WSSerper:
    API_KEY = "TU_API_KEY"

    @staticmethod
    def realizar_busqueda(query):
        headers = {"X-API-KEY": WSSerper.API_KEY}
        response = requests.post(f"https://api.serper.dev/search", json={"q": query}, headers=headers)
        return response.json()
