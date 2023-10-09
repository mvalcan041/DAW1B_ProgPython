
con_iva = float(input("Dime el importe final del artículo (€): "))

iva = con_iva * 0.10
sin_iva = con_iva - iva

print(f"Se ha pagado {iva}€ de un IVA al 10%.\nSin impuestos, el importe del artículo es de {sin_iva}€.")
