main :: IO ()
main = do
  x <- readLn
  print (sumaDigitos (x :: (Int)))

sumaDigitos :: Int -> Int
sumaDigitos n
  | n < 10 = n
  | otherwise = n `mod` 10 + sumaDigitos (n `div` 10)
