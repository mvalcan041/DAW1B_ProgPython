
n1, n2 = map(int, input("Indique 2 números:\n").split())
opcion = 0

while opcion < 1 or opcion > 4:
    opcion = int(input("Indique una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División):\n"))
    if opcion < 1 or opcion > 4:
        print(f"Error, no es una opción correcta (1-4)")

if opcion == 1:
    print(f"{n1} + {n2} = {n1 + n2}")
elif opcion == 2:
    print(f"{n1} - {n2} = {n1 - n2}")
elif opcion == 3:
    print(f"{n1} * {n2} = {n1 * n2}")
elif opcion == 4:
    if n2 == 0:
        print(f"La división entre 0 no es posible.")
    else:
        print(f"{n1} / {n2} = {n1/n2}")
