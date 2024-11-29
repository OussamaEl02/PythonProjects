from datetime import datetime
from CartModel.Product import Product


class Cart:
    """
    Esta clase es como el 'asistente personal' del carrito de compras.
    Te ayuda a gestionar los productos en el carrito y las acciones que puedes hacer con ellos.

    Atributos:
        db (Database): La base de datos que se encarga de guardar toda la información de productos y carrito y facturas.
    """

    def __init__(self, db):
        """
        Aquí estamos creando el carrito, y le estamos dando acceso a la base de datos
        para que pueda gestionar todos los datos .

        Args:
            db (Database): El objeto que conecta el carrito con la base de datos.
        """
        self.db = db
        self.product_model = Product(db)

    def add_product(self, product_id, quantity):
        """
        Este metodo se encarga de agregar un producto al carrito si está bien con el producto y el stock.

        Primero, buscamos el producto, luego verificamos que haya suficiente stock y que la cantidad sea válida.
        Si está bien, agregamos el producto al carrito.

        Args:
            product_id (int): El ID único del producto que quieres agregar.
            quantity (int): La cantidad del producto que deseas agregar.

        :Except:
            Exception: Si el producto no existe o si no hay suficiente stock para la cantidad que pides.
        """
        data = self.db.load_data()

        product = next((p for p in data["products"] if p["id"] == product_id), None)
        if not product:
            raise Exception("No encontramos el producto.")

        if quantity <= 0:
            raise Exception("Cantidad inválida. ¿Seguro que quieres agregar cero o menos productos?")

        if product["stock"] < quantity:
            raise Exception(f"No hay suficiente stock para el producto '{product['name']}'.")

        self.product_model.reduce_stock(product_id, quantity)

        cart_details = data["cart"]["details"]
        existing_detail = next((d for d in cart_details if d["product_id"] == product_id), None)

        if existing_detail:
            existing_detail["quantity"] += quantity
        else:
            cart_details.append({
                "id": len(cart_details) + 1,
                "product_id": product_id,
                "quantity": quantity
            })

        data["cart"]["total"] += product["price"] * quantity
        self.db.save_data(data)

    def view_cart(self):
        """
        Muestra el contenido del carrito.

        Returns:
            list: Una lista con los productos y las cantidades que están en el carrito.
        """
        data = self.db.load_data()
        cart_details = data["cart"]["details"]
        products = data["products"]

        return [
            {
                "product": next(p for p in products if p["id"] == detail["product_id"]),
                "quantity": detail["quantity"]
            }
            for detail in cart_details
        ]

    def clear_cart(self):
        """
        Vacía el carrito y pone el total a cero, como si no has agregado nada.

        """
        data = self.db.load_data()
        data["cart"]["details"].clear()
        data["cart"]["total"] = 0
        self.db.save_data(data)

    def generate_invoice(self):
        """
        Este metodo genera una factura con los productos que tienes en el carrito.



        Returns:
            dict: Un diccionario con la factura que contiene id, fecha, total y los detalles de los productos.

        :Except:
            Exception: Si el carrito está vacío, no se puede generar la factura.
        """
        data = self.db.load_data()
        cart = data["cart"]

        if not cart["details"]:
            raise Exception("¡Oh no! El carrito está vacío. Agrega algo para generar la factura.")

        invoice = {
            "id": len(data["invoices"]) + 1,
            "date": datetime.now().isoformat(),
            "total": cart["total"],
            "details": cart["details"]
        }

        data["invoices"].append(invoice)
        self.db.save_data(data)

        return invoice

