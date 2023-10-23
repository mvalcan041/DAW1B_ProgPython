
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

dinero_depositado = float(input("Introduzca la cantidad de dinero depositada en la cuenta (€):\n"))

interes = dinero_depositado * (1 + 0.04)
print(f"Ahorros en el primer año: {interes:.2f}€.")

interes = interes * (1 + 0.04)
print(f"Ahorros en el segundo año: {interes:.2f}€.")

interes = interes * (1 + 0.04)
print(f"Ahorros en el tercer año: {interes:.2f}€.")
