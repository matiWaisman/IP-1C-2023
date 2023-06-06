import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

# Ejercicio 1

def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()  # Lista de tuplas
    res: int = len(lineas)
    return res


def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    res: bool = False
    texto = open(nombre_archivo).read().split()
    for p in texto:
        if p == palabra:
            res = True
            break
    return res


def cantidad_apariciones(palabra: str, nombre_archivo: str) -> int:
    res: int = 0
    texto = open(nombre_archivo).read().split()
    for p in texto:
        if p == palabra:
            res += 1
    return res

# Ejercicio 2

# def clonar_sin_comentarios(nombre_archivo: str) -> str:


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


# Para imprimirlo hay que usar .queue despues de llamar a la funcion
def generar_pila_nros_al_azar(n: int, desde: int, hasta: int) -> Pila([(int)]):
    res: Pila([(int)]) = Pila([(int)])
    for i in range(0, n, 1):
        res.put(generar_numero_random(desde, hasta))
    return res


def cantidad_elementos_pila(
    p: Pila([(any)])) -> int: return p.qsize()  # len(p) no funciona


def cantidad_elementos_pila_manual(p: Pila([(any)])) -> int:
    res: int = 0
    copia_pila = copiar_pila(p)
    while(not copia_pila.empty()):
        res += 1
        copia_pila.get()
    return res


# implementar con un for que corte uno antes

def buscar_maximo_de_pila_for(p:  Pila([(int)])) -> int:
    res: int = 0
    copia_pila = copiar_pila(p)
    for i in range(0, copia_pila.qsize(), 1):
        valor_actual: int = copia_pila.get()
        if(valor_actual > res):
            res = valor_actual
    return res


def buscar_maximo_de_pila_while(p: Pila([(int)])) -> int:
    res: int = 0
    copia_pila = copiar_pila(p)
    valor_actual: int = copia_pila.get()
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
    for i in range(len(lista_intermedia) - 1, -1, -1):
        nueva_pila.put(lista_intermedia[i])
        p.put(lista_intermedia[i])
    return nueva_pila


p = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
p.put(5)

print(cantidad_elementos_pila_manual(p))

# Ejercicio 13


# Para imprimirlo hay que usar .queue despues de llamar a la funcion
def generar_cola_nros_al_azar(n: int, desde: int, hasta: int) -> Cola():
    res: Cola() = Cola()
    for i in range(0, n, 1):
        res.put(generar_numero_random(desde, hasta))
    return res

# Ejercicio 14


def cantidad_elementos_cola(c: Cola([(any)])) -> int: return c.qsize()  # len(c) no funciona

# Ejercicio 18

# def agrupar_por_longitud(nombre_archivo: str) -> dict:
