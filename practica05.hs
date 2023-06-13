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

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x : xs)
  | x == e = quitarTodos e xs
  | otherwise = x : quitarTodos e xs


eliminarRepetidos:: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)
  | pertenece x xs = eliminarRepetidos xs
  | otherwise = x: eliminarRepetidos xs


mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [x] y = True
mismosElementos (x : xs) y
  | not (pertenece x y) = False
  | otherwise = mismosElementos xs y

capicua :: (Eq t) => [t] -> Bool
capicua l
  | l == reverso l = True
  | otherwise = False

-- Ejercicio 3

sumatoria :: [Integer] -> Integer
sumatoria [x] = x
sumatoria (x : xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x : xs) = x * productoria xs

maximo :: [Integer] -> Integer
maximo (x : xs) = calcularMaximo x xs
  where
    calcularMaximo :: Integer -> [Integer] -> Integer
    calcularMaximo max (x : xs)
      | null xs && max > x = max
      | null xs && max < x = x
      | max < x = calcularMaximo x xs
      | otherwise = calcularMaximo max xs

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n = map (+ n)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x : xs) = x + x : sumarN x xs

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x : xs) = x + conseguirElUltimo (x : xs) : sumarElUltimo xs -- : sumarN conseguirElUltimo (x : xs) xs tambien deberia funcionar
  where
    conseguirElUltimo :: [Integer] -> Integer
    conseguirElUltimo [x] = x -- Podria usar last pero lo hago por el amor al arte!!!
    conseguirElUltimo (x : xs) = conseguirElUltimo xs

pares :: [Integer] -> [Integer]
pares [] = []
pares (x : xs)
  | even x = x : pares xs
  | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x : xs)
  | x `mod` n == 0 = x : multiplosDeN n xs
  | otherwise = multiplosDeN n xs

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x : y : xs)
  | x > y = y : x : ordenar xs
  | otherwise = ordenar (y : xs)

-- Ejercicio 4

sacarBlancosRepetidos :: String -> String
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x : y : xs)
  | x == ' ' && y == ' ' = y : sacarBlancosRepetidos xs
  | otherwise = x : y : sacarBlancosRepetidos xs

palabraMasLarga :: [Char] -> String
palabraMasLarga x = palabras x !! fromIntegral (posNumeroMasGrande (contarPalabras x) 0 0)

posNumeroMasGrande :: [Integer] -> Integer -> Integer -> Integer
posNumeroMasGrande [x] i max = max
posNumeroMasGrande (x : y : xs) i max
  | x >= y = posNumeroMasGrande (x : xs) (i + 1) max
  | x < y = posNumeroMasGrande (y : xs) (i + 1) (i + 1)

contarPalabras :: [Char] -> [Integer]
contarPalabras [] = []
contarPalabras x = contarHastaEspacio x : contarPalabras (drop (fromIntegral (contarHastaEspacio x + 1)) x)

contarHastaEspacio :: [Char] -> Integer
contarHastaEspacio [] = 0
contarHastaEspacio [x] = 1
contarHastaEspacio (x : xs)
  | x == ' ' = 0
  | otherwise = contarHastaEspacio xs + 1

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras x = acumularHastaEspacio x : palabras (drop (fromIntegral (contarHastaEspacio x + 1)) x)

acumularHastaEspacio :: [Char] -> [Char]
acumularHastaEspacio [] = []
acumularHastaEspacio [x] = [x]
acumularHastaEspacio (x : xs)
  | x == ' ' = []
  | otherwise = x : acumularHastaEspacio xs

aplanar :: [String] -> String
aplanar [x] = x
aplanar (x : xs) = x ++ aplanar xs

aplanarConBlancos :: [String] -> String
aplanarConBlancos [x] = x
aplanarConBlancos (x : xs) = x ++ [' '] ++ aplanar xs

aplanarConNBlancos :: [String] -> Integer -> String
aplanarConNBlancos [x] n = x
aplanarConNBlancos (x : xs) n = x ++ generarNBlancos n ++ aplanarConNBlancos xs n
  where
    generarNBlancos :: Integer -> String
    generarNBlancos 1 = [' ']
    generarNBlancos n = ' ' : generarNBlancos (n - 1)

-- Ejercicio 5

