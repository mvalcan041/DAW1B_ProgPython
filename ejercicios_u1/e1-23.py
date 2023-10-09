
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Introduzca aquí su correo electrónico:\n")

nombre, dominio = correo.split("@")
correo_cambiado = nombre + "@ceu.es"

print(f"{correo_cambiado}")

# print(mail[:mail.find("@")] + "@ceu.es")
# Hace print del correo, pero sólo la parte de antes del @, ya que con :mail.find("@") busca la posición del @ en el correo.
