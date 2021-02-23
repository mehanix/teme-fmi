import Data.Char

semiPare [] = []
semiPare (h : t)
  | even h = (h `div` 2) : (semiPare t)
  | otherwise = semiPare t

semiPareComp [] = []
semiPareComp lst = [x `div` 2 | x <- lst, even x]

intervalRec a b [] = []
intervalRec a b (h : t)
  | (a <= h) && (h <= b) = h : (intervalRec a b t)
  | otherwise = intervalRec a b t

intervalRec' a b [] = []
intervalRec' a b (h : t) =
  if (a <= h) && (h <= b)
    then h : (intervalRec a b t)
    else intervalRec a b t

intervalComp a b [] = []
intervalComp a b lst = [h | h <- lst, (a <= h) && (h <= b)]

pozitive [] = 0
pozitive (h : t)
  | h > 0 = 1 + pozitive t
  | otherwise = 0 + pozitive t

pozitive' lst = sum ([1 | x <- lst, x > 0])

impare [] poz = []
impare (h : t) poz
  | odd h = poz : (impare t (poz + 1))
  | otherwise = impare t (poz + 1)

pozImpare lst = impare lst 0

pozImpare' lst =
  let index = [0 .. (length lst)]
   in [snd x | x <- zip lst index, odd (fst x)]

multDigitsRec [] = 1
multDigitsRec (h : t)
  | ord '0' <= ord h && ord h <= ord '9' = (ord h - (ord '0')) * (multDigitsRec t)
  | otherwise = 1 * (multDigitsRec t)

--comp

isDigitt x
  | ord '0' <= ord x && ord x <= ord '9' = True
  | otherwise = False

multDigitsComp lst = product ([digitToInt x | x <- lst, isDigitt x])

discountRec [] = []
discountRec (h : t)
  | rez < 200 = rez : (discountRec t)
  | otherwise = discountRec t
  where
    rez = h - (h / 4)

discountRec' lst = [rez | x <- lst, let rez = x - (x / 4), rez < 200]
