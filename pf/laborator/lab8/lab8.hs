import Data.List (nub)
import Data.Maybe (fromJust)

type Nume = String

data Prop
  = Var Nume
  | F
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  deriving (Eq, Read)

infixr 2 :|:

infixr 3 :&:

p1 :: Prop
p1 = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

p2 :: Prop
p2 = undefined

p3 :: Prop
p3 = undefined

instance Show Prop where
  show (Var n) = n
  show (a :|: b) = (show a ++ " | " ++ show b)
  show (a :&: b) = (show a ++ " & " ++ show b)

test_ShowProp :: Bool
test_ShowProp =
  show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"

type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a, b)] -> b
impureLookup a = fromJust . lookup a

eval :: Prop -> Env -> Bool
eval (Var x) env = impureLookup x env
eval F _ = False
eval T _ = True
eval (Not p) env = not (eval p env)
eval (p :|: q) env = (eval p env) || (eval q env)
eval (p :&: q) env = (eval p env) & (eval q env)

test_eval = eval (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True

variabile :: Prop -> [Nume]
variabile (Var x) = [x]
variabile (Not p) = nub variabile p
variabile (p :|: q) = 

test_variabile =
  variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]

envs :: [Nume] -> [Env]
envs = undefined

test_envs =
  envs ["P", "Q"]
    == [ [ ("P", False),
           ("Q", False)
         ],
         [ ("P", False),
           ("Q", True)
         ],
         [ ("P", True),
           ("Q", False)
         ],
         [ ("P", True),
           ("Q", True)
         ]
       ]

satisfiabila :: Prop -> Bool
satisfiabila = undefined

test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True

test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Var "P") == False

valida :: Prop -> Bool
valida = undefined

test_valida1 = valida (Not (Var "P") :&: Var "Q") == False

test_valida2 = valida (Not (Var "P") :|: Var "P") == True

tabelAdevar :: Prop -> String
tabelAdevar = undefined

echivalenta :: Prop -> Prop -> Bool
echivalenta = undefined

test_echivalenta1 =
  True
    == (Var "P" :&: Var "Q") `echivalenta` (Not (Not (Var "P") :|: Not (Var "Q")))

test_echivalenta2 =
  False
    == (Var "P") `echivalenta` (Var "Q")

test_echivalenta3 =
  True
    == (Var "R" :|: Not (Var "R")) `echivalenta` (Var "Q" :|: Not (Var "Q"))
