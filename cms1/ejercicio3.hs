prod :: Integer -> Integer
prod n = calcularProductoria (2 * n)
  where
    calcularProductoria :: Integer -> Integer
    calcularProductoria dosN
      | dosN == 1 = (dosN ^ 2) + (2 * dosN)
      | otherwise = calcularProductoria (dosN - 1) * (dosN ^ 2 + 2 * dosN)