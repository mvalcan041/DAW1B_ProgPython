
x = int(input("Indique un número:\n"))
y = int(input("Indique otro número:\n"))

if x >= y:
    numIni = y
    numFin = x
else:
    numIni = x
    numFin = y

while (numIni <= numFin):
    print(numIni, end= "")    # end= "" para evitar saltar de línea con cada print
    if (numIni != numFin):
        print("-", end= "")
    numIni = numIni + 1
