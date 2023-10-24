
# "Práctica 2.1.1"
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def edad (num):
    if num >= 18:
        return True
    else:
        return False
    
def main():
    num = int(input(f"Indique su edad:\n"))

    if edad(num):
        print(f"Genial, eres mayor de edad.")
    else:
        print(f"Lo siento, eres menor de edad.")

if __name__ == "__main__":
    main()
