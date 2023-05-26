import sys
from typing import List

def fibonacciNoRecursivo(n: int) -> int:
  res: int = 0
  if n == 0 or n == 1: return 1
  ultimos: List[int] = [1,1]
  for i in range(2, n + 1, 1):
    res =  ultimos[0] + ultimos[1]
    ultimos[0] = ultimos[1]
    ultimos[1] = res
  return res

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))
