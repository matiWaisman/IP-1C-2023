-- Ejercicio 1 

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = longitud (xs) + 1 

ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo xs

principio :: [t] -> [t]
principio (x:xs) = [x]

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x] 

-- Ejercicio 2

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e l 
    | head l == e = True
    | otherwise = pertenece e (tail l)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) = True
todosIguales(x:y:xs)
    | x /= y = False
    | otherwise = todosIguales (y:xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:[]) = True
todosDistintos (x:xs) = verificarDistinto x xs
    where 
        verificarDistinto (Eq t) => t -> [t] -> Bool
        verificarDistinto (y:[]) = True
        verificarDistinto e (y:ys) 
            | y == e False
            | otherwise = verificarDistinto e xs
            




