import Test.QuickCheck

-- functie ajutatoare o folosesc la toate f2cn si f3cn
-- daca string e empty da false altfel verific daca incepe cu litera mare
f0cn :: [Char] -> Bool
f0cn str
  | str == "" = False
  | otherwise = head str `elem` ['A' .. 'Z']

--1. recursivitate
f1cn :: [[Char]] -> Bool
f1cn [] = False
f1cn (h : t)
  | h == "" = False || f1cn t
  | head h `elem` ['A' .. 'Z'] = True || f1cn t
  | otherwise = False || f1cn t

-- True daca sirul meu incepe cu litera mare, false daca incepe cu litera mica
-- daca dau sau intre ele => cand am cel putin 1 sir cu litera mare voi primi true

--2. list comprehension
f2cn :: [[Char]] -> Bool
f2cn lst = if length ([x | x <- lst, f0cn x]) >= 1 then True else False

-- aleg doar sirurile care incep cu litera mare, daca am cel putin unul atunci e True altfel false

-- 3. fct nivel inalt
f3cn :: [[Char]] -> Bool
f3cn lst = if length (filter (\x -> f0cn x) lst) >= 1 then True else False

-- folosesc Filter pentru a filtra sirurile care incep cu litera mare si daca am cel putin unul atunci e True

--4. quickCheck
f4cn :: [[Char]] -> Bool
f4cn lst = (f1cn lst) == (f3cn lst)

--3.
f5cn :: [Int] -> [Int]
f5cn lst = foldr op unit lst
  where
    unit = []
    a `op` acc
      | a < 10 = 0 : acc
      | length acc > 0 = (head acc + 1) : (tail acc)
      | otherwise = acc

f6cn :: [Int] -> [Int]
f6cn [] = []
f6cn lst = tail (f5cn lst)

-- fac foldr iar acumulatorul meu este lista unde vor fi lungimile secventelor
-- de fiecare data cand gasesc o cifra noua creez o suma noua
-- numerele care vin dupa cifra le adun in suma curenta
-- cand gasesc iar cifra => s-a terminat secventa, incep alta secventa
-- tailul ala e pt a mi scoate prima suma (care ori e o suma de 0 (daca sirul incepe cu cifra), ori e o suma neterminata (nu am gasit cifra la inceput) deci nu ma intereseaza)
-- edge case : lista goala, o scot tot goala

--teste:
-- [1,10,11,2,30,4,19,19] -> [2,1]
-- [1,10,11,2,30,4,19,19,2] -> [2,1,2]
-- [10,11,2,30,4,19,19,2] -> [1,2]
-- [10,11,2,30,4,19,19] -> [1]