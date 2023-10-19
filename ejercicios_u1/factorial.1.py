
def factorial (num: int):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total

print(f"El factorial de 4 es {factorial(4)}.")

# 4, que es "num", es totalmente distinto al num llamado en la función.

# En el otro ejemplo, se podría llamar num como una string, pero la llamamos número
# para distinguirla que la num que llamamos en la función.