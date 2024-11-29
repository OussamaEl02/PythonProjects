class CartView:
    """
    Esta clase representa las vistas del carrito de compras.
    """

    @staticmethod
    def show_menu():
        """
        Muestra el menú principal de la aplicación con las opciones disponibles.
        """
        print("\n------------Easy Compra-------------")
        print("Menú Principal:")
        print("1. Comprar un producto")
        print("2. Ver el carrito de compras")
        print("3. Generar factura")
        print("4. Salir")

    @staticmethod
    def show_products(products):
        """
        Muestra una lista de productos disponibles con sus detalles .

        Args:
            products (list): Lista de productos que se mostrarán al usuario.
        """
        print("\nProductos disponibles:")
        if not products:
            print("No hay productos disponibles.")
        else:
            for product in products:
                print(f"{product['id']}. {product['name']} - Precio: {product['price']} - Stock: {product['stock']}")

    @staticmethod
    def show_cart(cart):
        """
        Muestra el contenido actual del carrito de compras, incluyendo los productos y el total a pagar.

        Args:
            cart (list): Lista de productos en el carrito con sus cantidades.
        """
        print("\nCarrito de Compras:")
        if not cart:
            print("El carrito está vacío.")
        else:
            total = 0
            for item in cart:
                product_name = item['product']['name']
                quantity = item['quantity']
                total_price = item['product']['price'] * quantity
                print(f"- {product_name} (x{quantity}) | Precio: {total_price}")
                total += total_price
            print(f"Total a pagar: {total}")
