class Urlservicios:
# esta clase es para centralizar y manejar las URLS de servicios web.
    BASE_URL = "http://jasonplaceholder.typicode.com"

    @staticmethod
    def get_users_url():
        return f"{Urlservicios.BASE_URL}/users"
    
    @staticmethod
    def get_posts_url():
        return f"{Urlservicios.BASE_URL}/posts"