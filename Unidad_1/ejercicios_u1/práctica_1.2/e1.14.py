
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payasos = int(input("Número de ventas del artículo Payasos en el último pedido:\n"))
muñecas = int(input("Número de ventas del artículo Muñecas en el último pedido:\n"))

peso_total = (payasos * 112) + (muñecas * 75)

print(f"Peso total del paquete a enviar: {peso_total} g.")
