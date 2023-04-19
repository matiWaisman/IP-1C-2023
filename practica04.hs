-- Ejercicio 1

fib :: Int -> Int
fib n
  | n == 0 = 0
  | n == 1 = 1
  | otherwise = fib (n - 1) + fib (n - 2)

-- Ejercicio 2

parteEntera :: Float -> Int
parteEntera x
  | 0 <= x && x < 1 = 0
  | otherwise = parteEntera (x - 1) + 1

-- Ejercicio 3

esDivisor :: Int -> Int -> Bool
esDivisor n d
  | n == 0 = True
  | n < 0 = False
  | otherwise = esDivisor (n - d) d

-- Ejercicio 4

sumaImpares :: Int -> Int
sumaImpares n
  | n == 1 = 1
  | otherwise = sumaImpares (n - 1) + nesimoImpar n

nesimoImpar :: Int -> Int
nesimoImpar n
  | n == 1 = 1
  | otherwise = nesimoImpar (n - 1) + 2

-- Ejercicio 5

medioFact :: Int -> Int
medioFact n
  | n == 0 = 1
  | n == 1 = 1
  | n == 2 = 2
  | otherwise = n * medioFact (n - 2)

-- Ejercicio 6

sumaDigitos :: Int -> Int
sumaDigitos n
  | n < 10 = n
  | otherwise = n `mod` 10 + sumaDigitos (n `div` 10)

-- Ejercicio 7

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n
  | n < 10 = True
  | n `mod` 10 /= (n `div` 10) `mod` 10 = False
  | otherwise = todosDigitosIguales (n `div` 10)

-- Ejercicio 8

iesimoDigito :: Int -> Int -> Int
iesimoDigito i n
  | cantidadDeDigitos n == i = n `mod` 10
  | otherwise = iesimoDigito i (n `div` 10)

cantidadDeDigitos :: Int -> Int
cantidadDeDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantidadDeDigitos (n `div` 10)

-- Ejercicio 9

-- esCapicua :: Int -> Bool
-- esCapicua n
--  | n < 10 = True
--  | n `div` (10 ^ (cantidadDeDigitos n - 1)) /= n `mod` 10 = False
--  | otherwise = esCapicua como hago para volver a llamar a la funcion pero sacandome el primero y el ultimo sin pasarlo a strings

-- Ejercicio 10
-- Los que terminan en s son los ejercicios resueltos con forma de sumatoria y los que terminan en g son usando el termino general probado por induccion

f1s :: Int -> Int
f1s n
  | n == 0 = 2 ^ n
  | otherwise = f1s (n - 1) + 2 ^ n

f1g :: Int -> Int
f1g n = 2 ^ (n + 1) - 1

f2s :: Int -> Int -> Int
f2s n q
  | n == 1 = q ^ n
  | otherwise = f2s (n - 1) q + q ^ n

f2g :: Int -> Float -> Float
f2g n q
  | q == 1 || q == -1 = fromIntegral n + 1 -- Como sacar el fromIntegral
  | otherwise = (q ^ (n + 1) - 1) / q - 1 -- Verificar

f3s :: Int -> Float -> Float
f3s n q
  | n == 1 = q
  | otherwise = f3s ((2 * n) - 1) q + q ^ n -- Como resolver sin necesidad de pasarle un parametro extra (2n)

-- f3g :: Int -> Float -> Float To do
-- f3g n q

-- f4s :: Int -> Float -> Float To do
-- f4s n q

f4g :: Int -> Float -> Float
f4g n q
  | q == 1 = fromIntegral n - 1
  | otherwise = ((q ^ (2 * n + 1)) - q ^ n) / (q - 1)

-- Ejercicio 11 Falta verificar
-- Punto A

eAprox :: Int -> Float
eAprox n
  | n == 0 = 1 / fromIntegral (factorial n)
  | otherwise = eAprox (n - 1) + 1 / fromIntegral (factorial n)

factorial :: Int -> Int
factorial n
  | n == 0 = 1
  | otherwise = factorial (n - 1) * n

-- Punto B

-- eAproxDiez :: Int -> Float
-- eAproxDiez n

-- Ejercicio 12 Preguntar consigna

raizDe2Aprox :: Int -> Float
raizDe2Aprox n
  | n == 1 = 2
  | otherwise = 2 + (1 / raizDe2Aprox (n - 1))

-- Ejercicio 13

dobleSumatoria :: Int -> Int -> Int
dobleSumatoria n m
  | n == 1 = segundaSumatoria 1 m
  | otherwise = dobleSumatoria (n - 1) m + segundaSumatoria n m

segundaSumatoria :: Int -> Int -> Int
segundaSumatoria i m
  | m == 1 = i ^ m
  | otherwise = segundaSumatoria i (m - 1) + i ^ m

-- Ejercicio 14 Preguntar consigna

-- sumaPotencias :: Int ->Int ->Int ->Int
-- sumaPotencias q n m

-- Ejercicio 15 To finish

sumaRacionales :: Int -> Int -> Float
sumaRacionales n m
  | n == 1 = sumaInterna 1 m
  | otherwise = sumaRacionales (n - 1) m + sumaInterna n m

sumaInterna :: Int -> Int -> Float
sumaInterna p m
  | p == 1 = fromIntegral p / fromIntegral m
  | otherwise = sumaInterna p (m - 1) + fromIntegral p / fromIntegral m
