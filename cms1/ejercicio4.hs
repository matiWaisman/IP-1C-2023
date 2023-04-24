main :: IO ()
main = do
  x <- readLn
  print (sumaPrimerosNImpares (x :: (Integer)))

sumaPrimerosNImpares :: Integer -> Integer
sumaPrimerosNImpares n = calcularSumatoriaNImpares (2 * n)
  where
    calcularSumatoriaNImpares :: Integer -> Integer
    calcularSumatoriaNImpares i
      | i == 1 = 2 * i + 2
      | i `mod` 2 /= 0 = calcularSumatoriaNImpares (i - 1) + (2 * i + 2)
      | otherwise = calcularSumatoriaNImpares (i - 1)