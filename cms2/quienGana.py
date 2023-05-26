import sys

def quienGana(j1: str, j2: str) -> str : 
    res: str = ""
    jugada_ganadora: str = calcular_ganador(j1,j2)
    if(j1 == jugada_ganadora): res = "Jugador1"
    if(j2 == jugada_ganadora): res = "Jugador2"
    if(j1 == j2): res = "Empate"
    return res

def calcular_ganador(j1: str, j2: str) -> str: 
   res: str = ""
   if((j1 == "Piedra" and j2 == "Papel") or (j1 == "Papel" and j2 == "Tijera") or (j1 == "Tijera" and j2 == "Piedra")):
      res = j2  
   else: res = j1  
   return res 

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))

