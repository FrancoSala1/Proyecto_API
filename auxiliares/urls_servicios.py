class UrlServicios:
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    SERPER_URL = "https://api.serper.dev"

    @staticmethod
    def obtener_usuarios():
        return f"{UrlServicios.BASE_URL}/users"

    @staticmethod
    def obtener_usuario_por_id(user_id):
        return f"{UrlServicios.BASE_URL}/users/{user_id}"

    @staticmethod
    def crear_usuario():
        return f"{UrlServicios.BASE_URL}/users"

    @staticmethod
    def actualizar_usuario(user_id):
        return f"{UrlServicios.BASE_URL}/users/{user_id}"

    @staticmethod
    def eliminar_usuario(user_id):
        return f"{UrlServicios.BASE_URL}/users/{user_id}"
