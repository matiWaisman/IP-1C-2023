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


def clonar_sin_comentarios(nombre_archivo: str):
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    nuevo_archivo = open(nombre_archivo + "sinComentarios", "w")
    for linea in lineas:
        if(not (tiene_numeral(linea))):
            nuevo_archivo.write(linea)
    return nuevo_archivo


def tiene_numeral(linea: str) -> bool:
    res: bool = False
    linea_sin_espacios: str = linea.replace(" ", "")
    if(linea_sin_espacios[0] == "#"):
        res = True
    return res

# Ejercicio 3


def archivo_reverso(nombre_archivo: str):
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    nuevo_archivo = open(nombre_archivo + "reverso", "w")
    for i in range(len(lineas) - 1, -1, -1):
        nuevo_archivo.write(lineas[i])
    return nuevo_archivo

# Ejercicio 4


def agregar_texto_al_final(nombre_archivo: str, texto: str):
    archivo = open(nombre_archivo, "a")
    archivo.write("\n" + "\n"+texto)
    archivo.close()

# Ejercicio 5


def agregar_texto_al_principio(nombre_archivo: str, texto: str):
    archivo = open(nombre_archivo, "r+")
    lineas = archivo.readlines()
    archivo.seek(0)
    archivo.write(texto + "\n" + "\n")
    for linea in lineas:
        archivo.write(linea)
    archivo.close()


# Ejercicio 6

def leer_archivo_binario(nombre_archivo: str) -> list[(str)]:
    res: list[(str)] = []
    archivo = open(nombre_archivo, "rb")
    lineas = archivo.readlines()
    for linea in lineas:
        if(len(linea) >= 5):
            res.append(linea)
    archivo.close()
    return res

# Ejercicio 7

# def calcular_promedio_csv(nombre_archivo: str, lu: str) -> int: Espero a ver bien diccionarios y paso el csv a diccionario para parsear


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

# Ejercicio 10


def cantidad_elementos_pila(
    p: Pila([(any)])) -> int: return p.qsize()  # len(p) no funciona


def cantidad_elementos_pila_manual(p: Pila([(any)])) -> int:
    res: int = 0
    copia_pila = copiar_pila(p)
    while(not copia_pila.empty()):
        res += 1
        copia_pila.get()
    return res

# Ejercicio 11


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


# Ejercicio 12

# Preguntar mi solucion si es lo esperado
def esta_bien_balanceada(s: str) -> bool:
    res: bool = False
    p: Pila() = pasar_string_a_pila(s)
    contador_parentesis: int = 0
    for i in range(0, p.qsize(), 1):
        valor_actual: str = p.get()
        if(valor_actual == "("):
            contador_parentesis += 1
        if(valor_actual == ")"):
            contador_parentesis -= 1
    if(contador_parentesis == 0):
        res = True
    return res


def pasar_string_a_pila(s: str) -> Pila():
    res: Pila() = Pila()
    for c in s:
        res.put(c)
    return res

# Ejercicio 13

# Para imprimirlo hay que usar .queue despues de llamar a la funcion


def generar_cola_nros_al_azar(n: int, desde: int, hasta: int) -> Cola():
    res: Cola() = Cola()
    for i in range(0, n, 1):
        res.put(generar_numero_random(desde, hasta))
    return res

# Ejercicio 14


def cantidad_elementos_cola(
    c: Cola([(any)])) -> int: return c.qsize()  # len(c) no funciona


def cantidad_elementos_cola_manual(c: Cola([(any)])) -> int:
    res: int = 0
    copia_cola = copiar_cola(c)
    while(not copia_cola.empty()):
        res += 1
        copia_cola.get()
    return res


def copiar_cola(c: Cola()) -> Cola():
    lista_intermedia = []
    nueva_cola = Cola()
    while(c.empty() == False):
        lista_intermedia.append(c.get())
    for i in range(0, len(lista_intermedia), 1):
        nueva_cola.put(lista_intermedia[i])
        c.put(lista_intermedia[i])
    return nueva_cola

# Ejercicio 15


def buscar_maximo_de_cola_while(c: Cola([(int)])) -> int:
    res: int = 0
    copia_cola = copiar_cola(c)
    valor_actual: int = copia_cola.get()
    termino: bool = copia_cola.empty()
    while(termino != True):
        if(valor_actual > res):
            res = valor_actual
        valor_actual = copia_cola.get()
        if(copia_cola.empty()):
            termino = True
            if(valor_actual > res):
                res = valor_actual
    return res


def buscar_maximo_de_cola_for(q:  Cola([(int)])) -> int:
    res: int = 0
    copia_cola = copiar_cola(q)
    for i in range(0, copia_cola.qsize(), 1):
        valor_actual: int = copia_cola.get()
        if(valor_actual > res):
            res = valor_actual
    return res


# Ejercicio 16

def armar_secuencia_de_bingo() -> Cola[int]:
    res: Cola[int] = Cola()
    for i in range(0, 12, 1):
        numero_actual: int = generar_numero_random(0, 99)
        while(pertenece_cola(numero_actual, res)):  # Para evitar repetidos
            numero_actual = generar_numero_random(0, 99)
        res.put(generar_numero_random(0, 99))
    return res


def pertenece_cola(n: int, q:  Cola([(int)])) -> bool:
    res: bool = False
    copia_cola: Cola([(int)]) = copiar_cola(q)
    for i in range(0, copia_cola.qsize(), 1):
        valor_actual: int = copia_cola.get()
        if(valor_actual == n):
            res = True
    return res


# def jugar_carton_de_bingo(carton: list([int]), bolillero:  Cola([(int)])) -> int: # Preguntar como se juega al bingo y si uso una lista o una lista de listas

# Ejercicio 17

def numero_pacientes_urgentes(q: Cola[(int, str, str)]) -> int:
    res: int = 0
    copia_cola: Cola([(int, str, str)]) = copiar_cola(q)
    for i in range(0, copia_cola.qsize(), 1):
        valor_actual = copia_cola.get()
        if(valor_actual[0] >= 3):
            res += 1
    return res


c = Cola()
c.put(67)
c.put(2)
c.put(5)
c.put(4)
bingo = armar_secuencia_de_bingo()


# Ejercicio 18

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    res: dict = {}
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    for linea in lineas:
        acumulador: int = 0
        for caracter in linea:
            if(caracter != " "):
                acumulador += 1
            if(caracter == " "):
                if acumulador in res:
                    res[acumulador] += 1
                else:
                    res[acumulador] = 1  # Tengo que inicializarlo
                acumulador = 0
    return res


def la_palabra_que_mas_aparece(nombre_archivo: str) -> str:
    res: str = ""
    d: dict = calcular_cantidad_apariciones(nombre_archivo)
    numero_mayor_cantidad: int = calcular_numero_que_mas_aparece(d)
    for clave in d:
        if(d[clave] == numero_mayor_cantidad):
            res = clave
    return res


def calcular_numero_que_mas_aparece(d: dict) -> int:
    res: int = 0
    for clave in d:
        if(d[clave] > res):
            res = d[clave]
    return res


def calcular_cantidad_apariciones(nombre_archivo: str) -> dict:
    res: dict = {}
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()
    for linea in lineas:
        acumulador: str = ""
        for caracter in linea:
            if(caracter != " "):
                acumulador = acumulador + caracter
            if(caracter == " "):
                if acumulador in res:
                    res[acumulador] += 1
                else:
                    res[acumulador] = 1  # Tengo que inicializarlo
                acumulador = ""
    return res
