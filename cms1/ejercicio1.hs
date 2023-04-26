main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Integer, Integer, Integer)))

sumaMenosQueMax :: (Integer, Integer, Integer) -> Bool
sumaMenosQueMax (t0, t1, t2)
  | maximo t0 t1 t2 > (minimo t0 t1 t2 + medio t0 t1 t2) = True
  | otherwise = False

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

medio :: Integer -> Integer -> Integer -> Integer
medio a b c
  | (a <= b && b <= c) || (c <= b && b <= a) = b
  | (b <= a && a <= c) || (c <= a && a <= c) = a
  | otherwise = c
