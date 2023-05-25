# Ejercicio 1

def pertenece(l: list([int]), e: int) -> bool: 
    res: bool = False
    for i in range(0, len(l), 1):
        if(l[i] == e): res = True
    return res

def pertenece_while(l: list([str]), e: str) -> bool: 
    res: bool = False
    sigo: bool = True
    i: int = 0
    while (i < len(l) and sigo == True): 
        if(l[i] == e): 
            res = True
            sigo = False
        i += 1
    return res

# Preguntar como hacer para que la lista y el elemento sean del mismo tipo de dato generico como haciamos en haskell

def divide_a_todos(l: list([int]), e: int) -> bool: 
    res: bool = False
    sigo: bool = True
    i: int = 0
    while (i < len(l) and sigo == True):
        if(i == len(l) - 1 and l[i] % e == 0): res = True
        if(l[i] % e != 0): sigo = False
        i += 1 
    return res


def sumaTotal (l: list([int])) -> int:
    res: int = 0
    for i in range(0,len(l),1):
        res += l[i]
    return res

def ordenados (l: list([int])) -> bool: 
    res: bool = False
    i: int = 1
    sigo: bool = True
    while i < len(l) and sigo == True:
        if(l[i] < l[i-1]):
            sigo = False
        if(i == len(l) - 1 and sigo == True):
            res = True
        i += 1
    return res

def alguna_palabra_larga(l: list([str]), longitud: int) -> bool: 
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i < len(l) and sigo == True:
        if(len(l[i]) > longitud): 
            res = True
            sigo = False
        i += 1
    return res
    

def es_palindroma(palabra: str) -> bool: # Se podria usar returns en vez de los ifs para hacer mas eficiente, pero se nos indico que solo puede haber un return
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i <= ((len(palabra) - 1)  / 2) and sigo == True:
        if(palabra[i] != palabra[len(palabra) - 1 - i]): 
            sigo = False
        if(i == ((len(palabra) - 1) / 2) and sigo == True): # Este funciona para cantidad de letras impares
            res = True
        if(i + 1 == (len(palabra) / 2) and sigo == True): # Este funciona para cantidad de letras pares
            res = True
        i += 1
    return res

def es_palindroma_lenta(palabra: str) -> bool: return (palabra == invertir_palabra(palabra)) 

def invertir_palabra(palabra: str) -> str: 
    res: str = ""
    for i in range(len(palabra) - 1, -1, -1): 
        res += palabra[i]
    return res

def evaluar_contra(palabra:str) -> str: 
    res: str = "Amarilla"
    if(len(palabra) < 5): res = "Roja"
    if(len(palabra) > 8 and tiene_letra_mayuscula and tiene_letra_minuscula and tiene_letra_minuscula): res ="Verde"
    return res

def tiene_letra_minuscula(palabra:str) -> bool:
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i < len(palabra) and sigo == True: 
        if palabra[i].islower(): 
            res = True
            sigo = False
        i += 1
    return res

def tiene_letra_mayuscula(palabra:str) -> bool:
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i < len(palabra) and sigo == True: 
        if palabra[i].isupper(): 
            res = True
            sigo = False
        i += 1
    return res

def tiene_letra_numerica(palabra:str) -> bool:
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i < len(palabra) and sigo == True: 
        if palabra[i].isnumeric(): 
            res = True
            sigo = False
        i += 1
    return res

def saldo_bancario(historial: list([(str,int)])) -> int:
    res: int = 0
    for i in range(0, len(historial), 1):
        if(historial[i][0] == "I"):
            res += historial[i][1]
        if(historial[i][0] == "R"): 
            res -= historial[i][1]
    return res

def tiene_3_vocales_distintas(palabra:str) -> bool: 
    res: bool = False
    palabra_en_lower: str = palabra.lower()
    vocales: list([str]) = ["a","e","i","o","u"]
    vocales_en_uso: list([str]) = []
    i: int = 0
    sigo: bool = True
    while i < len(palabra) and sigo == True:
        if(pertenece_while(vocales, palabra_en_lower[i]) and not pertenece_while(vocales_en_uso, palabra_en_lower[i])): 
            vocales_en_uso.append(palabra_en_lower[i])
        if(len(vocales_en_uso) == 3): sigo = False
        i += 1
    if(len(vocales_en_uso) == 3): res = True
    return res

# Ejercicio 2 

lista = [1,2,3,4,5] 

def borrar_pares_de_lista_modificando_parametro(l: list([int])) -> list([int]):  
    res = l  
    for i in range(0,len(res),1):
        if res[i] % 2 == 0:
            res[i] = 0
    return res

def borrar_pares_de_lista_sin_modificar_original(l: list([int])) -> list([int]): 
    res = l[:]  
    for i in range(0,len(res),1):
        if res[i] % 2 == 0:
            res[i] = 0
    return res

def borrar_vocales(palabra: str) -> str: 
    vocales: list[(str)] = ["a","e","i","o","u"]
    palabra_en_lower: str = palabra[:].lower() 
    res: str = ""
    for i in range(0,len(palabra_en_lower),1):
        if(not pertenece_while(vocales, palabra_en_lower[i])): 
            res += palabra[i]
    return res

        
