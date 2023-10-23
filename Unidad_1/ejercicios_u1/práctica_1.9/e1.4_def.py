
def temp (celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Introduce una temperatura en grados Celsius: "))
print(f"{celsius} grados Celsius son {temp(celsius)} grados Fahrenheit.")
