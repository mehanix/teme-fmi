import Numeric.Natural

produsRec :: [Integer] -> Integer
produsRec = undefined

produsFold :: [Integer] -> Integer
produsFold lst = foldr (*) 1 lst

andRec :: [Bool] -> Bool
andRec [] = True
andRec (h : t)
  | h == True = True && andRec t
  | otherwise = False

andFold :: [Bool] -> Bool
andFold lst = foldr (&&) True lst

concatRec :: [[a]] -> [a]
concatRec [] = []
concatRec (h : t) = h ++ concatRec t

concatFold :: [[a]] -> [a]
concatFold lst = foldr (++) [] lst

isNotCh ch x = not (ch == x)

rmCharsRec :: String -> String -> String
rmCharsRec [] lst = lst
rmCharsRec lst [] = []
rmCharsRec (h : t) lst
  | h `elem` lst = rmCharsRec (t) (rmChar h lst)
  | otherwise = rmCharsRec t lst

test_rmchars :: Bool
test_rmchars = rmCharsRec ['a' .. 'l'] "fotbal" == "ot"

f lst x
  | x `elem` lst = ""
  | otherwise = x

rmChar :: Char -> String -> String
rmChar ch str = filter (isNotCh ch) str

rmCharsFold :: String -> String -> String
rmCharsFold lst1 lst2 = foldr rmChar lst2 lst1

logistic :: Num a => a -> a -> Natural -> a
logistic rate start = f
  where
    f 0 = start
    f n = rate * f (n - 1) * (1 - f (n - 1))

logistic0 :: Fractional a => Natural -> a
logistic0 = logistic 3.741 0.00079

ex1 :: Natural
ex1 = undefined

ex20 :: Fractional a => [a]
ex20 = [1, logistic0 ex1, 3]

ex21 :: Fractional a => a
ex21 = head ex20

ex22 :: Fractional a => a
ex22 = ex20 !! 2

ex23 :: Fractional a => [a]
ex23 = drop 2 ex20

ex24 :: Fractional a => [a]
ex24 = tail ex20

ex31 :: Natural -> Bool
ex31 x = x < 7 || logistic0 (ex1 + x) > 2

ex32 :: Natural -> Bool
ex32 x = logistic0 (ex1 + x) > 2 || x < 7

ex33 :: Bool
ex33 = ex31 5

ex34 :: Bool
ex34 = ex31 7

ex35 :: Bool
ex35 = ex32 5

ex36 :: Bool
ex36 = ex32 7

semnFold lst = foldr op unit lst
  where
    unit = ""
    h `op` s
      | h > 0 && h <= 9 = '+' : s
      | h == 0 = '0' : s
      | h < 0 && (h >= (-9)) = '-' : s
      | otherwise = s

--corect :: [[a]] -> Bool
corect mat = and (map (\x -> (length x) == t) mat)
  where
    t = length (head mat)

coolList len = [a | a <- [1 .. len], b <- [1 .. len]]

transforma mat = zip3 [col | line <- mat, col <- line] (coolList (length mat)) (cycle [1 .. (length (head mat))])