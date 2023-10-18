
num = 3
total = int(input("Dime cuántos números debe tener la serie:\n"))

cont = 1
while cont <= total:
    print(num, end= "")
    if cont < total:
        print(" ")
    num += 3
    cont += 1
