
def multiplicar (horas, coste):
    res = horas * coste
    return res

horas = int(input("Horas de trabajo: "))
coste = int(input("Coste por hora: "))

print(f"Importe total: {multiplicar(horas, coste)}")