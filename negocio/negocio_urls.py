from auxiliares.urls_servicios import Urlservicios

class NegocioUrl:

    @staticmethod
    def obtener_url_usuarios():
        return Urlservicios.get_users_url()
    
    @staticmethod
    def obtener_url_posts():
        return Urlservicios.get_posts_url()