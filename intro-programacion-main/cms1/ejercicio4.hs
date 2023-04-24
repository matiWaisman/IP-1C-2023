sumaPrimerosNImparesEspecial :: Integer -> Integer
sumaPrimerosNImparesEspecial n = calcularSumatoriaNImpares (2 * n)
  where
    calcularSumatoriaNImpares :: Integer -> Integer
    calcularSumatoriaNImpares i
      | i == 1 = 2 * i + 2
      | i `mod` 2 /= 0 = calcularSumatoriaNImpares (i - 1) + (2 * i + 2)
      | otherwise = calcularSumatoriaNImpares (i - 1)