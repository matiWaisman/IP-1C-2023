-- Ejercicio 1

maximo :: Integer -> Integer -> Integer -> Integer
maximo a b c
  | a == calcularMaximo a b && a == calcularMaximo a c = a
  | b == calcularMaximo a b && b == calcularMaximo b c = b
  | c == calcularMaximo a c && c == calcularMaximo b c = c
  where
    calcularMaximo :: Integer -> Integer -> Integer
    calcularMaximo a b
      | a > b = a
      | a < b = b

minimo :: Integer -> Integer -> Integer -> Integer
minimo a b c
  | a == calcularMinimo a b && a == calcularMinimo a c = a
  | b == calcularMinimo a b && b == calcularMinimo b c = b
  | c == calcularMinimo a c && c == calcularMinimo b c = c
  where
    calcularMinimo :: Integer -> Integer -> Integer
    calcularMinimo a b
      | a < b = a
      | a > b = b

-- esPermutacion :: (Integer, Integer) -> () o a es menor o c mayor

-- medio :: Integer -> Integer -> Integer -> Integer
-- medio a b c
