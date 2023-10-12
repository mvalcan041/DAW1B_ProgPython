
# Lee un número hasta que el número esté en el rango 1-10.

num = int(input("Indique un número:\n"))

while (num > 10) or (num < 1):
    num = int(input(f"Error, inténtalo de nuevo (1-10): \n"))

print(f"¡Correcto, ese es un número válido!")
