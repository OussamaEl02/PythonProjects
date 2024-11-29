from CartModel.Database import Database
from CartView.CartView import CartView
from CartController.CartController import CartController

if __name__ == "__main__":
    """
    Clase principal para ejecutar la aplicación.
    Inicializa la base de datos, la vista y el controlador, y ejecuta el flujo principal con el metodo run().
    """
    db = Database("db.json")
    view = CartView()
    controller = CartController(db, view)
    controller.run()

