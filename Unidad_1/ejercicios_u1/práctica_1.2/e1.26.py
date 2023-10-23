
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

cesta_compra = input("Indique los productos de su cesta separados por una coma y un espacio (ej: agua, cerveza, etc.):\n")
lista_compra = cesta_compra.split(", ")

print("Lista de productos añadidos:")

for cesta_compra in lista_compra:
    print(cesta_compra)

# lista_compra = lista_compra.replace(" ",""").replace(",","\n")
# print(lista_compra)

# Aquí cambias la lista y como no sabemos si se respetará el formato establecido en el enunciado, hacemos replace de espacios en blanco y de comas, a saltos de línea.
