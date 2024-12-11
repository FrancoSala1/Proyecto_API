from negocio.negocio_urls import NegocioUrls

def mostrar_menu():
    print("1. Obtener todos los usuarios")
    print("2. Obtener usuario por ID")
    print("3. Crear un usuario")
    print("4. Actualizar un usuario")
    print("5. Eliminar un usuario")
    print("6. Buscar en SERPER")
    print("0. Salir")

def main():
    negocio = NegocioUrls()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            print(negocio.obtener_usuarios())
        elif opcion == "2":
            user_id = input("Ingresa el ID del usuario: ")
            print(negocio.obtener_usuario_por_id(user_id))
        elif opcion == "3":
            data = {"name": "Nuevo Usuario", "email": "nuevo@correo.com"}
            print(negocio.crear_usuario(data))
        elif opcion == "4":
            user_id = input("Ingresa el ID del usuario: ")
            data = {"name": "Usuario Actualizado"}
            print(negocio.actualizar_usuario(user_id, data))
        elif opcion == "5":
            user_id = input("Ingresa el ID del usuario: ")
            print(negocio.eliminar_usuario(user_id))
        elif opcion == "6":
            query = input("Ingresa tu búsqueda: ")
            print(WSSerper.realizar_busqueda(query))
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
