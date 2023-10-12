
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Introduce una frase cualquiera:\n")
vocal = input("Introduce la vocal a remarcar: \n")

if vocal in "aeiouAEIOU":
    frase_cambiada = frase.replace(vocal, vocal.upper())

print(frase_cambiada)

# Usando frase.replace(vocal, vocal.upper())
