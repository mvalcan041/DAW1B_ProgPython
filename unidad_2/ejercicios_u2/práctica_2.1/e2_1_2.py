
# "Práctica 2.1.2"
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def pswdTrue (pswdInput):
    
    if pswdInput.lower() == "contraseña":
        return True
    else:
        return False

def main():
    pswd = input(f"Indique una contraseña:\n")
    
    if pswdTrue(pswd):
        print(f"Correcto, la contraseña es 'contraseña'.")
    else:
        print(f"Lo siento, no es esa contraseña.")

if __name__ == "__main__":
    main()
    