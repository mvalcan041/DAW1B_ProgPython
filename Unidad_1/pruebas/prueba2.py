
def comparacion (num1, num2):
    if num1 == num2:
        num_mayor = 0
        return num_mayor
    elif num1 > num2:
        num_mayor = num1
        return num_mayor
    else:
        num_mayor = num2
        return num_mayor
    
def main():
    num1 = int(input(f"Dime un número: "))
    num2 = int(input(f"Dime otro número: "))

    print(f"El número mayor es {comparacion(num1, num2)}.")

if __name__ == "__main__":
    main()
