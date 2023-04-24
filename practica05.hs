-- Ejercicio 1

longitud :: [t] -> Integer
longitud [] = 0
longitud (x : xs) = longitud xs + 1

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

principio :: [t] -> [t]
principio (x : xs) = [x]

reverso :: [t] -> [t]
reverso [] = []
reverso (x : xs) = reverso xs ++ [x]

-- Ejercicio 2

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e l
  | head l == e = True
  | otherwise = pertenece e (tail l)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x : y : xs)
  | x /= y = False
  | otherwise = todosIguales (y : xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x : xs) = verificarDistinto x xs
  where
    verificarDistinto :: (Eq t) => t -> [t] -> Bool
    verificarDistinto _ [] = True
    verificarDistinto e (y : ys)
      | y == e = False
      | otherwise = verificarDistinto e ys

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x : xs) = verificarRepetidos x xs
  where
    verificarRepetidos :: (Eq t) => t -> [t] -> Bool
    verificarRepetidos _ [] = False
    verificarRepetidos e (y : ys)
      | y == e = True
      | otherwise = verificarRepetidos e ys

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (y : ys)
  | y == e = ys
  | otherwise = y : quitar e ys

-- quitarTodos :: (Eq t ) => t -> [t] -> [t]
-- quitarTodos _[] = []
-- quitarTodos e l
--    | y == e = quitar e
--    | otherwise =

-- eliminarRepetidos :: (Eq t) => [t] -> [t]
-- eliminarRepetidos

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x : xs) y
  | null xs = True -- Como cambiar esto para que quede mas elegante
  | pertenece x y == False = False
  | otherwise = mismosElementos xs y

capicua :: (Eq t) => [t] -> Bool
capicua l
  | l == reverso l = True
  | otherwise = False

-- Ejercicio 3

sumatoria :: [Integer] -> Integer
sumatoria (x : xs)
  | null xs = x
  | otherwise = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria (x : xs)
  | null xs = x
  | otherwise = x * productoria xs

-- maximo :: [Integer] -> Integer
-- maximo (x : xs)

-- sumarN :: Integer -> [Integer] -> [Integer]
-- sumarN n (x : xs)
--  | null xs = x + n