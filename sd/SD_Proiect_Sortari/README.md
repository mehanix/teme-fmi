# SD_Proiect_Sortari
Tema 1 la Structuri de Date, Anul I Info UniBuc

![header-img](https://i.imgur.com/5q7HlKk.png)
> test input: 10^7 elemente din intervalul [0, 10^7)

## Cerinta temei
Sa se scrie un program care sorteaza un vector de numere folosind urmatoarele sort-uri:
* STL Sort
* Bubble Sort
* Merge Sort
* Radix Sort
* Quick Sort
* Count Sort

In plus, programul trebuie sa:
* Cronometreze timpul fiecarei sortari
* Verifice daca sortarea s-a facut corect
* Impuna conditii de eroare pentru sortarile care au nevoie de ele
  * Bubble sort: sa nu sorteze vectorii cu numar prea mare de elemente (avand complexitate O(n^2))
  * Count sort: sa nu sorteze vectorii cu elemente prea mari (deoarece foloseste memorie aditionala pentru a crea un vector caracteristic cu max(v) elemente)

## Implementare
**Generare**: Pentru fiecare test, generez un vector de nr_elem elemente, in intervalul [0,val_max).

**Cronometrare**: Cronometrez timpul cu biblioteca `chrono`. Iau timpul de inceput, de sfarsit, le scad si afisez durata in *milisecunde*.

**Quick sort**: Varianta recursiva. Include 2 moduri de alegere a pivotului:
* Ultimul element din vector
* Mediana din 3

Optimizat folosind separarea in 3 subliste: elemente < pivot, elemente = pivot, si elemente > pivot, apelul recursiv facandu-se apoi doar pe elementele mai mici strict decat pivotul(in stanga), respectiv mai mari strict decat pivotul(in dreapta).

Algoritmul de partitionare folosit este o versiune modificata a algoritmului lui Lomuto, gasit in [Introduction to Algorithms - Cormen, pagina 171](https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf).

**Radix sort**:Varianta standard, zic eu. Implementata cu Count Sort in spate, fara operatii pe biti, dar cu baza usor modificabila. Astfel, includ si compar urmatoarele variante de Radix:
* Baza 10
* Baza 256

**Bubble Sort, Merge Sort, Count Sort**: Implementare obisnuita, fara optimizari.

## Ce am observat pe parcursul proiectului

1.  _Impartirea in 3 liste_ are un impact foarte mare asupra performantei quick sort-ului, mai mare decat mediana din 3 in testele facute de mine.
2. Optimizarea merge sort-ului a fost o experienta interesanta:
  * Initial, la pasul de merge, eu cream cate un `vector<int>` nou pentru Left si Right, copiam valorile in el, apoi interclasarea o faceam direct in vectorul original, suprascriind valorile vechi.
     - Acest approach avea o performanta muult sub cea a Quick Sort-ului, si nu intelegeam de ce.
     - Facand research, am aflat ca nesetand dimensiunea asteptata a vectorului ( cu `v.reserve()`), atunci cand adaugam elemente in L si R, programul trebuia sa redimensioneze vectorul, iar asta adauga foarte mult la timpul de executie.
  *  Am obtinut performanta mai buna la Merge Sort in varianta in care in pasul de merge:
      * Creez un vector nou de lungime `right - left + 1`
      * cu i de la left->mid, si j de la mid+1->right, interclasez valorile vectorului vechi
      * copiez valorile inapoi in vectorul original.
  * In viitor, ar trebui sa optimizez si copierea in vectorul original (ceva cu pointeri?) pentru performanta si mai buna.
3. Python merge fooarte greu, chiar si cu pypy3. Acest proiect a fost scris original in Python, iar acea sursa se poate gasi aici. Nu m-a multumit, asa ca l-am rescris in C++.

## Format fisier intrare
```
nr_teste
nr_elemente1 val_max1
nr_elemente2 val_max2
...
```
## Timpi scosi
![time](https://i.imgur.com/hqQ8ATC.png)
