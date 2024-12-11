from Auxiliares.urls_servicios import UrlServicios
class NegocioUrls:
    #Clase para centralizar la lógica de obtención de URLs.
    
    @staticmethod
    def obtener_url_usuarios():
        return UrlServicios.get_users_url()

    @staticmethod
    def obtener_url_posts():
        return UrlServicios.get_posts_url()
