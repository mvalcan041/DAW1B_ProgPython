
total = int(input("¿Cuántas notas vas a introducir?:\n"))

while total < 1 or total > 100:
    print(f"Error, el número de notas debe ser un número entero entre 1 y 100.")
    total = int(input("¿Cuántas notas vas a introducir?:\n"))

print(f"Dame las {total} notas del curso: ")  # Print, que no input

media = 0
cont = 1
while cont <= total:
    nota = float(input())   # Ahora sí pedimos un input de cada nota, hasta total en un while
    media = media + nota
    cont = cont + 1

media = media/total
print(f"La media es {media:.2f}")
