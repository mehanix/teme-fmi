


unu(X, Y) :- X = Y, doi(X, Y).


% forall X Y. X = Y /\ doi(X, Y) -> unu(X, Y).


doi(A, B) :- A == B.

%forall X Y. X = Y /\ doi(X, Y) -> unu(X, Y)
%forall A B. A == B
%----------------------------------------------
%exists X. unu(f(X), f(a))



%unu(f(X), f(a))

%redenumim X si Y in
%unu(X, Y) :- X = Y, doi(X, Y).
%obtinem 
%unu(X1, Y1) :- X1 = Y1, doi(X1, Y1).


%unificam unu(f(X), f(a)) cu unu(X1, Y1)
%obtinem MGU theta:  theta(X1) = f(X) si  theta(Y1) = f(a)


%inlocuim unu(f(X), f(a)) cu theta(X1 = Y1, doi(X1, Y1)):
%f(X) = f(a), doi(f(X), f(a))


%unificam f(X) cu f(a) 
%obtinem MGU theta1:   theta1(X) = a

%f(X) = f(a) devine True și dispare. Aplicam theta1 pe doi(f(X), f(a)):
%doi(f(a), f(a))

%redenumim A și B în 
%doi(A, B) :- A == B
%obtinem
%doi(A1, B1) :- A1 == B1

%unificam doi(A1, B1) cu doi(f(a), f(a))
%Obținem MGU theta2: theta2(A1) = f(a) și theta2(B1) = f(A)

%înlocuim 
%doi(f(a), f(a)) cu A1 == B1 și aplicam theta2:
%f(a) == f(a)


%f(a) == f(a) se evaluează la True și dispare.

%multime vidă de literari, deci formula ține.

%În plus am determinat substituția:
%theta1(X) = a.




%?- unu(f(X),f(a)).

%exists X. unu(f(X), f(a))



%%%%%%%%%%%%%%


% Sigma - limbaj de ord I (simboluri de fn, ct)

% X - m variabile

% T_Sigma(X) - modelul termenilor peste Sigma cu var din X

% v(X) = v(f(X))


% f in T_Sigma(X)





% theta(X) = h(Y, Z)

% theta1(Y) = g(Z)

% theta2(Z) = 7



% sol(X) = h(g(7), 7).


