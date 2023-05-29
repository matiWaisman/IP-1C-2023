import sys

def fibonacciNoRecursivo(n: int) -> int:
  if (n == 0 or n == 1): return n
  res: int = 0
  ante_ultimo: int = 0 
  ultimo: int = 1 
  for i in range(2, n +1 , 1):
    res =  ante_ultimo + ultimo
    ante_ultimo = ultimo
    ultimo = res
  return res

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))
