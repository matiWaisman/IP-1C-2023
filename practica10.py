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

# Asumiendo que la primer linea es el encabezado


def calcular_promedio_csv(nombre_archivo: str, lu: str) -> float:
    res: float = 0
    acumulador_notas: float = 0
    cantidad_notas: int = 0
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    for i in range(1, len(lineas), 1):
        valores = lineas[i].strip().split(',')
        if(valores[0] == lu):
            acumulador_notas += float(valores[3])
            cantidad_notas += 1
    res = acumulador_notas/cantidad_notas
    return res


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

def esta_bien_balancea(s: str) -> bool: 
    res: bool = True
    pila_abiertos: Pila() = Pila()
    for letra in s: 
        if(letra == "("): 
            pila_abiertos.put(letra)
        if(letra == ")"):
            if(pila_abiertos.empty()): 
                res = False
            else: 
                pila_abiertos.get()
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
    for i in range(0, 100, 1):
        numero_actual: int = generar_numero_random(0, 99)
        while(pertenece_cola(numero_actual, res)):  # Para evitar repetidos
            numero_actual = generar_numero_random(0, 99)
        res.put(numero_actual)
    return res

def pertenece_cola(n: int, q:  Cola([(int)])) -> bool:
    res: bool = False
    copia_cola: Cola([(int)]) = copiar_cola(q)
    for i in range(0, copia_cola.qsize(), 1):
        valor_actual: int = copia_cola.get()
        if(valor_actual == n):
            res = True
    return res

def armar_carton_bingo() -> list([int]): # No va a ser una matriz como deberia, uso una lista de 15 y cuando me quede sin 15 gano 
    res: list([int]) = []
    for i in range(0, 15, 1 ):
        numero_actual: int =  generar_numero_random(0, 99)
        while(pertenece_lista(res, numero_actual)): 
            numero_actual = generar_numero_random(0, 99)
        res.append(numero_actual)
    return res

def jugar_carton_de_bingo(carton: list([int]), bolillero:  Cola([(int)])) -> int: 
    res: int = 0
    print(bolillero.queue)
    print(carton)
    while(len(carton) > 0): 
        bola_actual: int = bolillero.get()
        if(pertenece_lista(carton, bola_actual)): 
            carton = eliminar_de_lista(carton, bola_actual)
        if(len(carton) > 0): # Agrego esto porque si no suma una jugada de mas
            res += 1  
    return res


def pertenece_lista(l: list([int]), e: int) -> bool: 
    res: bool = False
    for i in range(0, len(l), 1):
        if(l[i] == e): res = True
    return res


def eliminar_de_lista(l: list([int]), e: int) -> list([int]): 
    res: list([int]) = []
    for i in range(0, len(l), 1): 
        if(l[i] != e): 
            res.append(l[i])
    return res

print(jugar_carton_de_bingo(armar_carton_bingo(), armar_secuencia_de_bingo()))

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
    archivo.close()
    for linea in lineas:
        acumulador: int = 0
        for caracter in linea:
            if(caracter != " "):
                acumulador += 1
            else:
                if acumulador in res:
                    res[acumulador] += 1
                else:
                    res[acumulador] = 1  # Hay que inicializarlo
                acumulador = 0
    return res


# Ejercicio 19

# Esta impementacion no es la manera para resolver el ejercicio, lo que hago es pasar el csv a diccionario y ahi resolver el ejercicio en vez de leyendo un csv leyendo un dict
# Asumiendo que la primer linea es el encabezado
def pasar_csv_a_dict(nombre_archivo: str) -> dict:
    res: dict = {}
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    claves_internas: list([str]) = armar_lista_claves(lineas[0])
    for i in range(1, len(lineas), 1):  # Accedo a las lineas
        linea_actual: list([str]) = lineas[i].strip().split(',')
        lu_alumno: str = linea_actual[0]
        valores_linea_actual: dict = armar_dict_valores(linea_actual, claves_internas)
        if(lu_alumno in res):
            # No funciona, preguntar como terminarlo se me ocurren metodos manuales de hacerlo pero son demasiado largos, tiene que haber alguna manera de hacer un append facilito
            res[lu_alumno].append(valores_linea_actual)
        else:
            res[lu_alumno] = [valores_linea_actual]  # Hay que inicializarlo
    return res

""""
Modelo respuesta que quiero: 
{
    "202101": [
        {
            "materia": "Matemáticas",
            "fecha": "2023-05-01",
            "nota": 8.5
        },
        {
            "materia": "Programación",
            "fecha": "2023-05-15",
            "nota": 7.2
        },
        {
            "materia": "Historia",
            "fecha": "2023-05-15",
            "nota": 6.5
        }
    ],
    "202102": [
        {
            "materia": "Inglés",
            "fecha": "2023-04-28",
            "nota": 9.1
        }
    ],
    "202103": [
        {
            "materia": "Física",
            "fecha": "2023-05-10",
            "nota": 6.8
        },
        {
            "materia": "Historia",
            "fecha": "2023-04-30",
            "nota": 7.5
        }
    ],
    "202104": [
        {
            "materia": "Economía",
            "fecha": "2023-05-06",
            "nota": 8.9
        }
    ]
}
"""


def armar_dict_valores(l: list([str]), claves: list([str])) -> dict:
    res: dict = {}
    for i in range(1, len(l), 1):
        res[claves[i]] = l[i]
    return res


def armar_lista_claves(linea: list([str])) -> list([str]):
    res: list([str]) = []
    valores = linea.strip().split(',')
    for i in range(0, len(valores), 1):
        res.append(valores[i])
    return res

# Ejercicio 20


def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
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
    archivo.close()
    for linea in lineas:
        acumulador: str = ""
        for caracter in linea:
            if(caracter != " "):
                acumulador = acumulador + caracter
            else:
                if acumulador in res:
                    res[acumulador] += 1
                else:
                    res[acumulador] = 1  # Hay que inicializarlo
                acumulador = ""
    return res
