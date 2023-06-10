import Distribution.Simple.Setup (trueArg)

doubleMe :: Integer -> Integer
doubleMe x = x + x

-- Ejercicio 1

-- Punto A
f :: Integer -> Integer
f n
  | n == 1 = 8
  | n == 4 = 138
  | n == 16 = 16

-- Punto B
g :: Integer -> Integer
g n
  | n == 8 = 16
  | n == 16 = 4
  | n == 131 = 1

-- Punto C
h :: Integer -> Integer
h n = f (g n)

k :: Integer -> Integer
k n = g (f n)

-- Punto 2

-- Punto A

absoluto :: Integer -> Integer
absoluto n
  | n > 0 = n
  | n < 0 = n * (-1)

-- Punto B

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y
  | absoluto x > absoluto y = absoluto x
  | absoluto x < absoluto y = absoluto y

-- Punto C

maximo :: Integer -> Integer -> Integer
maximo x y
  | x > y = x
  | x < y = y

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z
  | x == maximo x y && x == maximo x z = x
  | y == maximo x y && x == maximo y z = y
  | z == maximo x z && z == maximo y z = z

-- Punto D

-- Usando Pattern Matching

algunoEs0P :: Float -> Float -> Bool
algunoEs0P _ 0 = True
algunoEs0P 0 _ = True
algunoEs0P _ _ = False

-- Usando Guardas

algunoEs0G :: Float -> Float -> Bool
algunoEs0G x y
  | x == 0 || y == 0 = True
  | otherwise = False

-- Punto E

-- Usando Guardas

ambosSon0G :: Float -> Float -> Bool
ambosSon0G x y
  | x == 0 && y == 0 = True
  | otherwise = False

-- Usando Pattern Matching
ambosSon0P :: Float -> Float -> Bool
ambosSon0P 0 0 = True 
ambosSon0P _ _ = False

-- Punto F

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y
  | x <= 3 && y <= 3 = True
  | (x > 3 && x <= 7) && (y > 3 && x <= 7) = True
  | x > 7 && y > 7 = True
  | otherwise = False

-- Punto G

sumaDistIntegeros :: Integer -> Integer -> Integer -> Integer
sumaDistIntegeros x y z
  | x == y && y == z = x
  | x == y && x /= z = x + z
  | x /= y && x == z = x + y
  | y /= z && x == y = y + z
  | otherwise = x + y + z

-- Punto H

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y
  | mod x y == 0 = True
  | otherwise = False

-- Punto I

digitoUnidades :: Integer -> Integer
digitoUnidades x = x `mod` 10

-- Punto J

digitoDecenas :: Integer -> Integer
digitoDecenas x = (x `div` 10) `mod` 10

-- Ejercicio 3

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b
  | a == 0 && b == 0 = False
  | a * a + a * b * k == 0 = True
  | otherwise = False
  where
    k = div (a * a) ((-a) * b)

-- Ejercicio 4

-- Punto A

prodInteger :: (Integer, Integer) -> (Integer, Integer) -> Integer
prodInteger (x1, y1) (x2, y2) = x1 * x1 + y1 * y2

-- Punto B

todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor (x1, y1) (x2, y2)
  | x1 < x2 && y1 < y2 = True
  | otherwise = False

-- Punto C

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, y1) (x2, y2) = sqrt ((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

-- Punto D

sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x1, x2, x3) = x1 + x2 + x3

-- Punto F

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x1, x2, x3) n
  | n < 0 = 0
  | n > 0 = determinarMultiplo x1 n + determinarMultiplo x2 n + determinarMultiplo x3 n

determinarMultiplo :: Integer -> Integer -> Integer
determinarMultiplo x n
  | mod x n == 0 = x
  | mod x n /= 0 = 0

-- Punto F

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x1, x2, x3)
  | esMultiploDe x1 2 = 0
  | esMultiploDe x2 2 = 1
  | esMultiploDe x3 2 = 3
  | otherwise = 4

-- Punto G

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

-- Punto H

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- Ejercicio 5

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3)
  | f n1 > g n1 && f n2 > g n2 && f n3 > g n3 = True
  | otherwise = False

f5 :: Integer -> Integer
f5 n
  | n <= 7 = n ^ 2
  | otherwise = 2 * n - 1

g5 :: Integer -> Integer
g5 n
  | esMultiploDe n 2 = n `div` 2
  | otherwise = 3 * n + 1

-- Ejercicio 6

bisiesto :: Integer -> Bool
bisiesto y
  | not (esMultiploDe y 4) || (esMultiploDe y 100 && not (esMultiploDe y 400)) = False
  | otherwise = True

-- Ejercicio 7

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1, p2, p3) (q1, q2, q3) = abs (p1 - q1) + abs (p2 - q2) + abs (p3 - q3)

-- Ejercicio 8

comparar :: Integer -> Integer -> Integer
comparar a b
  | sumaUltimoDosDigitos a < sumaUltimoDosDigitos b = 1
  | sumaUltimoDosDigitos a > sumaUltimoDosDigitos b = -1
  | sumaUltimoDosDigitos a == sumaUltimoDosDigitos b = 0

sumaUltimoDosDigitos :: Integer -> Integer
sumaUltimoDosDigitos x = digitoUnidades x + digitoDecenas x