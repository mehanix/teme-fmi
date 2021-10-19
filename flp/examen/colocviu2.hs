type Val = Int
data Operatie = Add | Tail Operatie
data Lit = V Val | Id String
data Arb
   = Leaf Lit
   | Node Operatie [Arb]

type Stare = [(String, Val)]   -- valori pentru identificatorii (`Id x`) din arbore

eval ::  Arb -> Stare -> Val
eval (Leaf v) env = val v env
eval (Node Add []) env = 0
eval (Node (Tail op) []) env = error "lista vida"


eval (Node op ((Leaf l):t)) env = case op of
    Add -> val l env + (eval(Node op t) env)
    Tail op' -> (eval(Node op' t) env)

eval (Node op ((Node op' arb):t)) env = case op of
    Add -> (eval (Node op' arb) env) + (eval (Node op t) env)
    Tail op'' -> (eval (Node op'' t) env)

val :: Lit -> Stare -> Val
val (V v) _ = v
val (Id name) env = let res = lookup name env in
    case res of
        Nothing -> error "variabila negasita"
        Just v -> v 

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
