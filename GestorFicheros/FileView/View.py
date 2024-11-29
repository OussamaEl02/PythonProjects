class View:
    """
    Clase para manejar la interacción con el usuario.
    """

    def mostrar_menu(self):
        """
        Muestra el menú principal al usuario.

        >>> vista = View()
        >>> vista.mostrar_menu()
        === ArchiGestor ===
        1. Crear un archivo
        2. Leer el contenido de un archivo
        3. Escribir en un archivo
        4. Eliminar un archivo
        5. Salir
        """
        print("\n=== ArchiGestor ===")
        print("1. Crear un archivo")
        print("2. Leer el contenido de un archivo")
        print("3. Escribir en un archivo")
        print("4. Eliminar un archivo")
        print("5. Salir")

    def pedir_input(self, mensaje: str) -> str:
        """
        Solicita una entrada del usuario.

        Args:
            mensaje (str): Mensaje que se mostrará al usuario.

        Returns:
            str: Entrada proporcionada por el usuario.

        >>> vista = View()
        >>> vista.pedir_input("Introduce el nombre del fichero: ")
        'Prueba'
        """
        return input(mensaje)

    def mostrar_mensaje(self, mensaje: str):
        """
        Muestra un mensaje al usuario.

        Args:
            mensaje (str): El mensaje que se mostrará.

        >>> vista = View()
        >>> vista.mostrar_mensaje("Operación realizada con éxito.")
        Operación realizada con éxito.
        """
        print(mensaje)
