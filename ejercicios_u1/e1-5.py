
sin_iva = float(input("Dime el importe del artículo (€):\n"))
iva = float(input("Dime el IVA que quieres aplicar (%):\n"))

importe_iva = sin_iva * (iva/100)
con_iva = sin_iva + importe_iva

print(f"El precio final con IVA incluído es {con_iva}€.")
