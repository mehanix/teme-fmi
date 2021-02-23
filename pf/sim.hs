import Data.Char
import Data.List

rotate _ "" = ""
rotate n str
  | n < 0 || n > length str = error "aiurea"
  | otherwise = (drop n str) ++ (take n str)

makeKey n = zip ['A' .. 'Z'] (rotate n ['A' .. 'Z'])

lookUp ch lst = snd (head (filter (\x -> ch == fst (x)) (lst) ++ [(ch, ch)]))

encipher n ch = lookUp ch (makeKey n)

normalize str = map toUpper (filter isAlphaNum str)

encipherStr n str = map (\x -> encipher n x) (normalize str)

reverseKey lst = [(snd (x), fst (x)) | x <- lst]

decipher n ch = lookUp ch (reverseKey (makeKey n))

decipherStr n str = map (\x -> decipher n x) (normalize str)

data Fruct
  = Mar String Bool
  | Portocala String Int
  deriving (Show)

listaFructe = [Mar "Ionatan" False, Portocala "Sanguinello" 10, Portocala "Valencia" 22, Mar "Golden Delicious" True, Portocala "Sanguinello" 15, Portocala "Moro" 12, Portocala "Tarocco" 3, Portocala "Moro" 12, Portocala "Valencia" 2, Mar "Golden Delicious" False, Mar "Golden" False, Mar "Golden" True]

getTip (Portocala x _) = x
getTip (Mar _ _) = ""

getFelii (Portocala _ x) = x

f = map (getTip) listaFructe

ePortocalaDeSicilia lst = filter (\x -> (getTip x) `elem` ["Tarocco", "Moro"]) lst

nrFeliiSicilia = sum ([getFelii x | x <- ePortocalaDeSicilia listaFructe])

data Linie = L [Int]
  deriving (Show)

data Matrice = M [Linie]

getLinii (M t) = t

getElem (L t) = t

f2 [] = ""
f2 (h : t) = (show h) ++ " " ++ f2 t

instance Show Matrice where
  show (M linii) =
    "[" ++ foldr (\x acc -> show x ++ "\n" ++ acc) "]" linii

verifica mat val = foldr op unit (getLinii mat)
  where
    a `op` b = (sum (getElem a) == val) && b
    unit = True

f (h : t) lst