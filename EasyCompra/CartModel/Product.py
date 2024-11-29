class Product:
    """
    Esta clase se encarga de gestionar los productos en nuestra base de datos.
    """

    def __init__(self, db):
        """
        Aquí estamos creando la clase `Product` y la estamos conectando con la base de datos.

        Args:
            db (Database): Objeto `Database` que nos permite acceder a los datos de los productos.
        """
        self.db = db

    def list_products(self):
        """
        Esta función nos devuelve todos los productos que están en la base de datos.

        Returns:
            list: Una lista con todos los productos disponibles.
        """
        data = self.db.load_data()
        return data.get("products", [])

    def reduce_stock(self, product_id, quantity):
        """
        Esta función reduce la cantidad de un producto en el inventario cuando se añade al carrito.

        Primero busca el producto por su ID, luego verifica si hay suficiente stock.
        Si está bien, reduce el stock.

        Args:
            product_id (int): ID del producto cuyo stock queremos reducir.
            quantity (int): La cantidad que queremos restar del stock.

        :Except:
            Exception: Si el producto no se encuentra o si no hay suficiente stock para la cantidad solicitada.
        """
        data = self.db.load_data()
        for product in data["products"]:
            if product["id"] == product_id:
                if product["stock"] > quantity:
                    product["stock"] -= quantity
                    self.db.save_data(data)
                    return
                if product["stock"] == quantity:
                    product["stock"] -= quantity
                    self.db.save_data(data)
                    return
                else:
                    raise Exception(f"Stock insuficiente para el producto '{product['name']}'.")
        raise Exception("Producto no encontrado.")
