Descrierea solutiilor - Tema 3 SD
---

## Sortari, Cautari, SDO

### Numarare triunghiuri - _cautare binara_

(in cate moduri pot alege 3 betisoare a.i. sa se poata forma un triunghi cu ele)

* sortez vectorul, le iau cate 2 si le fac suma.
* cautare binara pentru cel mai mare numar < v[i] + v[j] (din criteriul: suma a 2 laturi > a treia.).
* cum vectorul e sortat crescator, daca poz nr gasit != j => toate numerele din intervalul (j,c) formeaza triunghi valid asa ca le adun la suma.
Complexitate: N^2logn

### Factorial - _cautare binara_, _legendre_

(se da P. sa se gaseasca cel mai mic nr natural strict pozitiv N a.i. N! are exact P de 0 la sfarsit)

* formula lui legendre - folosita pt a gasi a=5^x a.i. a divide N!.
* citesc numarul p, si pe intervalul [0,p*5] fac cautare binara, unde:
  * iau nr nou si ii calculez cati de 0 are folosind legendre
  * daca are prea multi, ma duc in stanga, daca are prea putini in dreapta, daca are = tin minte unde l-am gasit si caut cel mai din stanga nr care indeplineste conditia.
  
Complexitate: Nlogn

### Cautare binara

* cea mai mare poz sau -1: 
  * variabila _last_=-1, odata ce gasesc elem. ii salvez pozitia in last si continui sa ma duc in dreapta(mid=left+1)
* cea mai mare pozitie cu valoare <= x:
  * last = -1
    * cand gasesc <= ii salvez pozitia si ma duc in dreapta
* cea mai mica pozitie cu valoare >=x:
  * last = -1
  * cand gasesc >= ii salvez pozitia si ma duc in stanga

### Drazil and Factorial 

* problema asta nu stiu daca asa trebuia facuta, eu am facut-o efectiv cu niste observatii de mate:
  * practic descompun cifrele:
    * numerele prime raman nr prime(2,3,5,7)
    * 4! = 3! * 2! * 2!
    * 6! = 5! * 3!
    * 8! = 7! * 2! * 2! * 2!
    * 9! = 7! * 3! * 3! * 2!
  * Descompunerea asta merge pt ca vreau cel mai mare nr => vreau cat mai multe cifre si cat mai mari
  * Nr merg descompuse pana la primul nr prim
  * Numar cate apar si le afisez in ordine descrescatoare si aia e.
  
### Sum of Odd Integers 