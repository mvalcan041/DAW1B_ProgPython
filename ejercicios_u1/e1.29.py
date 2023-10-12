
# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
# Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
# El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
# El pseudocódigo debes incluirlo como comentarios en el programa de Python.

# Pseudocódigo:

"""
Inicio
    Escribe "Dime un nombre: "
    Lee nombre
    Escribe "Dime una edad: "
    Lee edad

    Si (edad > 125) o (edad < 0) entonces
        Mientras (edad > 125) o (edad < 0) hacer
            Escribe "Dame una edad válida, comprendida entre 0 y 125 años: "
            Lee edad
        dif = 125 - edad
        Si (nombre == "") entonces
            nombre = "Desconocido"
            Escribe "Te llamas " + nombre + " y tienes " + edad + " años, te quedan aún " + dif + " años por cumplir."
        Sino
            Escribe "Te llamas " + nombre + " y tienes " + edad + " años, te quedan aún " + dif + " años por cumplir."
    Sino
        dif = 125 - edad
        Si (nombre == "") entonces
            nombre = "Desconocido"
            Escribe "Te llamas " + nombre + " y tienes " + edad + " años, te quedan aún " + dif + " años por cumplir."
    
        Sino
            Escribe "Te llamas " + nombre + " y tienes " + edad + " años, te quedan aún " + dif + " años por cumplir."
Fin
"""

# Python

nombre = input(f"Dame un nombre:\n")
edad = int(input(f"Dame una edad:\n"))

if (edad > 125) or (edad < 0):
    while (edad > 125) or (edad < 0):
        edad = int(input(f"Dame una edad válida, comprendida entre 0 y 125 años:\n"))
    dif = 125 - edad    
    if nombre == "":
        nombre = "Desconocido"
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {dif} años por cumplir.")

    else:
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {dif} años por cumplir.")

else:
    dif = 125 - edad
    if nombre == "":
        nombre = "Desconocido"
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {dif} años por cumplir.")

    else:
        print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {dif} años por cumplir.")
