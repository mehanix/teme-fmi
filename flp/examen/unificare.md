a, b contante =>
    a = b => Nu se poate
X variabila, XXXX cv =>
    X = XXXX => L-am gasit pe X (este XXXX)
h(A, B, C) = h(X, Y, Z) =>
    A = X
    B = Y
    C = Z

S1.1

Pas1:
    S: []
    R:
        p(a, x, h(g(y))) = p(z, h(z), h(u))

Pas2:
    S: []
    R:
        a = z
        x = h(z)
        h(g(y)) = h(u)

Pas3:
    S: 
        z = a
    R: 
        x = h(a)
        h(g(y)) = h(u)

Pas4:
    S: 
        z = a
        x = h(a)
    R: 
        h(g(y)) = h(u)

Pas5:
    S: 
        z = a
        x = h(a)
    R: 
        g(y) = u

Pas6:
    S: 
        z = a
        x = h(a)
        u = g(y)
    R: []

z = a
x = h(a)
u = g(y)



S1.2

Pas0:
    S: []
    R:
        g(y) = x 
        p(x, h(y), y) = p(g(z), b, z)
Pas1:
    S:
        x = g(y)
    R:
        p(g(y), h(y), y) = p(g(z), b, z)
Pas2:
    S:
        x = g(y)
    R:
        g(y) = g(z)
        h(y) = b
        y = z
Pas3:
    S:
        x = g(y)
        y = z
    R:
        g(z) = g(z)
        h(z) = b -- FAIL
        

S1.2

1. p(X,Y) :- q(X,Z), r(Z,Y).
2. p(X,X) :- s(X).
3. q(X,b).
4. q(b,a).
5. q(X,a) :- r(a,X).
6. r(b,a).
7. s(X) :- t(X,a).
8. s(X) :- t(X,b).
9. s(X) :- t(X,X).
10. t(a,b).
11. t(b,a).

?- p(X, X).

p(X, X)
    \-> p(X, X) = p(X, Y) (1) <=> Y = X
        :- q(X, Z), r(Z, X)
            \-> q(X, Z) = q(X,b) (3) <=> Z = b
                :- r(b, X)
                    \-> r(b, X) = r(b,a) (6) <=> X = a
                        => SUCCESS (X = a).
            \-> q(X, Z) = q(b,a) (4) <=> X = b, Z = a
                :- r(a, b).
                    \-> FAIL.
            \-> q(X, Z) = q(X, a) (5) <=> Z = a
                :- r(a, X)
                    \-> FAIL.
    \-> p(X, X) = p(X, X) (2) <=> X = X
        :- s(X)
            \-> s(X) = s(X) (7) <=> X = X
                :- t(X, a)
                    \-> t(X, a) = t(b, a) (11) <=> X = b
                        \-> SUCCESS (X = b).
            \-> S(X) = s(X) (8) <=> X = X
                :- t(X, b)
                    \-> t(X, b) = t(a, b) (10) <=> X = a
                        \-> SUCESS (X = a).
            \-> s(X) = s(X) (9) <=> X = X
                :- t(X, X)
                    \-> FAIL.







P(X, X)
    \-> p(X,X) :-
            q(X,Z), r(Z,X)
                \-> q(X,Z) = q(X,b) <=> Z = b
                        \-> r(b, X) = r(b,a). => Z = b, X = a
                \-> q(X, Z) = q(b,a) <=> X = b, Z = a
                        \-> r(a, b) => FAIL
                \-> q(X, Z) = q(X,a) <=> Z = a



S1.3



  /---------------------------------------------------
 /   /----------------------------------
/   /   /-------    /-----                 /----------
λx.(λy.(λx.x + z) ((λx.x x) (x + y) + x)) (λz. x  y  z)
 1   2   3 4   5     6 7 8   9  10   11    12 13 14 15

λx.(x x)   <=> Prolog:     x       :-       x                  y
                        legatura    variabila legata   variabila libera
λx.(x x) y  ->  y y 
  aici x din paranteza sunt variabile legate de variabila de legatura (de argument)
  
variabile libere 

 
 x1 = argument  (de legatura)
 y2 = legatura
 x3 = legatura
 x4 = legata de x3
 z5 = variabila libera
 x6 = legatura 
 x7 = legata de x6
 x8 = legata de x6
 x9 = legat de x1
 y10 = legat de y2
 x11 = legat de x1
 z12 = de legatura
 x13 = legat de x1
 y14 = variabila libera
 z15 = legat de z12


S1.4

empty :: list X
cons :: X -> List X -> List X
uncons :: list X -> Y -> (X -> list X -> Y) -> Y


type(_, empty, list(T)) :-
    is_type(T).
type(Gamma, cons(Head, Tail, List), list(Tip)) :-
    type(Gamma, Head, Tip),
    type(Gamma, Tail, list(Tip)),
    is_type(Tip).
type(Gamma, uncons(Lista, IfEmpty, IfNotEmpty), TipY) :-
    type(Gamma, Lista, list(TipX)),
    type(Gamma, IfEmpty, TipY),
    type(Gamma, IfNotEmpty, TipX -> list(TipX) -> TipY).


?????
```python
def uncons(lista, if_empty, if_not_empty):
    if lista == []:
        return if_empty
    head, tail = lista[0], lista[1:]
    return if_not_empty(head, tail)
```

<if (0 <= i, i = i + -4; while (0 <= i, { i = i + -4}), skip), i = 3>
il scoatem pe i din env.
<if (0 <= 3, i = i + -4; while (0 <= i, { i = i + -4}), skip), i = 3>
Il comparam pe 0 cu 3.
<if (true, i = i + -4; while (0 <= i, { i = i + -4}), skip), i = 3>
Executam if-ul.
<i = i + -4; while (0 <= i, { i = i + -4}), i = 3>
Evaluam i.
<i = 3 + -4; while (0 <= i, { i = i + -4}), i = 3>
facem suma.
<i = -1; while (0 <= i, { i = i + -4}), i = 3>
Updatam i.
<while (0 <= i, { i = i + -4}), i = -1>
Transformam while in if.
<if (0 <= i, i = i + -4; while (0 <= i, { i = i + -4}), skip), i = -1>
il evaluam pe i.
<if (0 <= -1, i = i + -4; while (0 <= i, { i = i + -4}), skip), i = -1>
Executam comparatia
<if (false, i = i + 4; while (0 <= i, { i = i + -4}), skip), i = -1>
executam if.
<skip, i = -1>
exetuam skip-ul.
<i = -1>