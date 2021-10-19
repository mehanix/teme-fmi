-- 1 a

-- functie care verifica daca o litera e permisa sau nu (vocalele mici nu-s permise, orice altceva este)
verif 'a' = False
verif 'e' = False
verif 'i' = False
verif 'o' = False
verif 'u' = False 
verif _ = True

-- trec prin toate literele si dau si intre valorile returnate de verif, daca e vreo vocala mica imi face toata conditia false
vocaleRec:: [Char] -> Bool
vocaleRec "" = True
vocaleRec (x:xs) = (verif x) && (vocaleRec xs)

-- b

-- aleg doar literele care nu sunt permise, daca am mai mult de 0 atunci cuvantul nu e ok
vocaleLst cuvant = if length [x | x <- cuvant, not (verif x)] > 0 then False else True

-- c
-- filtrez doar literele nepermise din cuvant, daca am gasit macar una atunci cuvantul nu e ok
vocaleFilter cuvant = if length (filter (\x -> verif x == False) cuvant) > 0 then False else True

-- teste

test1 = "banane pestrite" -- False
test2 = "bAnAne pestrIte" -- False
test3 = "bAnAnE pEstrItE" -- true

--2

data Pol =   X Integer     -- variabila X la putere, puterea o presupunem >=0
           | S Integer     -- scalari
           | Pol :+: Pol   -- adunare
           | Pol :*: Pol   -- produs/inmultire
       deriving (Show)


-- functie care parcurge o expresie Pol si returneaza lista puterilor
puteri (S v1 :*: X n1) = [n1]
puteri (expr :+: restul) = puteri expr ++ puteri restul

-- functie care parcurge o expresie Pol si returneaza lista coeficientilor
coef (S v1 :*: X n1) = [v1]
coef (expr :+: restul) = coef expr ++ coef restul

-- functie care verifica daca expresia este formata corect
forma (S _) = False
forma (X _) = False
forma (S v1 :*: X n1) = True
forma (expr :+: restul) = (forma expr) && (forma restul) 

-- functie care verifica daca lista data are elementele in ordine descrescatoare
descrescator (x:y:xs) = (x>y) && descrescator (y:xs)
descrescator x = True

-- daca polinomul dat are forma corecta, si toti coeficientii pozitivi, si toate puterile descrescatoare, atunci e bun, altfel nu
ex2 polinom = if (forma polinom) then (all (>0) (coef polinom)) && (descrescator (puteri polinom)) else False


testf1 = (S 2 :*: X 3) :+: ((S 2 :*: X 2) :+: (S 2 :*: X 1)) -- true
testf2 = (S 2 :*: X 3) :+: ((S 2 :+: X 2) :+: (S 2 :*: X 1))  -- false, forma gresita polinom
testf3 = (S 2 :*: X 1) :+: ((S 2 :+: X 3) :+: (S 2 :*: X 2)) -- false, nu s in ordine x-urile
testf4 = (S 3 :*: X 3) :+: ((S 2 :+: X 2) :+: (S (-2) :*: X 1)) -- false, scalari negativi

--3

data Digit = O | I | D deriving (Eq)                        -- O =0, I=1, D=2
data NBase = NB  Digit Digit Digit deriving (Eq)     -- numere in baza 3 pe 3 biti

instance Show Digit where
    show O = "O"
    show I = "I"
    show D = "D"

-- conversie cifra la digit
numarLaDigit::Integer -> Digit
numarLaDigit 0 = O
numarLaDigit 1 = I
numarLaDigit 2 = D

digitLaNumar O = 0
digitLaNumar I = 1
digitLaNumar D = 2

class MyNum x where
  myfromInteger :: Integer -> x
  myNegate :: x -> x

-- fa negarea, scade din D D D numarul tau si apoi aduna 1 (practic fac complementul lui 3, conform
-- mesajului dat pe teams "Atentie! daca n este un numar pe k biti atunci n + (negate n) = 10000 unde apare k de 0"
-- daca fac doar ce scrie in cerinta (fara sa adun 1), cele 2 numere adunate nu o sa dea  O O O cum se cere mai sus)
-- asadar fac D - fiecare bit si la finalul crearii numarului adun 1
transforma (NB a b c) = 26 - (9*(digitLaNumar a) + 3*(digitLaNumar b) + (digitLaNumar c)) + 1


instance MyNum NBase where
    -- pt orice numar pozitiv, transforma-l din baza 10 in baza 3, pastrand doar cei mai nesemnificativi biti daca repr lui e mai mare
    myfromInteger x = if (x<0) then error "numar negativ"
    else NB (numarLaDigit ((x `div` 9) `mod` 3)) (numarLaDigit ((x `div` 3) `mod` 3)) (numarLaDigit (x `mod` 3))
    myNegate x = myfromInteger (transforma x)

test_ex3_simplu = (myfromInteger 5 == NB O I D)
teste_ex3_numar_mare = (myfromInteger 500 == NB I I D) -- 500 e 200112 in b3 ramane doar 112
teste_ex3_zero = (myfromInteger 0 == NB O O O)
teste_ex3_max = (myfromInteger 26 == NB D D D)

teste_ex3_negatie = (myNegate (NB O D D) == (NB D O I)) -- O D D + D O I = I O O O, true

