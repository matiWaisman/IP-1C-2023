-- Ejercicio 3, preguntar, al ingresarle 2 devuelve 48 cuando deveria devolver 8640

prod :: Integer -> Integer
prod n = calcularProductoria 2 * n
  where
    calcularProductoria :: Integer -> Integer
    calcularProductoria dosN
      | dosN == 1 = dosN ^ 2 + 2 * dosN
      | otherwise = calcularProductoria (dosN - 1) * (dosN ^ 2 + 2 * dosN)