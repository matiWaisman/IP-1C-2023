-- Ejercicio 1

fib :: Int -> Int 
fib n | n == 0 = 0
      | n == 1 = 1
      | otherwise = fib (n - 1) + fib (n - 2)

-- Ejercicio 2

parteEntera :: Float -> Int 
parteEntera x | 0 <= x && x < 1 = 0
              | otherwise = parteEntera(x - 1) + 1

-- Ejercicio 3

esDivisor :: Int -> Int -> Bool
esDivisor n d | n == 0 = True
              | n < 0 = False
              | otherwise = esDivisor (n - d) d

-- Ejercicio 4
sumaImpares :: Int -> Int 
sumaImpares n | n == 1 = 1
              | otherwise = sumaImpares(n-1) + nesimoImpar n

nesimoImpar :: Int -> Int
nesimoImpar n | n == 1 = 1 
              | otherwise = nesimoImpar(n-1) + 2

-- Ejercicio 7
--todosDigitosIguales :: Int -> Bool
--todosDigitosIguales n 
