from negocio.negocio_urls import NegocioUrls
from servicios.ws_jasonplaceholder import WsJsonPlaceholder
from modelos.usua import User
import sys
import os

# Agrega la ruta raíz del proyecto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from negocio.negocio_urls import NegocioUrls


def main():
    # Obtener la URL de usuarios desde el negocio
    url_usuarios = NegocioUrls.obtener_url_usuarios()

    # Obtener datos de la API
    print("Consultando usuarios...")
    datos_usuarios = WsJsonPlaceholder.obtener_datos(url_usuarios)

    if datos_usuarios:
        print("Usuarios obtenidos:")
        usuarios = [User(**usuario) for usuario in datos_usuarios]
        for usuario in usuarios[:3]:  # Mostrar los primeros 3 usuarios
            print(usuario)

if __name__ == "__main__":
    main()
