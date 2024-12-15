from negocio.negocio_urls import NegocioUrls
from servicios.ws_jsonplaceholder import WSJsonPlaceholder
from servicios.ws_serper import WSSerper

def main():
    # Instanciar servicios
    api_service = WSJsonPlaceholder()
    serper_service = WSSerper(api_key="TU_API_KEY")
    negocio = NegocioUrls(api_service)

    while True:
        print("\nMenú:")
        print("1. Obtener usuarios desde JSONPlaceholder")
        print("2. Buscar algo en Google con Serper")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuarios = negocio.procesar_datos_usuarios()
            for usuario in usuarios:
                print(vars(usuario))
        elif opcion == "2":
            consulta = input("¿Qué quieres buscar en Google? ")
            resultado = serper_service.buscar_en_google(consulta)
            print(resultado)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
