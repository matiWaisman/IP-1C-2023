-- Ejercicio 1

fib :: Integer -> Integer
fib n
  | n == 0 = 0
  | n == 1 = 1
  | otherwise = fib (n - 1) + fib (n - 2)

-- Ejercicio 2

parteEntera :: Float -> Integer
parteEntera x
  | 0 <= x && x < 1 = 0
  | otherwise = parteEntera (x - 1) + 1

-- Ejercicio 3

esDivisor :: Integer -> Integer -> Bool
esDivisor n d
  | n == 0 = True
  | n < 0 = False
  | otherwise = esDivisor (n - d) d

-- Ejercicio 4

sumaImpares :: Integer -> Integer
sumaImpares n
  | n == 1 = 1
  | otherwise = sumaImpares (n - 1) + nesimoImpar n

nesimoImpar :: Integer -> Integer
nesimoImpar n
  | n == 1 = 1
  | otherwise = nesimoImpar (n - 1) + 2

-- Ejercicio 5

medioFact :: Integer -> Integer
medioFact n
  | n == 0 = 1
  | n == 1 = 1
  | n == 2 = 2
  | otherwise = n * medioFact (n - 2)

-- Ejercicio 6

sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = n `mod` 10 + sumaDigitos (n `div` 10)

-- Ejercicio 7

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
  | n < 10 = True
  | n `mod` 10 /= (n `div` 10) `mod` 10 = False
  | otherwise = todosDigitosIguales (n `div` 10)

-- Ejercicio 8

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito i n
  | cantidadDeDigitos n == i = n `mod` 10
  | otherwise = iesimoDigito i (n `div` 10)

cantidadDeDigitos :: Integer -> Integer
cantidadDeDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantidadDeDigitos (n `div` 10)

-- Ejercicio 9

-- esCapicua :: Integer -> Bool
-- esCapicua n

-- | n < 10 = True
-- | n `div` (10 ^ (cantidadDeDigitos n - 1)) /= n `mod` 10 = False
-- | otherwise = esCapicua

-- Ejercicio 10
-- Los que terminan en s son los ejercicios resueltos con forma de sumatoria y los que terminan en g son usando el termino general probado por induccion

f1s :: Integer -> Integer
f1s n
  | n == 0 = 2 ^ n
  | otherwise = f1s (n - 1) + 2 ^ n

f1g :: Integer -> Integer
f1g n = 2 ^ (n + 1) - 1

f2s :: Integer -> Integer -> Integer
f2s n q
  | n == 1 = q ^ n
  | otherwise = f2s (n - 1) q + q ^ n

f2g :: Integer -> Float -> Float
f2g n q
  | q == 1 || q == -1 = fromIntegral n + 1
  | otherwise = (q ^ (n + 1) - 1) / q - 1 -- Verificar

f3s :: Integer -> Float -> Float
f3s n q = sumatoria2n (2 * n) q
  where
    sumatoria2n :: Integer -> Float -> Float
    sumatoria2n dosN q
      | dosN == 1 = q
      | otherwise = f3s (dosN - 1) q + q ^ dosN

-- f3g :: Integer -> Float -> Float To do

f4s :: Integer -> Float -> Float
f4s n q = sumatoriaF4 n (2 * n) q
  where
    sumatoriaF4 :: Integer -> Integer -> Float -> Float
    sumatoriaF4 n dosN q
      | dosN == n = q ^ n
      | otherwise = sumatoriaF4 n (dosN - 1) q + q ^ dosN

f4g :: Integer -> Float -> Float
f4g n q
  | q == 1 = fromIntegral n - 1
  | otherwise = ((q ^ (2 * n + 1)) - q ^ n) / (q - 1)

-- Ejercicio 11 Falta verificar
-- Punto A

eAprox :: Integer -> Float
eAprox n
  | n == 0 = 1 / fromIntegral (factorial n)
  | otherwise = eAprox (n - 1) + 1 / fromIntegral (factorial n)

factorial :: Integer -> Integer
factorial n
  | n == 0 = 1
  | otherwise = factorial (n - 1) * n

-- Punto B

-- eAproxDiez :: Integer -> Float
-- eAproxDiez n

