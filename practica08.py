# Ejercicio 1

def pertenece(l: list([int]), e: int) -> bool: 
    res: bool = False
    for i in range(0, len(l), 1):
        if(l[i] == e): res = True
    return res

def pertenece_while(l: list([int]), e: int) -> bool: 
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
    

def es_palindroma(palabra: str) -> bool:
    res: bool = False
    i: int = 0
    sigo: bool = True
    while i <= ((len(palabra) - 1)  / 2) and sigo == True:
        if(palabra[i] != palabra[len(palabra) - 1 - i]): 
            sigo = False
        if(i == ((len(palabra) - 1) / 2) and sigo == True): 
            res = True
        i += 1
    return res

#print(esPalindroma("holloh")) # Arreglar impares

def es_palindroma_lenta(palabra: str) -> bool: return (palabra == invertir_palabra(palabra)) 

def invertir_palabra(palabra: str) -> str: 
    res: str = ""
    for i in range(len(palabra) - 1, -1, -1): 
        res += palabra[i]
    return res


# Ejercicio 2 

listaAlterada = [1,2,3,4,5] 

def alterar_lista(l: list([int])) :
    l[3] = 2


def alterar_lista_por_copia(l: list([int])): 
    res = l
    res[3] = 2 
    return res

        
