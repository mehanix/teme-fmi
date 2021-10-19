import Data.Either
type Val = Int
data Operatie = Add | Tail Operatie
data Lit = V Val | Id String
data Arb
   = Leaf Lit
   | Node Operatie [Arb]

type Stare = [(String, Val)]   -- valori pentru identificatorii (`Id x`) din arbore

eval ::  Arb -> Stare -> Either String Val
eval (Leaf v) env = val v env
eval (Node Add []) env = Right 0
eval (Node (Tail op) []) env = Left "lista vida"


-- eval (Node op ((Leaf l):t)) env = case op of
--     Add -> val l env + (eval(Node op t) env)
--     Tail op' -> (eval(Node op' t) env)

-- eval (Node op ((Node op' arb):t)) env = case op of
--     Add -> (eval (Node op' arb) env) + (eval (Node op t) env)
--     Tail op'' -> (eval (Node op'' t) env)

eval (Node op ((Leaf l):t)) env = 
    let a = val l env
        b = eval(Node op t) env
        c = case (a) of
            Right r -> r
            Left msg -> error msg
        d = case (b) of
            Right r -> r
            Left msg -> error msg in 
        case op of
            Add -> Right (c+d)
            Tail op' ->Right (d)
    

eval (Node op ((Node op' arb):t)) env =
    let a = eval (Node op' arb) env
        b = (eval (Node op t) env)
        c = case (a) of
            Right r -> r
            Left msg -> error msg
        d = case (b) of
            Right r -> r
            Left msg -> error msg in 
        case op of  
            Add -> Right (c+d)
            Tail op' -> Right (d)

-- eval (Node op ((Node op' arb):t)) env = case op of

--     Add -> Right (fromRight 0 (eval (Node op' arb) env) + fromRight 0(eval (Node op t) env))
--     Tail op'' -> Right (fromRight 0(eval (Node op'' t) env))

val :: Lit -> Stare -> Either String Val
val (V v) _ = Right v
val (Id name) env = let res = lookup name env in
    case res of
        Nothing -> Left "variabila negasita"
        Just v -> Right v 

-- test :: Val -> Bool
-- -- test = (/= 0)

run test state = eval test state
-- simplu
test1 = (Leaf (V 1)) --1
-- root cu 3 noduri
test2 = (Node Add [Leaf (V 1), Leaf (V 2), Leaf (V 3)]) --6
-- root, nod, ramura 2 noduri
test3 = (Node Add [Leaf (V 4), Node Add [Leaf (V 5), Leaf (V 6)]]) --15
-- ramura in ramura
test4 = (Node Add [Leaf (V 4), Node Add [Node Add[Leaf (V 1), Leaf (V 2)], Leaf (V 6)]]) --13
-- variabile
test5 = (Node Add [Leaf (Id "a"), Leaf (Id "b"), Leaf (V 3)]) --cu state = [("a",1),("b",2)] -> 6
-- crapa
test9 =  (Node Add [Leaf (Id "c"), Leaf (Id "b"), Leaf (V 3)]) --cu state = [("a",1),("b",2)] -> error


--- teste pt 2

-- tail simplu
test6 = (Node (Tail Add) [Leaf (V 1), Leaf (V 2), Leaf (V 3)]) --5

-- tail de 2 ori
test7 = (Node (Tail Add) [Node (Tail Add) [Leaf (V 1)], Leaf (V 2), Leaf (V 3), Leaf (V 4)])

-- variabile
test8 = (Node (Tail Add) [Leaf (Id "a"), Leaf (Id "b"), Leaf (V 3)]) --cu state = [("a",1),("b",2)] -> 5

-- crapa
test10 = (Node (Tail Add)[])
