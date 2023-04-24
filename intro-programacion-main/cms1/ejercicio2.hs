sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = n `mod` 10 + sumaDigitos (n `div` 10)