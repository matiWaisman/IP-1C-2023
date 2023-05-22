# Ejercicio 1

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

def esPalindroma(palabra: str) -> bool:
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

print(esPalindroma("holloh")) # Arreglar impares

# Ejercicio 2 

listaAlterada = [1,2,3,4,5] 

def alterar_lista(l: list([int])) :
    l[3] = 2


def alterar_lista_por_copia(l: list([int])): 
    res = l
    res[3] = 2 
    return res

        
