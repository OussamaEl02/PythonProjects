from CartModel.Cart import Cart
from CartModel.Product import Product
from reportlab.pdfgen import canvas
import os

class CartController:
    """
    Esta clase Gestiona las acciones del usuario en la tienda..

    """

    def __init__(self, db, view):
        """
        Inicializa el controlador con la base de datos y la vista.

        Params:
            db: Objeto `Database` para manejar los datos.
            view: Objeto de la vista que muestra la interfaz al usuario.
        """
        self.db = db
        self.view = view
        self.ProductModel = Product(db)
        self.CartModel = Cart(db)

    def run(self):
        """
        Ejecuta el bucle principal de la aplicación, permitiendo al usuario interactuar con el menú.
        """
        while True:
            self.view.show_menu()
            option = input("Selecciona una opción: ")

            if option == "1":
                self.buy_product()
            elif option == "2":
                self.view_cart()
            elif option == "3":
                self.generate_invoice()
            elif option == "4":
                print("Saliendo de la tienda de Oussama. ¡Gracias por tu compra!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

    def buy_product(self):
        """
        Permite al usuario comprar un producto seleccionándolo de la lista y especificando la cantidad.
        """
        products = self.ProductModel.list_products()
        self.view.show_products(products)

        while True:
            try:
                product_id = int(input("\nSelecciona el ID del producto: "))
                quantity = int(input("Ingresa la cantidad: "))
                self.ProductModel.reduce_stock(product_id, quantity)
                self.CartModel.add_product(product_id, quantity)
                print("Producto agregado al carrito.")
                break
            except ValueError:
                print("Error: Por favor, ingresa un número válido para el ID o la cantidad.")
            except Exception as e:
                print(f"Error: {e}")

    def view_cart(self):
        """
        Muestra los productos en el carrito de compras.
        """
        cart = self.CartModel.view_cart()
        self.view.show_cart(cart)

    def generate_invoice(self):
        """
        Genera una factura para los productos en el carrito y ofrece la opción de limpiar el carrito.
        """
        try:
            invoice = self.CartModel.generate_invoice()
            print("\nFactura generada:")
            print(f"ID: {invoice['id']}")
            print(f"Fecha: {invoice['date']}")
            print(f"Total: {invoice['total']}")
            print("Detalles:")
            for detail in invoice["details"]:
                print(f"- Producto ID {detail['product_id']} | Cantidad: {detail['quantity']}")

            self.generate_invoice_pdf(invoice)
            self.delete_cart()

        except Exception as e:
            print(f"Error: {e}")

    def generate_invoice_pdf(self, invoice):
        """
        Genera una factura en PDF y la guarda en 'invoices'.
        """
        os.makedirs('Invoices', exist_ok=True)
        filename = f'Invoices/factura_{invoice["id"]}.pdf'

        c = canvas.Canvas(filename)
        c.setFont("Helvetica", 10)

        c.drawString(72, 800, f"Factura No: {invoice['id']}")
        c.drawString(72, 785, f"Fecha: {invoice['date']}")
        c.drawString(72, 770, f"Total: {invoice['total']}")

        c.setFont("Helvetica", 8)
        text_object = c.beginText(72, 750)

        for item in invoice['details']:
            text_object.textLine(f"Producto ID: {item['product_id']} | Cantidad: {item['quantity']}")

        c.drawText(text_object)
        c.save()

        print(f"Factura guardada como {filename}")

    def delete_cart(self):
        """
        Pide confirmación al usuario antes de limpiar el carrito de compras.
        """
        confirmation = input("¿Estás seguro de que deseas vaciar el carrito? (S/N): ").strip().upper()

        if confirmation == "S":
            data = self.db.load_data()
            data["cart"]["details"] = []
            data["cart"]["total"] = 0
            self.db.save_data(data)
            print("El carrito ha sido limpiado.")
        else:
            print("El carrito no se ha vaciado.")

