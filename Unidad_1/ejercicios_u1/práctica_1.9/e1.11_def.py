
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

# n = int(input("Introduzca un número: "))

# suma = (n * (n + 1)) /2

# print(f"La suma de los primeros números enteros hasta {n} es {suma}.")

def suma_n (n):
    suma = int((n * (n + 1)) /2)
    return suma

n = int(input("Introduzca un número: "))
print(f"La suma de los primeros números enteros hasta {n} es {suma_n(n)}.")
