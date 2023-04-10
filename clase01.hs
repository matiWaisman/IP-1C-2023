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

maximo3:: Int -> Int -> Int -> Int
maximo3 x y z | absoluto x == maximoAbsoluto x y && absoluto x == maximoAbsoluto x z = absoluto x  
                | absoluto y == maximoAbsoluto x y && absoluto x == maximoAbsoluto y z = absoluto y
                | absoluto z == maximoAbsoluto x z && absoluto z == maximoAbsoluto y z = absoluto z 