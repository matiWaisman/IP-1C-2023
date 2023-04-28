main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax t = maximo t > (minimo t + medio t)

maximo :: (Int, Int, Int) -> Int
maximo (a, b, c)
  | a >= b && a >= c = a
  | b >= a && b >= c = b
  | c >= b && c >= a = c

minimo :: (Int, Int, Int) -> Int
minimo (a, b, c)
  | a <= b && a <= c = a
  | b <= a && b <= c = b
  | c <= b && c <= a = c

medio :: (Int, Int, Int) -> Int
medio (a, b, c)
  | (a <= b && b <= c) || (c <= b && b <= a) = b
  | (b <= a && a <= c) || (c <= a && a <= c) = a
  | otherwise = c
