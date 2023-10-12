
x = int(input("Indique un número:\n"))
y = int(input("Indique otro número:\n"))

if x >= y:
    numIni = x - 1
    numFin = y
else:
    numIni = y - 1
    numFin = x

for i in (numIni, numFin):
    print(f"{i} +")
    if (numIni != numFin):
        print(f"-")

# Está mal en su pseudocódigo.
