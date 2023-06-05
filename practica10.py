import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

# Ejercicio 8

def generar_lista_nros_al_azar(n: int, desde: int, hasta: int) -> list([int]): 
    res: list[(int)] = []
    for i in range(0, n, 1): 
        res.append(generar_numero_random(desde, hasta))
    return res

def generar_numero_random(desde: int, hasta: int) -> int: 
    res = random.randint(desde, hasta)
    return res

# Ejercicio 9

def generar_pila_nros_al_azar(n: int, desde: int, hasta: int) -> Pila([(int)]): # Para imprimirlo hay que usar .queue despues de llamar a la funcion
    res: Pila([(int)]) = Pila([(int)])
    for i in range(0, n, 1): 
        res.put(generar_numero_random(desde, hasta))
    return res


def cantidad_elementos_pila(p: Pila([(any)])) -> int: return p.qsize() # len(p) no funciona

def buscar_maximo_de_pila(p: Pila([(int)])) -> int: # Esta implementacion borra la pila implementar con un for que corte uno antes
    res: int = 0
    copia_pila = copiar_pila(p)
    valor_actual : int = copia_pila.get()
    termino: bool = copia_pila.empty()
    while(termino != True): 
        if(valor_actual > res): 
            res = valor_actual
        valor_actual = copia_pila.get()
        if(copia_pila.empty()): 
            termino = True
            if(valor_actual > res): 
                res = valor_actual
    return res

def copiar_pila(p: Pila()) -> Pila(): 
    lista_intermedia = []
    nueva_pila = Pila()
    while(p.empty() == False): 
        lista_intermedia.append(p.get())
    for i in range(len(lista_intermedia), 0, -1): 
        nueva_pila.put(lista_intermedia[i])
        p.put(lista_intermedia[i])
    return nueva_pila



p = Pila()
p.put(4)
p.put(3)
p.put(2)
p.put(1)

# Ejercicio 13 

def generar_cola_nros_al_azar(n: int, desde: int, hasta: int) -> Cola(): # Para imprimirlo hay que usar .queue despues de llamar a la funcion
    res: Cola() = Cola()
    for i in range(0, n , 1): 
        res.put(generar_numero_random(desde, hasta))
    return res 

# Ejercicio 14

def cantidad_elementos_cola(c: Cola([(any)])) -> int: return c.qsize() # len(c) no funciona

# Ejercicio 18 

def agrupar_por_longitud(nombre_archivo: str) -> dict: 
