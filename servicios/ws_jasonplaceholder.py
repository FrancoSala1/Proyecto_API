import requests
from auxiliares.urls_servicios import UrlServicios

class WSJsonPlaceholder:
    def obtener_usuarios(self):
        response = requests.get(UrlServicios.obtener_usuarios())
        return response.json()

    def obtener_usuario_por_id(self, user_id):
        response = requests.get(UrlServicios.obtener_usuario_por_id(user_id))
        return response.json()

    def crear_usuario(self, data):
        response = requests.post(UrlServicios.crear_usuario(), json=data)
        return response.json()

    def actualizar_usuario(self, user_id, data):
        response = requests.put(UrlServicios.actualizar_usuario(user_id), json=data)
        return response.json()

    def eliminar_usuario(self, user_id):
        response = requests.delete(UrlServicios.eliminar_usuario(user_id))
        return response.status_code
