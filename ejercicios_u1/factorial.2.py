
def factorial (num: int):
    total = 1
    resultado = str(num) + "! => "
    while num > 0:
        resultado += str(num)
        if num != 1:
            resultado += " x "
        total *= num
        num -= 1
    resultado += " = " + total
    return resultado

numero = input("Introduce un número:\n")
print(f"El factorial de 4 es {factorial(numero)}.")
