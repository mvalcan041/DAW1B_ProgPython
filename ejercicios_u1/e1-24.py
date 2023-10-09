
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = float(input("Indique el precio del producto:\n"))

euros = int(precio)
centimos = precio - euros

print(f"Euros = {euros}€\nCéntimos = {centimos:.2f}€")

# precio = input("Indique el precio del producto:\n")
# Hacer un split(.) al input de tipo str y sacar por un lado los euros [0] y los céntimos [1].
