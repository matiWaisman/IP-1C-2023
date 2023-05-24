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

def peso_pino(altura_total: int) -> int:  # Altura expresada en centimetros
    res: int = 0
    altura_arriba_de_3: int = altura_total - 300
    if(altura_arriba_de_3 > 0):
        res = (altura_total - altura_arriba_de_3) * 3 + altura_arriba_de_3 * 2
    else: 
        res = altura_total * 3
    return res

def es_peso_util(peso_total: int) -> bool: return (peso_total >= 400 and peso_total <= 1000)

def sirve_pino(altura_total: int) -> bool: return (es_peso_util(peso_pino(altura_total)))



# Ejercicio 5

def devolver_el_doble_si_es_par(n: int) -> int: 
    res: int = n
    if (es_par(n)): res = 2*n
    return res

def devolver_valor_si_es_par_sino_el_que_sigue (n) -> int: 
    res: int = 0
    if(es_par(n)): res = n
    else: res = n + 1
    return res  

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n) -> int: 
    res: int = n
    if(es_multiplo_de(9,n)): res = 3 * n
    if(es_multiplo_de(3,n) and es_multiplo_de(9,n) == False): res = 2 * n
    return res

def que_tan_grande_es_tu_nombre(nombre: str) -> str: 
    res: str = ""
    if(len(nombre) >= 5): res = "Tu nombre tiene muchas letras!"
    else: res = "Tu nombre tiene menos de 5 caracteres"
    return res

def te_toca_irte_de_vacaciones(sexo: str, edad: int) -> str:
    res: str = "Anda a trabajar"
    if ((edad >= 65 and sexo=="M") or (edad >= 60 and sexo=="F")): res = "Anda de vacaciones" 
    if (edad < 18): res= "Anda de vacaciones"
    return res


# Ejercicio 6

def numeros_entre_1_y_10(): 
    i: int = 1
    while(i <= 10): 
        print(i)
        i+=1

def numeros_pares_entre_10_y_40(): 
    i: int = 10
    while(i <= 40):
        if(es_par(i)): print(i)
        i+=1

def pares_entre(cota_inferior: int, cota_superior: int): 
    i = cota_inferior
    while i <= cota_superior:
        if (es_par(i)): print(i)
        i += 1 

def cuenta_regresiva(n: int): 
    i: int = n
    while(i > 0): 
        print(i)
        i = i - 1 
    print("Despegue")

def viaje_en_el_tiempo(partida:int, llegada: int):
    i: int = partida
    while(i >= llegada): 
        print(f"Viajó un año en el pasado, estamos en el año: {i}")
        i = i - 1

def viaje_a_aristoteles(partida: int): 
    i = partida
    while(i >= -384): 
        print(f"Viajó un año en el pasado, estamos en el año: {i}")
        i = i - 20


# Ejercicio 7

def pares_entre_for(cota_inferior: int, cota_superior: int): 
    for i in range (cota_inferior, cota_superior + 1):
        if (es_par(i) and i): print(i)

