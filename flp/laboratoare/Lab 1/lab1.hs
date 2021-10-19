data Prog = On Instr 
data Instr = Off | Expr :> Instr 
data Expr = Mem | V Int | Expr :+ Expr 
type Env = Int
type DomProg = [Int]
type DomInstr = Env -> [Int]
type DomExpr = Env -> Int

prog :: Prog -> DomProg
prog (On i) = stmt i 0

stmt :: Instr -> DomInstr
stmt Off env = []
stmt (e :> i) env =let ex = expr e env in
   (ex):(stmt i (ex))

expr :: Expr -> DomExpr 
expr Mem env = env 
expr (V i) env = i
expr (e1 :+ e2) env = (expr e1 env) + (expr e2 env)


p1 = On ( (V 3) :> ((Mem :+ (V 5)):> (((V 1) :+ (V 2)) :> (Mem :> Off))))

---------stonks!

type Name = String
data Hask = HTrue
 | HFalse
 | HLit Int
 | HIf Hask Hask Hask
 | Hask :==: Hask
 | Hask :+: Hask
 | HVar Name
 | HLam Name Hask
 | Hask :$: Hask
  deriving (Read, Show)
infix 4 :==:
infixl 6 :+:
infixl 9 :$:

data Value = VBool Bool
 | VInt Int
 | VFun (Value -> Value)
 | VError -- pentru reprezentarea erorilor
type HEnv = [(Name, Value)]

type DomHask = HEnv -> Value

instance Show Value where
  show (VInt i) = show i
  show (VFun a) = "VFun "
  show VError = "VError"
  show (VBool b) = show b

instance Eq Value where
  VBool a == VBool b = (a==b)
  VInt a == VInt b = (a==b)
  _ == _ = error "eroare"

hEval :: Hask -> DomHask
hEval HTrue env = VBool True
hEval HFalse env = VBool False
hEval (HLit i) env = VInt i
hEval (HVar x) env = 
  let rez = lookup x env in
    case rez of
      Nothing -> VError
      Just exp -> exp 

-- hEval (HLam nume x) env = 
--   let rez = lookup nume env in
--     case rez of
--       Nothing -> VError
--       Just exp -> exp    

hEval (h1 :+: h2) env =
  let x = hEval h1 env 
      y = hEval h2 env in 
  case (x,y) of 
    (VInt a, VInt b) -> VInt (a+b)
    _ -> VError


hEval (HIf a b c) env 
  | res == VBool True = hEval b env
  | res == VBool False = hEval c env
  | otherwise = VError
  where 
    res = hEval a env

hEval (h1 :==: h2) env
  | True = VBool (e1 == e2)
  where
    e1 = hEval h1 env
    e2 = hEval h2 env 

hEval (HLam n h) env = VFun (\k -> hEval h ((n,k):env))

-- f a = 5
-- g b = 6

-- f (g 3)
-- f $ g 3

hEval (h1 :$: h2) env
  | True = case f1 of
      VFun f -> f v2
      _ -> VError
  where
    f1 = hEval h1 env
    v2 = hEval h2 env

-- hEval (h1 :$: h2) env =
  
--   let 
--     f1 = hEval h1 env 
--     h = hEval h2 env in
--       case f1 of
--         VFun f -> f h
--         _ -> VError


p2 = HIf (HLit 2 :==: HLit 5) (HTrue) (HFalse)

p3 = HLam x (VFun (V))