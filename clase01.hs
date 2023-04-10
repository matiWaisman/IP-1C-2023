doubleMe :: Int -> Int
doubleMe x = x + x  

--Ejercicio 1

--Punto A
f:: Int -> Int
f n | n == 1 = 8
    | n == 4 = 138
    | n == 16 = 16

--Punto B
g:: Int -> Int
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

--Punto C
h:: Int -> Int
h n = f (g n)

k:: Int -> Int
k n = g (f n)



--Punto 2

--Punto A

absoluto:: Int -> Int
absoluto n | n > 0 = n
           | n < 0 = n * (-1)

--Punto B

maximoAbsoluto:: Int -> Int -> Int
maximoAbsoluto x y | absoluto x > absoluto y = absoluto x
                   | absoluto x < absoluto y = absoluto y

--Punto C

maximo:: Int -> Int -> Int
maximo x y | x > y = x
           | x < y = y

maximo3:: Int -> Int -> Int -> Int
maximo3 x y z | x == maximo x y && x == maximo x z = x  
              | y == maximo x y && x == maximo y z = y
              | z == maximo x z && z == maximo y z = z 

--Punto D

--Usando Pattern Matching

algunoEs0P:: Float -> Float -> Bool
algunoEs0P _ 0 = True
algunoEs0P 0 _ = True
algunoEs0P _ _ = False


--Usando Guardas

algunoEs0G:: Float -> Float -> Bool
algunoEs0G x y | x == 0 || y == 0 = True
               | otherwise = False

-- Punto F

--mismoIntervalo:: Float -> Float -> Bool

