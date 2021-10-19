-- data Exp = Atom String
--     | Not Exp
--     | And Exp Exp
--     | Or Exp Exp
--     deriving (Show)

-- dnf (Atom _) = True
-- dnf (Not (Atom _)) = True
-- dnf (Not _) = False
-- dnf (Or a b) = (dnf a) && (dnf b)
-- dnf (And (Or _ _) _) = False
-- dnf (And _ (Or _ _)) = False
-- dnf (And a b) = (dnf a) && (dnf b) 

-- a = Or (Or (Atom "d")(Atom "c"))(And (Atom "a")(Not(Atom "b")))

-- -- 
-- b = Or (Atom "a") (And (Atom "b") (Or (Atom "c")(Not (Atom "d"))))

data T a = L (Either String a) | N (T a) (T a)

--

instance Foldable T where
    foldr op acc (L (Right va)) = (va `op` acc)
    foldr op acc (L (Left vb)) = acc
    -- dau fold in partea dreapta, ala devine nou acc, si se reface fold pe partea stanga
    foldr op acc (N a b) = let res = foldr op acc b in
        foldr op res a


a = N (L(Right "a")) (N (L (Left "b")) (L(Right "c")))


class C e where
    cRemove:: String -> (a->Bool) -> e a -> e a
    toList:: e a -> [a]
    fromList::[a] -> e a

instance C T where
    toList (L (Left va)) = []
    toList (L (Right va)) = [va]
    toList (N a b) = (toList a) ++ (toList b) 

    fromList [] = error "de ce"
    fromList [x] = L (Right x)
    fromList (x:xs) = N (L (Right x)) (fromList xs)

    cRemove val fun (L (Left va)) = L (Left va)
    cRemove val fun (L (Right va)) = if (fun va) then (L(Left val)) else (L(Right va))
    cRemove val fun (N a b) = N (cRemove val fun a) (cRemove val fun b) 
