unu(X, Y) :- doi(X, Y), X = Y.


% forall X Y. X = Y /\ doi(X, Y) -> unu(X, Y).


doi(A, B) :- A == B.
