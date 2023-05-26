import sys

def fibonacciNoRecursivo(n: int) -> int:
  res: int = 0
  if n == 0 or n == 1: return 1
  ante_ultimo: int = 1 
  ultimo: int = 1
  for i in range(2, n, 1):
    res =  ante_ultimo + ultimo
    ante_ultimo = ultimo
    ultimo = res
  return res


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))
