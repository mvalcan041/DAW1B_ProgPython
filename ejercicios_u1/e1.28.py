
# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
# El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
# Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
# El pseudocódigo debes incluirlo como comentarios en el programa de Python.

# Pseudocódigo:

"""
Inicio
    Escribe "Dame un número entero: "
    Lee num1
    Escribe "Dame otro número entero: "
    Lee num2
    
    Si (num1 == num2) entonces
        Escribe "Los números no pueden ser iguales."
    
    Sino
        Si (num1 < num2) entonces
            dif = num2 - num1
            Escribe "El número menor es " + num1 + " y entre ellos existen " + dif + " números enteros."
        Sino
            dif = num1 - num2
            Escribe "El número menor es " + num2 + " y entre ellos existen " + dif + " números enteros."
Fin
"""

# Python

num1 = int(input("Dame un número entero:\n"))
num2 = int(input("Dame un otro número entero:\n"))

if num1 == num2:
    print(f"Los números no pueden ser iguales.")
else:
    if num1 < num2:
        dif = num2 - num1
        print(f"El número menor es {num1} y entre ellos existen {dif} números enteros.")
    else:
        dif = num1 - num2
        print(f"El número menor es {num2} y entre ellos existen {dif} números enteros.")
