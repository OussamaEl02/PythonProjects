from FileController.FileManager import FileManager

""" 
    La clase Main es el punto de entrada principal del programa
    Se crea una instancia del gestor de archivos.
    Se llama al método 'ejecutar', que inicia el bucle principal del programa.
    Este bucle muestra el menú al usuario, espera una opción y ejecuta la acción correspondiente.
"""


if __name__ == "__main__":

    FileManager = FileManager()
    FileManager.ejecutar()

