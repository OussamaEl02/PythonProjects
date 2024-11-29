import json

class Database:
    """
    Clase para gestionar operaciones en un archivo JSON que contiene todos los datos.

    Atributos:
        filename: Nombre del archivo JSON que se utiliza como base de datos.
    """

    def __init__(self, filename="db.json"):
        """
        Inicializa la base de datos con el nombre del archivo JSON.

        Args:
            filename (str): Nombre del archivo JSON .
        """
        self.filename = filename

    def load_data(self):
        """
        Carga los datos desde el archivo JSON.

        Si el archivo no existe, lo informa.

        Returns:
            dict: Datos cargados del archivo .
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("El fichero .json no existe")

    def save_data(self, data):
        """
        Guarda los datos proporcionados en el archivo JSON.

        Args:
            data (dict): Datos a almacenar en el archivo.
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
