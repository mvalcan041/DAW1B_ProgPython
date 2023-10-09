
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Indique aquí su fecha de nacimiento en formato dd/mm/aaaa:\n")

dia, mes, año = fecha.split("/")

if (int(dia) <= 31) and (int(mes) <= 12) and (int(año) <= 2023):
    print(f"El día es {dia}.")
    print(f"El mes es {mes}.")
    print(f"El año es {año}.")

else:
    print("Error en el formato usado, revise los datos introducidos.")
