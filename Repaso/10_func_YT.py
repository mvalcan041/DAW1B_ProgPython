# # Funciones # #

def mi_funcion (): # Definida función sin parámetros
    print("Esto es una función")

mi_funcion () # Llamada de función sin argumentos
mi_funcion ()
mi_funcion ()

def suma_dos_numeros (value1, value2): # Definida función con parámetros
    print(value1 + value2)

suma_dos_numeros (5, 7) # Llamada de función con argumentos; 
suma_dos_numeros (524234, 72423)
suma_dos_numeros ("5", "7")
suma_dos_numeros (1.4, 5.2)

def suma_dos_numeros_con_retorno (value1, value2):
    mi_suma = value1 + value2
    return mi_suma

mi_resultado = suma_dos_numeros (1.4, 5.2)
print(mi_resultado)

mi_resultado = suma_dos_numeros_con_retorno(10, 5)
print(mi_resultado)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname ="Canalejas", name = "Mario")