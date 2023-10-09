
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

ventas_pan_ayer = int(input("Número de barras vendidas que no son del día:\n"))

precio_pan = 3.49
precio_pan_ayer = 3.49 * 0.6
descuento_pan_ayer = precio_pan - precio_pan_ayer

print(f"El precio habitual de una barra de pan es de {precio_pan}€.\nEl descuento que se le hace a una barra de pan por no ser fresca es de {descuento_pan_ayer:.2f}€.\nEl coste final total de las {ventas_pan_ayer} barras de pan vendidas que no son del día es de {(precio_pan_ayer * ventas_pan_ayer):.2f}€.")
