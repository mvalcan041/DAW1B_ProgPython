
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Indique aquí su peso en kilogramos (kg):\n"))
estatura = float(input("Indique aquí su estatura en metros (m):\n"))

masa_corporal = peso / (estatura ** 2)

print(f"Tu índice de masa corporal es {masa_corporal:.2f}")
