from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int : 
  acumulador_actual: int = 1 
  lista_acumuladores: List[int] = []
  for i in range(0, len(l), 1):
    if(i != len(l) - 1):
      if(l[i] == l[i+1]):
        acumulador_actual += 1
      if(l[i] != l[i+1]): 
        lista_acumuladores.append(acumulador_actual)
        acumulador_actual = 1
    else: lista_acumuladores.append(acumulador_actual)
  res: int = acumulador_mas_grande(lista_acumuladores)
  return res

def acumulador_mas_grande(l: List[int]) -> int: 
  res: int = 0
  for i in range(0,len(l), 1): 
    if(l[i] > res): res = l[i]
  return res   

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))