from auxiliares.urls_servicios import Url_Servicios
from servicios.ws_jsonplaceholder import Ws_jsonplaceholder
from modelos.usua import User

def obtener_usuarios():
    return f"{Url_Servicios.BASE_URL}/users"

    #@staticmethod
def obtener_usuario_por_id(user_id):
    return f"{UrlServicios.BASE_URL}/users/{user_id}"

    #@staticmethod
def crear_usuario():
    return f"{UrlServicios.BASE_URL}/users"

    #@staticmethod
def actualizar_usuario(user_id):
    return f"{UrlServicios.BASE_URL}/users/{user_id}"

    #@staticmethod
def eliminar_usuario(user_id):
    return f"{UrlServicios.BASE_URL}/users/{user_id}"

class NegocioUrls:
    def __init__(self, api_service):
        self.api_service = api_service

    def procesar_datos_usuarios(self):
        # Para obtener datos de la API
        datos_json = self.api_service.obtener_usuarios()
        
        # Transformar datos JSON en objetos User
        usuarios = []
        for usuario in datos_json:
            address = usuario['Address']
            geo = address['Geo']
            company = usuario['Company']
            usuarios.append(User(
                id=usuario['id'],
                name=usuario['name'],
                username=usuario['username'],
                email=usuario['email'],
                street=address['calle'],
                suite=address['suite'],
                city=address['city'],
                zipcode=address['zipcode'],
                lat=geo['lat'],
                lng=geo['lng'],
                company_name=company['name'],
                catch_phrase=company['catchPhrase'],
                bs=company['bs']
            ))
        return usuarios