-- Ejercicio 12 Falta verificar

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n
  | n == 1 = 2
  | otherwise = 2 + (1 / raizDe2Aprox (n - 1))

-- Ejercicio 13

dobleSumatoria :: Integer -> Integer -> Integer
dobleSumatoria n m
  | n == 1 = segundaSumatoria 1 m
  | otherwise = dobleSumatoria (n - 1) m + segundaSumatoria n m

segundaSumatoria :: Integer -> Integer -> Integer
segundaSumatoria i m
  | m == 1 = i ^ m
  | otherwise = segundaSumatoria i (m - 1) + i ^ m

-- Ejercicio 14 Preguntar consigna

-- sumaPotencias :: Integer ->Integer ->Integer ->Integer
-- sumaPotencias q n m

-- Ejercicio 15

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m
  | n == 1 = sumaIntegererna 1 m
  | otherwise = sumaRacionales (n - 1) m + sumaIntegererna n m

sumaIntegererna :: Integer -> Integer -> Float
sumaIntegererna p m
  | m == 1 = fromIntegral p / fromIntegral m
  | otherwise = sumaIntegererna p (m - 1) + fromIntegral p / fromIntegral m

-- Ejercicio 16

menorDivisor :: Integer -> Integer
menorDivisor n = encontrarMenorDivisor n 2

encontrarMenorDivisor :: Integer -> Integer -> Integer
encontrarMenorDivisor n i
  | n == 1 = 1
  | n /= i && n `mod` i == 0 = i
  | n == i = i
  | otherwise = encontrarMenorDivisor n (i + 1)

esPrimo :: Integer -> Bool
esPrimo n
  | encontrarMenorDivisor n 2 == n = True
  | otherwise = False

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n1 n2
  | encontrarMenorDivisorComun n1 n2 2 == 1 = True
  | otherwise = False

encontrarMenorDivisorComun :: Integer -> Integer -> Integer -> Integer
encontrarMenorDivisorComun n1 n2 i
  | i > n1 || i > n2 = 1
  | n1 `mod` i == 0 && n2 `mod` i == 0 = i
  | otherwise = encontrarMenorDivisorComun n1 n2 (i + 1)

-- nEsimoPrimo :: Integer -> Integer To Do
-- nesimoPrimo n

-- Ejercicio 17 Preguntar, idea: Hacer una funcion recursiva que me vaya dando el numero de fibo metiendole un iterador. Si me da igual devuelvo true, si el numero de fibonacci se hace 50 unidades mas grande corto el loop para que no sea infinito

esFibonacci :: Integer -> Bool
esFibonacci n = iterarFibo n 0
  where
    iterarFibo :: Integer -> Integer -> Bool
    iterarFibo n i
      | fib i == n = True
      | n - fib i < -100 = False -- Esto lo hago para cortar el loop, si por ejemplo me dan 500 i i = 14 -> Fib 14 = 377 = 15 -> Fib 15 = 610 500 - 610 = 100, corto
      | otherwise = iterarFibo n (i + 1)

-- Ejercicio 18

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = encontrarDigitoMayorPar n (-1)
  where
    encontrarDigitoMayorPar :: Integer -> Integer -> Integer
    encontrarDigitoMayorPar n a
      | (n >= 10) && (n `mod` 10 >= a) && (n `mod` 10) `mod` 2 == 0 = encontrarDigitoMayorPar (n `div` 10) (n `mod` 10)
      | n < 10 && (n `mod` 10) `mod` 2 == 0 && n `mod` 10 > a = n `mod` 10 -- Evaluo el ultimo caso para cortar la recursion
      | n < 10 && ((n `mod` 10) `mod` 2 /= 0 || n `mod` 10 <= a) = a -- Evaluo el ultimo caso para cortar la recursion
      | otherwise = encontrarDigitoMayorPar (n `div` 10) a

-- Ejercicio 19 Preguntar como generar los primos con el ejercicio 16 D

-- esSumaInicialDePrimos :: Integer ->Bool
-- esSumaInicialDePrimos n

-- Ejercicio 20 Preguntar

-- tomaValorMax :: Integer -> Integer -> Integer
-- tomaValorMax n1 n2

-- Ejercicio 21 Preguntar

-- pitagoras :: Integer -> Integer -> Integer -> Integer
-- pitagoras m n r
