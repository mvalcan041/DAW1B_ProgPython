
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = str(input("Indique el nombre del producto:\n"))
precio = float(input("Indique su precio:\n"))
cantidad = int(input("Indique la cantidad:\n"))

print(f"El producto se llama {producto}, su precio unitario es {precio:6.2f}, de una cantidad de {cantidad:3d} y un total de {(precio * cantidad):8.2f}.")
