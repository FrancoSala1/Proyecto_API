import requests

class WsJsonPlaceholder:

    @staticmethod
    def obtener_datos(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de {url}: {e}")
            return None