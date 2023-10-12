
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

numero_telefono = input("Indique un número de teléfono con el siguiente formato '+34-XXXXXXXXX-XX':\n")

if numero_telefono[:4] == "+34-" and numero_telefono[13] == "-" and len(numero_telefono) == 16:
    print(f"El número de teléfono introducido sin el prefijo y la extensión es {numero_telefono[4:13]}.")

else:
    print(f"El formato que has introducido es incorrecto. Asegúrese que usa el formato '+34-XXXXXXXXX-XX'.")
