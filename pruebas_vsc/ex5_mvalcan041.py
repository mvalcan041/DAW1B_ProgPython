"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 360 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 27 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.
"""

# Pseudocódigo:

"""
Inicio
    Escribe "Introduzca los días trabajados: "
    Lee dias_trabajados

    Mientras (dias_trabajados < 0) hacer
        Escribe "*** Error - el valor no puede ser negativo ***"
        Escribe "Introduzca los días trabajados: "
        Lee dias_trabajados

    años = dias_trabajados // 360
    restante_dias = dias_trabajados % 360
    meses = restante_dias // 30
    dias = restante_dias % 30
    
    Si (años != 1) entonces
        Si (meses != 1) entonces
            Si (dias != 1) entonces
                Escribir "Ha cotizado " + años + " años, " + meses + " meses y " + dias + " días."
            Sino
                Escribir "Ha cotizado " + años + " años, " + meses + " meses y " + dias + " día."
        Sino
            Si (dias != 1) entonces
                Escribir "Ha cotizado " + años + " años, " + meses + " mes y " + dias + " días."
            Sino
                Escribir "Ha cotizado " + años + " años, " + meses + " mes y " + dias + " día."
    Sino
        Si (meses != 1) entonces
            Si (dias != 1) entonces
                Escribir "Ha cotizado " + años + " año, " + meses + " meses y " + dias + " días."
            Sino
                Escribir "Ha cotizado " + años + " año, " + meses + " meses y " + dias + " día."
        Sino
            Si (dias != 1) entonces
                Escribir "Ha cotizado " + años + " año, " + meses + " mes y " + dias + " días."
            Sino
                Escribir "Ha cotizado " + años + " año, " + meses + " mes y " + dias + " día."
Fin
"""

# Python:

dias_trabajados = int(input("Introduzca los días trabajados:\n"))

while dias_trabajados < 0:
    print("*** Error - el valor no puede ser negativo ***")
    dias_trabajados = int(input("Introduzca los días trabajados:\n"))

años = dias_trabajados // 360
restante_dias = dias_trabajados % 360
meses = restante_dias // 30
dias = restante_dias % 30

if años != 1:
    if meses != 1:
        if dias != 1:
            print(f"Ha cotizado {años} años, {meses} meses y {dias} días.")
        else:
            print(f"Ha cotizado {años} años, {meses} meses y {dias} día.")
    else:
        if dias != 1:
            print(f"Ha cotizado {años} años, {meses} mes y {dias} días.")
        else:
            print(f"Ha cotizado {años} años, {meses} mes y {dias} día.")
else:
    if meses != 1:
        if dias != 1:
            print(f"Ha cotizado {años} año, {meses} meses y {dias} días.")
        else:
            print(f"Ha cotizado {años} año, {meses} meses y {dias} día.")
    else:
        if dias != 1:
            print(f"Ha cotizado {años} año, {meses} mes y {dias} días.")
        else:
            print(f"Ha cotizado {años} año, {meses} mes y {dias} día.")
