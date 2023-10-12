
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Introduzca una frase:\n").split()

frase_cambiada = frase[::-1]

print(frase_cambiada)
