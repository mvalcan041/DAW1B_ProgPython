
# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
# El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
# Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
# El pseudocódigo debes incluirlo como comentarios en el programa de Python.

# Pseudocódigo:

"""
Inicio
    Escribe "Dime un número inicial: "
    Lee num
    Escribe "Dime un número incremental: "
    Lee inc
    Escribe "Dime el total de números en la serie: "
    Lee ser

    Mientras (inc <= 0) hacer
        Escribe "Error, el número incremental debe ser mayor que 0. Introduza un número de nuevo: "
        Lee inc

    Mientras (ser <= 0) hacer
        Escribe "Error, el total de números en la serie debe ser mayor que 0. Introduza un número de nuevo: "
        Lee ser
    
    cont = 0
    Escribe "Serie => " + ini + "-"

    Mientras (cont < (ser - 3)) hacer
        ini += inc
        Escribir ini + ".."
        cont += 1

    ini += inc
    Escribir ini + "-" + (ini + inc)
Fin
"""

# Python

ini = int(input(f"Dime un número inicial:\n"))
inc = int(input(f"Dime un número incremental:\n"))
ser = int(input(f"Dime el total de números en la serie:\n"))

while (inc <= 0):
    inc = int(input(f"Error, el número incremental debe ser mayor que 0. Introduza un número de nuevo:\n"))
    
while (ser <= 0):
    ser = int(input(f"Error, el total de números en la serie debe ser mayor que 0. Introduza un número de nuevo:\n"))

cont = 0
print(f"Serie => {ini}-", end= "")

while cont < (ser - 3):
    ini += inc
    print(f"{ini}..", end= "")
    cont += 1

ini += inc
print(f"{ini}-{ini + inc}")
