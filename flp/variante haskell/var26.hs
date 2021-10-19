
{-
Gasiti mai jos limbajul unui minicalculator si o interpretare partiala. 
Calculatorul are doua celule de memorie, care au valoarea initiala 0.
Expresia `mem :< expr` are urmatoarea semantica: 
`expr` este evaluata, iar valoarea este pusa in `mem`.  
Un program este o expresie de tip `Prog`iar rezultatul executiei este dat de valorile finale ale celulelor de memorie.
Testare se face apeland `run test`. 
-}

data Prog  = Stmt ::: Prog | Off
data Stmt  = Mem :< Expr
data Mem = Mem1 | Mem2 
data Expr  =  M Mem | V Int | Expr :+ Expr | If Expr Expr

infixl 6 :+
infix 3 :<
infixr 2 :::

type Env = (Int,Int)   -- corespunzator celor doua celule de memorie (Mem1, Mem2)

  
expr ::  Expr -> Env -> Int 
expr (e1 :+  e2) m = expr  e1 m + expr  e2 m
expr (M Mem1) m = fst m 
expr (M Mem2) m = snd m 
expr (V i) m = i

--2
expr (If e1 e2) m
   | fst m == 0 = expr e1 m
   | otherwise = expr e2 m
--end 2

stmt :: Stmt -> Env -> Env
stmt (Mem1 :< e) m = 
   let calc = expr e m in
      (calc,snd m)
stmt (Mem2 :< e) m = 
   let calc = expr e m in
      (fst m,calc)


prog :: Prog -> Env -> Env
prog Off m = m
prog (st ::: pr) m = prog pr (stmt st m)
run :: Prog -> Env
run p = prog p (0, 0)


test1 = Mem1 :< V 3 ::: Mem2 :< M Mem1 :+ V 5 ::: Off
test2 = Mem2 :< V 3 ::: Mem1 :< V 4 ::: Mem2 :< (M Mem1 :+ M Mem2) :+ V 5 ::: Off
test3 = Mem1 :< V 3 :+  V 3 ::: Off

test4 = Mem2 :< V 5 ::: Mem1 :< If ( V 10) ( V 50) ::: Off
test5 = Mem1 :< V 5 ::: Mem1 :< If ( V 10) ( V 50) ::: Off

{-CERINTE

1) (10pct) Finalizati definitia functiilor de interpretare. -- done
2) (10 pct) Adaugati expresia `If e1 e2` care evaluează `e1` daca `Mem1` are valoarea `0` si evaluează 
   `e2` in caz contrar.
3)(20pct) Definiti interpretarea  limbajului extins astfel incat executia unui program sa intoarca valoarea finala si un mesaj
   care retine toate modificarile celulelor de memorie (pentru fiecare instructiune `m :< v` se adauga 
   mesajul final `Celula m a fost modificata cu valoarea v`), mesajele pastrand ordine de efectuare a instructiunilor.  
    Rezolvați subiectul 3) în același fișier redenumind funcțiile de interpretare. 

Indicati testele pe care le-ati folosit in verificarea solutiilor. 

-}

---3

newtype WriterLS a = Writer {runWriter :: (a, [String])}

instance Monad WriterLS where
  return va = Writer (va, [])
  ma >>= k =
    let (va, log1) = runWriter ma
        (vb, log2) = runWriter (k va)
     in Writer (vb, log1 ++ log2)

instance Applicative WriterLS where
  pure = return
  mf <*> ma = do
    f <- mf
    a <- ma
    return (f a)

instance Functor WriterLS where
  fmap f ma = pure f <*> ma

tell :: String -> WriterLS ()
tell log = Writer ((), [log])



stmt2 :: Stmt -> WriterLS Env -> WriterLS Env
stmt2 (Mem1 :< e) env = do
   m <- env
   let calc = expr e m 
   tell ("Folosit Mem1")
   return (fst m, calc)
stmt2 (Mem2 :< e) env = do
   m <- env
   let calc = expr e m 
   tell ("Folosit Mem2")
   return (fst m, calc)
-- stmt2 (Mem2 :< e) m = 
--    let calc = expr e m in
--       (fst m,calc)

prog2 :: Prog -> WriterLS Env -> WriterLS Env
prog2 Off env = env
prog2 (st ::: pr) env = (prog2 pr (stmt2 st env))

run2 :: Prog -> (Env, [String])
run2 p = runWriter $ prog2 p (Writer((0,0), []))