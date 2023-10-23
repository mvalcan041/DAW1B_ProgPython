
def aplicar_iva (sin_iva, iva):
    importe_iva = sin_iva * (iva/100)
    con_iva = sin_iva + importe_iva
    return con_iva

sin_iva = float(input("Dime el importe del artículo (€):\n"))
iva = float(input("Dime el IVA que quieres aplicar (%):\n"))

print(f"El precio final con IVA incluído es {aplicar_iva(sin_iva, iva)}€.")
