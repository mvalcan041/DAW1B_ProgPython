
total = int(input("¿Cuántas notas vas a introducir?:\n"))

while total < 1 or total > 100:
    print(f"Error, el número de notas debe ser un número entero entre 1 y 100.")
    total = int(input("¿Cuántas notas vas a introducir?:\n"))

notas = input(f"Dame las {total} notas del curso:\n").split()
notas == int

media = 0
cont = 1

while cont <= 10:
    media += notas()
    cont += 1

media = media / total
print(f"La media es {media}.")

# Sin acabar.
