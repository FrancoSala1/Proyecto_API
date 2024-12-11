from auxiliares.urls_servicios import Url_Servicios
from servicios.ws_jasonplaceholder import WS_JsonPlaceholder

class NegocioUrls:
    def __init__(self):
        self.servicio = WS_JsonPlaceholder()

    def obtener_usuarios(self):
        return self.servicio.obtener_usuarios()

    def obtener_usuario_por_id(self, user_id):
        return self.servicio.obtener_usuario_por_id(user_id)

    def crear_usuario(self, data):
        return self.servicio.crear_usuario(data)

    def actualizar_usuario(self, user_id, data):
        return self.servicio.actualizar_usuario(user_id, data)

    def eliminar_usuario(self, user_id):
        return self.servicio.eliminar_usuario(user_id)

