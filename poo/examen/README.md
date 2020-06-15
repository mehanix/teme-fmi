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
* la operatori:
  * ++i: type operator++()
  * i++: type operator++(int x)
* NU merge overload pe:
  * ::
  * .*
  * ?
  * .
* = NU este mostenit din clasa derivata. restul da (curs 4)
### Overload cu friend (curs 4 pg 60+)
* trebuie toti operanzii dati ca argumente(vezi << >>)
* NU merge overload pe = () [] -> cu functii friend
  * iar pt ++ -- trebuie referinte (nu avem this la friend)
* se folosesc cand ai chestii gen 100 + ob (pt ca operatorul se apeleaza de pe operandul din stanga)
 ```cpp
    friend loc operator+(loc op1, int op2); 
    friend loc operator+(int op1, loc op2); 

    // loc + int
    loc operator+(loc op1, int op2){
    loc temp;
    temp.longitude = op1.longitude + op2;
    temp.latitude =op1.latitude + op2;
    return temp;}

    // + is overloaded for int + loc.
    loc operator+(int op1, loc op2){
    loc temp;
    temp.longitude = op1 + op2.longitude;
    temp.latitude =op1 + op2.latitude;
    return temp;}
```
### Overload pe new/delete
Se poate face doar pt **un obiect** (inauntrul clasei) sau **global** (inafara oricarei clase).

Pentru new/delete definiti si global si in clasa, cel din clasa e folosit pentru elemente de tipul clasei, si in rest e folosit cel redefinit global.

```cpp
void *loc::operator new(size_t size){   
    void *p;  
    cout << "In overloaded new.\n";   
    p = malloc(size);  
    if(!p) { bad_alloc ba; throw ba; }
 return p;} 

void loc::operator delete(void *p){ 
     cout << "In overloaded delete.\n"; 
     free(p); 
}
```

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
### Pointeri catre functii
* Da, exista.
* La fct polimorfice, trebuie definit a.i. sa fie clar ce functie e.
  ```cpp
    int myfunc(int a); 
    int myfunc(int a, int b); 

    int main() 
    { 
        int (*fp)(int a); // !!! pointer to int f(int) 
        fp = myfunc; // points to myfunc(int) 
        cout << fp(5); 
        return 0; 
    } 

  ```

Constructori
---
* Constructor cu un parametru » conversie implicita
  ```
  X(int j){a=j}
  ...
  X ob = 99; // == X ob(99)
  ```
* vector de obiecte: merg initializate individual cu {X(param), X(param)} etc.
  * Obiecte globale : constructori apelati in ordinea definirii obiectelor
  * Destructori apelati in ordinea inversa definirii obiectelor
### De copiere
* cand pasez obiect in functie: pass-by-value, se apeleaza copy constructor
* cand ai alocare dinamica tre sa redefinesti copy constructor
* 

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
* Scope global/local cu :: :
    ```cpp
    int i; // global i 
    void f() 
    { 
        int i; // local i 
        i = 10; // uses local i
        ::i = 10; // now refers to global i 
    }
    ```
* clasa definita in functie:
  * nu acceseaza variabilele locale ale functiei
  * acceseaza variabilele statice
  * nu am voie sa definesc statice in clasa
* Eroare de compilare la overload(acelasi tip de date, desi nu pare  ):
   ```cpp
    void f(int *p);
    void f(int p[]); // error, *p is same as p[]

    void f(int x); // a aparut de 2 ori in curs
    void f(int& x);

   ```
* Ambiguitati dubioase la fct polimorfice:
  * intre char si unsigned char
  * intre fct cu param impliciti:
  ```cpp
    int myfunc(int i);
    int myfunc(int i, int j=1);

    int main()
    {
    cout << myfunc(4, 5) << " "; // unambiguous
    cout << myfunc(10); // ambiguous
    return 0;
    }
```
De cercetat
-------
* referinta vs pointer constant?
* union: curs 3 slideurile 25+