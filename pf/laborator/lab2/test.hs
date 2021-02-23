--recursie
import Data.Char

inInterval x y [] = []
inInterval x y (h : t) =
  if (x <= h && h <= y)
    then h : inInterval x y t
    else inInterval x y t

--list comprehension

inInterval2 x y [] = []
inInterval2 a b l = [x | x <- l, a <= x, x <= b]

-- recursie
pozitive [] = 0
pozitive (h : t) =
  if h > 0
    then 1 + pozitive t
    else pozitive t

-- cu guard
pozitive2 [] = 0
pozitive2 (h : t)
  | h > 0 = 1 + pozitive2 t
  | otherwise = pozitive2 t

-- list compr
pozitive3 l = sum ([1 | x <- l, x > 0])

--recursie
multDigits [] = 0
multDigits (h : t)
  | isDigit h = digitToInt h + multDigits t
  | otherwise = 0 + multDigits t

-- simulare
--1
f ch
  | ch_i >= 97 && ch_i <= 109 = True
  | ch_i >= 110 && ch_i <= 122 = False
  | ch_i >= 65 && ch_i <= 77 = True
  | ch_i >= 78 && ch_i <= 90 = False
  | otherwise = error "no"
  where
    ch_i = ord ch

--2 list comprehension
g :: String -> Bool
g "" = False
g list
  | firstHalfCount > secondHalfCount = True
  | otherwise = False
  where
    firstHalfCount = sum ([1 | x <- list, f x])
    secondHalfCount = sum ([1 | x <- list, not (f x)])

--3 recursion
g2 [] = 0
g2 (h : t)
  | f h = 1 + g2 t
  | otherwise = -1 + g2 t

g2' list
  | g2 list > 0 = True
  | otherwise = False

-- 4 list comprehension
c list = [p | p <- zip list (tail list), fst (p) == snd (p)]

-- 5
