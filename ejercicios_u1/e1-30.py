
# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
# El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
# Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
# El pseudocódigo debes incluirlo como comentarios en el programa de Python.

# Pseudocódigo:

"""
Inicio
    Escribe "Dime un número: "
    Lee num
    Escribe "Dime un número de incremento: "
    Lee inc
    Escribe "Dime un número como total de la serie: "
    Lee serie

    Mientras (inc < 0) or (serie < 0) hacer
        Escribe "Error, debe introducir valores mayores a 0 tanto en incremento como en serie."
        Escribe "Dime otro número de incremento: "
        Lee inc
        Escribe "Dime otro número como total de la serie: "
        Lee serie

    Escribe "SERIE =>" + num + "-"
    cont = num
    Mientras (cont != (serie - 1) hacer
        Escribe num + "..."
        num += inc
    
    Escribe (num + inc) + "-"
    Escribe serie
Fin
"""

# Python

num = int(input(f"Dime un número:\n"))
inc = int(input(f"Dime un número de incremento:\n"))
serie = int(input(f"Dime un número como total de la serie:\n"))

while (inc < 0) or (serie < 0):
    print(f"Error, debe introducir valores mayores a 0 tanto en incremento como en serie.")
    inc = int(input(f"Dime otro número de incremento:\n"))
    serie = int(input(f"Dime otro número como total de la serie:\n"))

print(f"SERIE => {num}-")

cont = num
while (cont != (serie - 1)):
    print(f"{num}...")
    num += inc

print(f"{num + inc}-{serie}")

# Hola amiguis