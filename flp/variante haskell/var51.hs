{-
Gasiti mai jos limbajul unui minicalculator si o interpretare partiala. 
Calculatorul are o celulă de memorie, care are valoarea initiala  0.
Interpretarea instructiunilor este data mai jos.

Un program este o expresie de tip `Prog`iar rezultatul executiei este starea finala a memoriei. 
Testare se face apeland `prog test`. 
-}

data Prog  = On [Stmt]                
data Stmt =
     Save Expr     -- evalueaza expresia și salvează rezultatul in Mem
   | NoSave Expr   -- evalueaza expresia, fără a modifica Mem 
data Expr  =  Mem | V Int | Expr :+ Expr 


infixl 6 :+


type Env = Int   -- valoarea curentă a celulei de memorie

expr ::  Expr -> Env -> Int
expr (e1 :+  e2) m = expr e1 m + expr e2 m
expr _ _ = undefined

stmt :: Stmt -> Env -> Env
stmt _ _ = undefined

stmts :: [Stmt] -> Env -> Env
stmts _ _ = undefined

prog :: Prog -> Env
prog (On ss) = undefined



test1 = On [Save (V 3), NoSave (Mem :+ (V 5))]
test2 = On [NoSave (V 3 :+  V 3)]

{-CERINTE

1) (10pct) Finalizati definitia functiilor de interpretare.
2) (10 pct) Adaugati expresia `If e e1 e2` care se evaluează `e1` daca `e` are valoarea `0` si la `e2` in caz contrar.
3) (20pct)Definiti interpretarea  limbajului extins modificand functiile de interpretare astfel incat executia unui program
 sa intoarca starea memoriei si  lista valorilor calculate. 
Rezolvați subiectul 3) în același fișier redenumind funcțiile de interpretare.     


Indicati testele pe care le-ati folosit in verificarea solutiilor. 

-}