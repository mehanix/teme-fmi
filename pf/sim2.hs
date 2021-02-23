import qualified Data.Foldable as F
import Data.Maybe

data Arbore a
  = Nod (Arbore a) a (Arbore a)
  | Frunza a
  | Empty

-- maxMaybe Nothing Nothing = Nothing
-- maxMaybe (Nothing) (Just a) = Just a
-- maxMaybe (Just a) (Nothing) = Just a
-- maxMaybe (Just a) (Just b) = Just (max a b)

-- getMax Empty = Nothing
-- getMax (Frunza a) = Just a
-- getMax (Nod l a r) =
--   let maxL = getMax l
--    in let maxR = getMax r
--        in maxMaybe (maxMaybe maxL maxR) (Just a)

-- minMaybe Nothing Nothing = Nothing
-- minMaybe (Nothing) (Just a) = Just a
-- minMaybe (Just a) (Nothing) = Just a
-- minMaybe (Just a) (Just b) = Just (min a b)

-- getmin Empty = Nothing
-- getmin (Frunza a) = Just a
-- getmin (Nod l a r) =
--   let minL = getmin l
--    in let minR = getmin r
--        in minMaybe (minMaybe minL minR) (Just a)

-- fromMaybe' (Just a) = a
-- fromMaybe' Nothing = -100

-- fromMaybe'' (Just a) = a
-- fromMaybe'' Nothing = 100

-- verifica (Empty) = True
-- verifica (Frunza a) = True
-- verifica (Nod left a right)
--   | (fromMaybe' (getMax left)) >= a = False
--   | (fromMaybe' (getmin right)) <= a = False
--   | otherwise = verifica left && verifica right

data Numar a = Something a | MinInf | MaxInf deriving (Eq)

instance (Eq a, Ord a) => Ord (Numar a) where
  Something a <= MinInf = False
  MinInf <= Something a = True
  Something a <= MaxInf = True
  MaxInf <= Something a = False
  MinInf <= MaxInf = True
  MaxInf <= MinInf = False
  Something a <= Something b = a <= b

getMax Empty = MinInf
getMax (Frunza a) = Something a
getMax (Nod l a r) =
  let maxL = getMax l
   in let maxR = getMax r
       in max (max maxL maxR) (Something a)

getMin Empty = MinInf
getMin (Frunza a) = Something a
getMin (Nod l a r) =
  let minL = getMin l
   in let minR = getMin r
       in min (min minL minR) (Something a)

verifica Empty = True
verifica (Frunza a) = True
verifica (Nod l a r)
  | getMax l >= Something a = False
  | getMin r <= Something a = False
  | otherwise = verifica l && verifica r

insert x Empty = Frunza x
insert x (Frunza a)
  | x > a = Nod Empty a (Frunza x)
  | x < a = Nod (Frunza x) a Empty
  | otherwise = Frunza a
insert x (Nod l a r)
  | x < a = Nod (insert x l) a r
  | x > a = Nod l a (insert x r)
  | otherwise = Nod l a r

instance Functor Arbore where
  fmap f Empty = Empty
  fmap f (Frunza x) = Frunza (f x)
  fmap f (Nod l x r) = Nod (fmap f l) (f x) (fmap f r)

instance F.Foldable Arbore where
  foldMap f Empty = mempty
  foldMap f (Frunza a) = f a
  foldMap f (Nod l a r) =
    F.foldMap f l
      `mappend` f a
      `mappend` F.foldMap f r

foldme :: (Show a) => Arbore a -> [Char]
foldme Empty = ""
foldme (Frunza a) = show a ++ ","
foldme (Nod l a r) = foldme l ++ foldme (Frunza a) ++ foldme r

f lst = [p | p <- lst, even (fst p) && even (snd p)] == [p | p <- lst, even (fst p) && even (snd p) && (fst p) * (snd p) > 10]

pp newlst _ [] = newlst
pp newlst prod (h : t)
  | even h = pp (newlst ++ [prod]) (prod * h) t
  | otherwise = pp (newlst ++ [prod]) prod t

p lst = pp [] 1 lst

--p' lst = foldr (\x acc -> if even x then ((snd acc) : (fst acc), (snd acc) * x) else ((snd acc) : (fst acc), (snd acc))) ([], 1) lst

--p' lst = foldr (\x acc -> acc ++ [getsumm x])

data Binar a = Leaf a | Node (Binar a) (Binar a)

tree = (Node (Node (Leaf 3) (Leaf 4)) (Node (Node (Leaf 1) (Leaf 2)) (Leaf 5)))

encoding (Leaf a) curent = [(a, curent)]
encoding (Node a b) curent = (encoding a (curent ++ [True])) ++ (encoding b (curent ++ [False]))

getSum = do
  nr <- getLine
  let val = read nr
  if (val == 0)
    then return 0
    else do
      nr2 <- getSum
      return (val + nr2)

type Nume = String
data Prop
  = Var Nume
  | F
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  | Prop :->: Prop
  | Prop :<->: Prop
  deriving (Eq, Read)
infixr 2 :|:
infixr 3 :&:

instance Show Prop where
  show (Var nume)= nume
  show (a :|: b) = "("++show a ++ "|" ++ show b++")"
  show (a :&: b) = "("++show a ++ "&" ++ show b++")"
  show (a :->: b) = "("++show a ++ "->" ++ show b++")"
  show (a :<->: b) = "("++show a ++ "<->" ++ show b++")"
  show (Not p) = "(~"++show p++")" 
  show F = "F"
  show T = "T"

test_ShowProp :: Bool
test_ShowProp =
    show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"

type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

impl :: Bool -> Bool -> Bool
impl False _ = True
impl _ x = x

echiv :: Bool -> Bool -> Bool
echiv x y = x==y

eval :: Prop -> Env -> Bool
eval (Var x) env = impureLookup x env	
eval T _ = True
eval F _ = False
eval (Not p) env = not $ eval p env
eval (p :&: q) env = eval p env && eval q env
eval (p :|: q) env = eval p env || eval q env
eval (p :->: q) env = eval p env `impl` eval q env
eval (p :<->: q) env = eval p env `echiv` eval q env


 
test_eval = eval  (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True

variabile :: Prop -> [Nume]
variabile (Var p) = [p]
variabile (Not p) = nub $ variabile p
variabile (p :&: q) = nub $ variabile p ++ variabile q
variabile (p :|: q) = nub $ variabile p ++ variabile q
variabile (p :->: q) = nub $ variabile p ++ variabile q
variabile (p :<->: q) = nub $ variabile p ++ variabile q
variabile _ = [] -- T si F  
 
test_variabile =
  variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]

envs :: [Nume] -> [[(Nume, Bool)]]
envs [] = []
envs [x] = [[(x,False)],[(x,True)]]
envs (str:xs) = let r = envs xs in  map (\x-> (str,False):x) r  ++ map (\x->(str,True):x) r
 
test_envs = 
    envs ["P", "Q"]
    ==
    [ [ ("P",False)
      , ("Q",False)
      ]
    , [ ("P",False)
      , ("Q",True)
      ]
    , [ ("P",True)
      , ("Q",False)
      ]
    , [ ("P",True)
      , ("Q",True)
      ]
    ]

fold1 lst letter val = foldr (\x acc -> ((letter, val) : x) : acc) [] lst

envs lst = foldr (\x acc -> ((fold1 acc x True) ++ (fold1 acc x False))) [[]] lst

valida prop = 