import Data.List

-- L3.1 Încercati sa gasiti valoarea expresiilor de mai jos si
-- verificati raspunsul gasit de voi în interpretor:
{-
[x^2 | x <- [1 .. 10], x `rem` 3 == 2]
[(x, y) | x <- [1 .. 5], y <- [x .. (x+2)]]
[(x, y) | x <- [1 .. 3], let k = x^2, y <- [1 .. k]]
[x | x <- "Facultatea de Matematica si Informatica", elem x ['A' .. 'Z']]
[[x .. y] | x <- [1 .. 5], y <- [1 .. 5], x < y ]

-}

factori :: Int -> [Int]
factori x = [a | a <- [1 .. x], x `rem` a == 0]

prim :: Int -> Bool
prim x = length (factori x) == 2

numerePrime :: Int -> [Int]
numerePrime x = [n | n <- [2 .. x], prim n]

-- L3.2 Testati si sesizati diferenta:
-- [(x,y) | x <- [1..5], y <- [1..3]]
-- zip [1..5] [1..3]

myzip3 :: [Int] -> [Int] -> [Int] -> [(Int, Int, Int)]
myzip3 [] l1 l2 = []
myzip3 l1 [] l2 = []
myzip3 l1 l2 [] = []
myzip3 l1 l2 l3 = (head l1, head l2, head l3) : (myzip3 (tail l1) (tail l2) (tail l3))

--------------------------------------------------------
----------FUNCTII DE NIVEL INALT -----------------------
--------------------------------------------------------
aplica2 :: (a -> a) -> a -> a
--aplica2 f x = f (f x)
--aplica2 f = f.f
--aplica2 f = \x -> f (f x)
aplica2 = \f x -> f (f x)

-- L3.3
{-

map (\ x -> 2 * x) [1 .. 10]
map (1 `elem` ) [[2, 3], [1, 2]]
map ( `elem` [2, 3] ) [1, 3, 4, 5]

-}

-- firstEl [ ('a', 3), ('b', 2), ('c', 1)]

firstEl lst = map (fst) lst

-- sumList [[1, 3],[2, 4, 5], [], [1, 3, 5, 6]]

sumList lst = map sum lst

-- prel2 [2,4,5,6]

check n
  | even n = (n `div` 2)
  | otherwise = (n * 2)

prel2 lst = map check lst

f1 ch lst = filter (elem ch) lst

f2 lst = map (\x -> x ^ 2) (filter (odd) (lst))

get (index, nr)
  | odd index = True
  | otherwise = False

f3 lst = map (\(a, b) -> b ^ 2) (filter get (zip [0 .. length lst] lst))

vocala ch
  | elem ch ['a', 'e', 'i', 'o', 'u'] = True
  | otherwise = False

f4 word = filter vocala word

f4' lst = map (\x -> filter vocala x) lst

semn [] = ""
semn (h : t)
  | h > 0 && h <= 9 = '+' : (semn t)
  | h == 0 = '0' : (semn t)
  | h < 0 && (h >= (-9)) = '-' : (semn t)
  | otherwise = (semn t)

