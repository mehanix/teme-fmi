Notițe curs pentru examenul la POO
---------------

Polimorfism:
--------------

* la compilare:
  * max(int,int)
  * max(float,float)
  * adica: acelasi nume de fct dar alti parametri
* la executie: RTTI

Overloading
--------
* sa schimbi return type nu e suficient pt a da overload
* schimbi parametrii fct


Definiții
--------
* operator - functie care are ca nume un/mai multe simboluri
  * cin>>x » operator>>(cin,x)
* :: » scope resolution operator

Referinte
--------
* pointer implicit, trebuie initializat la declarare
* poate fi doar initializat, nu modificat
* devine alias pt variabila
* nu poti avea referinte NULL, sau array de referinte, sau obtine adresa unei referinte, sau ref catre bitset?

Functii
-----
### Friend

* **Functii friend:**
  * faci o fct friend si accesezi cu ea membrii protected/private ai unei clase fara ca fct sa apartina clasei (waw)
  * merge sa ai clasa C2 care are friend o functie "F" din C1 (si asa in F ai acces si la membri privati din c1 si din c2)
* **clase friend:**
  * clasa C1 e prietena cu C2 => toate functiile din C1 au acces la membrii privati din C2
  ```cpp
  class TwoValues { 
  int a; 
  int b; 
  public: 
      TwoValues(int i, int j) { a = i; b = j; }
      friend class Min; 
  }; 

  class Min { 
  public: 
      int min(TwoValues x); 
  }; 

  int Min::min(TwoValues x) 
  ```

### Inline
* Explicit:
  ```cpp
    class myclass { 
        int a, b; 
    public: 
        void init(int i, int j); 
    }; 

    // Create an inline function. 
    inline void myclass::init(int i, int j) 
    { a = i; b = j; }
  ```
* Implicit:
    ```cpp
    class myclass { 
        int a, b; 
    public: 
        // automatic inline 
        void init(int i, int j) { a=i; b=j; } 
        };
    ```

Chichițe a la Păun
---------
* cand pui **valori implicite** unor operatori de functii:
  * argumentele cu valori implicite trebuie sa se afle neaparat la sfarsitul listei de parametri.
  * Se specifica o singura data in definitie(de obicei in prototip)
* Unele **functii** pot fi **membru stang** pt atribuire (cand returneaza reference)
    ```cpp
    char s[10] = "Hello";
    char& f(int i) {  return s[i];}

    int main() {
        f(2) = 'X';
        cout<<s;
        return 0;
    }
    ```
* nu poti pune auto, extern, register in clasa
* Constructor cu un parametru » conversie implicita
  ```
  X(int j){a=j}
  ...
  X ob = 99; // == X ob(99)
  ```
* vector de obiecte: merg initializate individual cu {X(param), X(param)} etc.
De cercetat
-------
* funcțiile membru sunt date prin semnătură ??????
* referinta vs pointer constant?
* union: curs 3 slideurile 25+