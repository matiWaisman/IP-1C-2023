import math

# Ejercicio 1

def raiz_de_2 () -> int:
    return round(2 ** 0.5, 4)

def imprimir_hola () : print("Hello world")    

def imprimir_un_verso () : print ("I'll just keep playing back \nThese fragments of time \nEverywhere I go, this moment'll shine \nI'll just keep playing back These fragments of time \nEverywhere I go, this moment'll shine")

def factorial_de (x: int) -> int:
    res = 1 
    for i in range(1, x + 1):
        res = res * i 
    return res

# Ejercicio 2

def imprimir_saludo (nombre: str) : print (f"Hola {nombre}")

def raiz_cuadrada_de (n: int) -> int:
    return round(n ** 0.5, 4)

# def imprimir_dos_veces ()

def es_multiplo_de (n: int, m: int) -> bool: return m % n == 0 # Es multiplo n de m

def es_par (n: int) -> bool: return (es_multiplo_de(2, n))

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int: return (math.ceil((min_cant_de_porciones * comensales) / 8))

# Ejercicio 3

def alguno_es_0(n1: int, n2: int) -> bool: return (n1 == 0 or n2 == 0)

def ambos_son_0(n1: int, n2: int) -> bool: return (n1 == 0 and n2 == 0)

def es_nombre_largo(nombre: str) -> bool: return (len (nombre) >= 3 and len (nombre) <= 8)

def es_bisiesto(year: int) -> bool: return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

# Ejercicio 4

#def peso_pino(altura: int) -> int:  # Altura expresada en centimetros
#    for i in range 

# Ejercicio 5

def devolver_el_doble_si_es_par(n: int) -> int: 
    if (es_par(n)): return 2*n
    else: return n

# Ejercicio 6

def pares_entre(cota_inferior: int, cota_superior: int): 
    i = cota_inferior
    while i <= cota_superior:
        if (es_par(i)): print(i)
        i += 1 

# Ejercicio 7

def pares_entre_for(cota_inferior: int, cota_superior: int): 
    for i in range (cota_inferior, cota_superior + 1):
        if (es_par(i) and i): print(i)

