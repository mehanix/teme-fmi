{-
Gasiti mai jos limbajul unui minicalculator si o interpretare partiala. 
Calculatorul are doua celule de memorie, care au valoarea initiala 0. Expresia `Mem := Expr` are urmatoarea semantica: 
`Expr` este evaluata, iar valoarea este pusa in `Mem`.  
Un program este o expresie de tip `Prog`iar rezultatul executiei este dat de valorile finale ale celulelor de memorie.
Testare se face apeland `run test`. 
-}

data Prog  = Stmt ::: Prog | Off
data Stmt  = Mem := Expr
data Mem = Mem1 | Mem2 
data Expr  =  M Mem | V Int | Expr :+ Expr

infixl 6 :+
infix 3 :=
infixr 2 :::

type Env = (Int,Int)   -- corespunzator celor doua celule de memorie (Mem1, Mem2)

  
expr ::  Expr -> Env -> Int
expr (e1 :+  e2) m = expr  e1 m + expr  e2 m
expr _ _ = undefined

stmt :: Stmt -> Env -> Env
stmt _ _ = undefined


prog :: Prog -> Env -> Env
prog Off m = m
prog _ _ = undefined

run :: Prog -> Env
run p = prog p (0, 0)


test1 = Mem1 := V 3 ::: Mem2 := M Mem1 :+ V 5 ::: Off
test2 = Mem2 := V 3 ::: Mem1 := V 4 ::: Mem2 := (M Mem1 :+ M Mem2) :+ V 5 ::: Off
test3 = Mem1 := V 3 :+  V 3 ::: Off

{-CERINTE

1) (10pct) Finalizati definitia functiilor de interpretare.
2) (10 pct) Adaugati expresia `e1 :/ e2` care evaluează expresiile e1 și e2, apoi
  - dacă valoarea lui e2 e diferită de 0, se evaluează la câtul împărțirii lui e1 la e2;
  - în caz contrar va afișa eroarea "împarțire la 0" și va încheia execuția.
3)(20pct) Definiti interpretarea  limbajului extins astfel incat executia unui program fara erori sa intoarca valoarea finala si un mesaj
   care retine toate modificarile celulelor de memorie (pentru fiecare instructiune `m :< v` se adauga 
   mesajul final `Celula m a fost modificata cu valoarea v`), mesajele pastrand ordine de efectuare a instructiunilor.  
    Rezolvați subiectul 3) în același fișier redenumind funcțiile de interpretare. 

Indicati testele pe care le-ati folosit in verificarea solutiilor. 

-}