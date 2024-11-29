import os

class File:
    """
    Modelo para gestionar archivos con operaciones básicas.
    """

    def __init__(self, nombre: str, ruta: str = "."):
        """
        Inicializa un objeto `File`.

        Args:
            nombre (str): El nombre del archivo (se agrega automáticamente la extensión `.txt` si no se proporciona).
            ruta (str): La ruta del directorio donde se encuentra el archivo (por defecto es el directorio actual).

        >>> archivo = File("prueba", "/documentos")
        >>> archivo.obtener_ruta_completa()
        '/documentos/prueba.txt'
        """
        self.nombre = nombre if nombre.endswith(".txt") else f"{nombre}.txt"
        self.ruta = ruta

    def obtener_ruta_completa(self) -> str:
        """
        Devuelve la ruta completa del archivo.

        Returns:
            str: Ruta completa del archivo.

        >>> archivo = File("mi_archivo")
        >>> archivo.obtener_ruta_completa()
        './mi_archivo.txt'
        """
        return os.path.join(self.ruta, self.nombre)

    def crear_archivo(self) -> str:
        """
        Crea un archivo vacío si no existe.

        Returns:
            str: Mensaje indicando si el archivo fue creado o si ya existía.

        >>> archivo = File("nuevo_archivo")
        >>> archivo.crear_archivo()
        'Archivo creado: ./nuevo_archivo.txt'
        """
        ruta_completa = self.obtener_ruta_completa()
        directorio = os.path.dirname(ruta_completa)

        if not os.path.exists(directorio):
            return f"El directorio no existe: {directorio}"

        if not os.path.exists(ruta_completa):
            with open(ruta_completa, "w") as archivo:
                pass
            return f"Archivo creado: {ruta_completa}"

        return f"El archivo ya existe: {ruta_completa}"

    def leer_archivo(self) -> str:
        """
        Lee el contenido del archivo.

        Returns:
            str: Contenido del archivo o un mensaje indicando que el archivo no existe.

        >>> archivo = File("prueba")
        >>> archivo.leer_archivo()
        'El archivo está vacío.'
        """
        ruta_completa = self.obtener_ruta_completa()
        if os.path.exists(ruta_completa):
            with open(ruta_completa, "r") as archivo:
                return archivo.read() or "El archivo está vacío."
        return "El archivo no existe."

    def escribir_archivo(self, contenido: str) -> str:
        """
        Añade contenido al archivo.

        Args:
            contenido (str): El texto que se añadirá al archivo.

        Returns:
            str: Mensaje indicando si se añadió contenido o si el archivo no existe.

        >>> archivo = File("prueba")
        >>> archivo.escribir_archivo("test")
        'Contenido añadido al archivo: ./prueba.txt'
        """
        ruta_completa = self.obtener_ruta_completa()
        if os.path.exists(ruta_completa):
            with open(ruta_completa, "a") as archivo:
                archivo.write(contenido + "\n")
            return f"Contenido añadido al archivo: {ruta_completa}"
        return "El archivo no existe."

    def eliminar_archivo(self) -> str:
        """
        Elimina el archivo.

        Returns:
            str: Mensaje indicando si el archivo fue eliminado o si no existía.

        >>> archivo = File("prueba")
        >>> archivo.eliminar_archivo()
        'Archivo eliminado: ./prueba.txt'
        """
        ruta_completa = self.obtener_ruta_completa()
        if os.path.exists(ruta_completa):
            os.remove(ruta_completa)
            return f"Archivo eliminado: {ruta_completa}"
        return "El archivo no existe."