nat2bin :: Integer -> [Integer]
nat2bin n
  | n < 2 = [1]
  | n == 0 = [0]
  | otherwise = nat2bin (n `div` 2) ++ [n `mod` 2]

bin2nat :: [Integer] -> Integer
bin2nat [x] = 1 * x
bin2nat (x : xs) = 2 ^ length xs * x + bin2nat xs

nat2hex :: Integer -> String -- Me devuelve un caracter unicode, ver como resolver
nat2hex n
  | n < 16 = [pasarNumeroAHexa n]
  | otherwise = nat2hex (n `div` 16) ++ [pasarNumeroAHexa (n `mod` 16)]
  where
    pasarNumeroAHexa :: Integer -> Char -- La idea es que el valor este si o si entre 0 y 16
    pasarNumeroAHexa n
      | n < 10 = toEnum (fromInteger n)
      | n == 10 = 'A'
      | n == 11 = 'B'
      | n == 12 = 'C'
      | n == 13 = 'D'
      | n == 14 = 'E'
      | n == 15 = 'F'

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x : y : xs) = x : sumaAcumulada (x + y : xs)

descomponerEnPrimos :: [Integer] -> [[Integer]] 
descomponerEnPrimos [] = []
descomponerEnPrimos [x] = [calcularDescomposicion x (x - 1)]
descomponerEnPrimos (x : xs) = calcularDescomposicion x (x - 1) : descomponerEnPrimos xs

calcularDescomposicion :: Integer -> Integer -> [Integer]
calcularDescomposicion n i
  | esPrimo n = [n]
  | i == 1 = []
  | i < n && (n `mod` i) == 0 = calcularDescomposicion n (i - 1) ++ [i]
  | otherwise = calcularDescomposicion n (i - 1)

esPrimo :: Integer -> Bool
esPrimo n
  | encontrarMenorDivisor n 2 == n = True
  | otherwise = False
  where
    encontrarMenorDivisor :: Integer -> Integer -> Integer
    encontrarMenorDivisor n i
      | n == 1 = 1
      | n /= i && n `mod` i == 0 = i
      | n == i = i
      | otherwise = encontrarMenorDivisor n (i + 1)

-- Ejercicio 6

type Set a = [a]

agregarATodos :: Integer -> Set (Set Integer) -> Set (Set Integer)
agregarATodos n [] = []
agregarATodos n (l : ls) = agregarA n l : (agregarATodos n ls)

agregarA :: Integer -> Set Integer -> Set Integer
agregarA n x
  | not (pertenece n x) = n : x
  | otherwise = x

partes :: Integer -> Set (Set Integer)
partes 0 = [[]]
partes x = agregarATodos x (partes (x - 1)) ++ partes (x - 1)

productoCartesiano :: Set Integer -> Set Integer -> Set (Integer, Integer)
productoCartesiano [] y = []
productoCartesiano [x] y = productoUnElemento x y
productoCartesiano (x : xs) y = productoUnElemento x y ++ productoCartesiano xs y

productoUnElemento :: Integer -> Set Integer -> Set (Integer, Integer)
productoUnElemento x [] = []
productoUnElemento x [y] = [(x, y)]
productoUnElemento x (y : ys) = (x, y) : productoUnElemento x ys

-- Ejercicio dado de ejemplo como ejercicio de parcial

eliminarYContarRepetidos :: [Integer] -> ([Integer], [(Integer, Integer)])
eliminarYContarRepetidos l = (eliminarRepetidos l, contarRepetidos l)

contarRepetidos :: [Integer] -> [(Integer, Integer)]
contarRepetidos l = contarCuantosRepetidosHay (eliminarRepetidos l) l

contarCuantosRepetidosHay :: [Integer] -> [Integer] -> [(Integer, Integer)]
contarCuantosRepetidosHay [] _ = []
contarCuantosRepetidosHay (x:xs) listaOriginal = (x, (cantidadApariciones x listaOriginal) - 1) : contarCuantosRepetidosHay xs listaOriginal

cantidadApariciones :: (Eq t) => t -> [t] -> Integer
cantidadApariciones _ [] = 0
cantidadApariciones e (x:xs)
  | e == x = 1 + cantidadApariciones e xs
  | otherwise = cantidadApariciones e xs
