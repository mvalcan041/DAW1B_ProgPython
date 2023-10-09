
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input("Introduzca su nombre completo:\n")

print(nombre_completo.lower())
print(nombre_completo.upper())

list = []
list = nombre_completo.split()
contador = 0
nombre_completo = ""

for i in list:
    nombre_completo = nombre_completo + list[contador].title() + " "
    contador += 1

print(nombre_completo)

# nombre_completo = input("Nombre completo: ")
# print(nombre.lower()) ...
# print(nombre.upper()) ...
# print(nombre.title())
