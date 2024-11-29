from FileModel.File import File
from FileView.View import View

class FileManager:
    """
    Controlador para gestionar las operaciones con archivos.
    """

    def __init__(self):
        """
        Inicializa el gestor de archivos con una vista para la interacción con el usuario.

        >>> gestor = FileManager()
        >>> type(gestor.view)
        <class 'FileView.View'>
        """
        self.view = View()

    def procesar_opcion(self, opcion: int):
        """
        Procesa la opción seleccionada por el usuario.

        Args:
            opcion (int): Opción seleccionada.

        >>> gestor = FileManager()
        >>> gestor.procesar_opcion(1)
        """
        if opcion == 1:
            self.crear_archivo()
        elif opcion == 2:
            self.leer_archivo()
        elif opcion == 3:
            self.escribir_archivo()
        elif opcion == 4:
            self.eliminar_archivo()
        elif opcion == 5:
            self.salir()
        else:
            self.view.mostrar_mensaje("Opción inválida.")

    def crear_archivo(self):
        """
        Solicita datos y crea un archivo.

        >>> gestor = FileManager()
        >>> gestor.crear_archivo()
        Introduce el nombre del archivo: prueba.txt
        Introduce la ruta (o deja vacío para usar el directorio actual): ruta
        File created: ruta/prueba.txt
        """
        nombre = self.view.pedir_input("Introduce el nombre del archivo: ")
        ruta = self.view.pedir_input("Introduce la ruta (o deja vacío para usar el directorio actual): ") or "."
        archivo = File(nombre, ruta)
        self.view.mostrar_mensaje(archivo.crear_archivo())

    def leer_archivo(self):
        """
        Lee el contenido de un archivo.

        >>> gestor = FileManager()
        >>> gestor.leer_archivo()
        Introduce el nombre del archivo: prueba.txt
        Introduce la ruta (o deja vacío para usar el directorio actual): ruta
        File content: "Este es un archivo de prueba."
        """
        nombre = self.view.pedir_input("Introduce el nombre del archivo: ")
        ruta = self.view.pedir_input("Introduce la ruta (o deja vacío para usar el directorio actual): ") or "."
        archivo = File(nombre, ruta)
        self.view.mostrar_mensaje(f"Contenido del archivo:\n{archivo.leer_archivo()}")

    def escribir_archivo(self):
        """
        Añade contenido a un archivo.

        >>> gestor = FileManager()
        >>> gestor.escribir_archivo()
        Introduce el nombre del archivo: prueba.txt
        Introduce la ruta (o deja vacío para usar el directorio actual): ruta
        Introduce el contenido a escribir: Esto es una prueba.
        Content added to the file: ruta/prueba.txt
        """
        nombre = self.view.pedir_input("Introduce el nombre del archivo: ")
        ruta = self.view.pedir_input("Introduce la ruta (o deja vacío para usar el directorio actual): ") or "."
        contenido = self.view.pedir_input("Introduce el contenido a escribir: ")
        archivo = File(nombre, ruta)
        self.view.mostrar_mensaje(archivo.escribir_archivo(contenido))

    def eliminar_archivo(self):
        """
        Elimina un archivo.

        >>> gestor = FileManager()
        >>> gestor.eliminar_archivo()
        Introduce el nombre del archivo: prueba.txt
        Introduce la ruta (o deja vacío para usar el directorio actual): ruta
        File deleted: ruta/prueba.txt
        """
        nombre = self.view.pedir_input("Introduce el nombre del archivo: ")
        ruta = self.view.pedir_input("Introduce la ruta (o deja vacío para usar el directorio actual): ") or "."
        archivo = File(nombre, ruta)
        self.view.mostrar_mensaje(archivo.eliminar_archivo())

    def salir(self):
        """
        Sale del programa.

        >>> gestor = FileManager()
        >>> gestor.salir()
        Salida: Saliendo del programa...
        """
        self.view.mostrar_mensaje("Saliendo del programa...")
        exit()

    def ejecutar(self):
        """
        Inicia el bucle principal para gestionar las operaciones.

        >>> gestor = FileManager()
        >>> gestor.ejecutar()
        Muestra el menú de opciones y procesa las opciones del usuario.
        """
        while True:
            self.view.mostrar_menu()
            try:
                opcion = int(self.view.pedir_input("Selecciona una opción: "))
                self.procesar_opcion(opcion)
            except ValueError:
                self.view.mostrar_mensaje("Por favor, introduce un número válido.")
