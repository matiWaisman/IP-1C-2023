from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  res: int = 1 
  destino_actual: str = hay_partida(destino, vuelos)
  while(destino_actual != "" and destino_actual != origen):
    res += 1
    destino_actual = hay_partida(destino_actual, vuelos)
  if(destino_actual == ""): res = -1
  return res

def hay_partida(destino: str, vuelos: List[Tuple[str, str]]) -> str: #Devuelve vacio si no hay, devuelve una ciudad que tiene un vuelo hacia el destino deseado
  res: str = ""
  sigo: bool = True
  i: int = 0
  while i < len(vuelos) and sigo:
    if vuelos[i][1] == destino:
      res = vuelos[i][0]
      sigo = False
    i += 1
  return res

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))
