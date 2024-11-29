# Easy Compra

Esta es una aplicación simple de carrito de compras en Python que permite gestionar productos, realizar compras y generar facturas en formato PDF.

## Funcionalidades

- Visualizar productos disponibles.
- Agregar productos al carrito de compras.
- Ver los productos en el carrito.
- Generar facturas a partir del carrito de compras.
- Guardar facturas en formato PDF en una carpeta .

## Estructura de la Aplicación

La aplicación sigue el patrón de arquitectura **MVC** (Modelo-Vista-Controlador) y está compuesta por las siguientes clases:

- **Modelo:**
  - `Database`: Gestiona la carga y almacenamiento de datos en un archivo JSON.
  - `Product`: Maneja los productos, incluyendo la lista de productos y la reducción de stock.
  - `Cart`: Maneja las operaciones del carrito de compras.
  
- **Vista:**
  - `CartView`: Muestra las interfaces de texto para interactuar con el usuario.

- **Controlador:**
  - `CartController`: Controla la lógica de la aplicación, interactuando entre el modelo y la vista.

## Requisitos

Para ejecutar la aplicación, debes instalar las siguientes dependencias:

1. **reportlab**: Para generar facturas en formato PDF.
2. **json**: Para gestionar el archivo de datos en formato JSON.

Puedes usar el fichero requirements.txt :
`pip install -r requirements.txt`

