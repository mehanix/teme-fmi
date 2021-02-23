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