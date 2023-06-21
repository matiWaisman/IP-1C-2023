from typing import List
from typing import Dict
import json


def unir_diccionarios(a_unir: List[Dict[str, str]]) -> Dict[str, List[str]]:
    res: Dict[str, List[str]] = {}
    lista_claves: List[str] = calcular_claves(a_unir)
    for i in range(0, len(a_unir), 1):
        for j in range(0, len(lista_claves), 1):
            clave_actual: str = lista_claves[j]
            if clave_actual in a_unir[i]:
                valor_actual: str = a_unir[i][clave_actual]
                if clave_actual in res:
                    res[clave_actual].append(valor_actual)
                else:
                    # Hay que iniciarlizarlo
                    res[clave_actual] = [valor_actual]
    return res


def calcular_claves(l: List[Dict[str, str]]) -> List[str]:
    res: List[str] = []
    for i in range(0, len(l), 1):
        claves = l[i].keys()
        lista_claves: List[str] = list(claves)
        for clave in lista_claves:
            if(pertenece(res, clave) == False):
                res.append(clave)
    return res


def pertenece(l: list([str]), e: str) -> bool:
    res: bool = False
    sigo: bool = True
    i: int = 0
    while (i < len(l) and sigo == True):
        if(l[i] == e):
            res = True
            sigo = False
        i += 1
    return res


if __name__ == '__main__':
    x = json.loads(input())  # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
    print(unir_diccionarios(x))
