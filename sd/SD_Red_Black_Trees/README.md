# SD_Red_Black_Trees
Tema 2 la Structuri de Date, anul I UniBuc

## Cerinta temei 
Sa se implementeze urmatoarele operatii:
* Cautare 
* inserare 
* ștergere 
* succesor
* predecesor
* afisare elemente sortat

## Despre Red Black Trees

Un Red-Black tree este un **arbore binar de cautare echilibrat**. El garanteaza operatiile de *cautare, predecesor, succesor, minim, maxim, insert, delete* in timp logaritmic.

In arborii rosii-negri, pe langa informatiile obisnuite tinute in nod (informatie, parent, left, right) vom avea si un bit de **culoare** (0 negru, 1 rosu).

### Reguli

Arborii rosii-negri trebuie sa respecte urmatoarele reguli:

1. Orice nod e ori rosu, ori negru.
2. Nodul ROOT trebuie sa fie mereu negru.
3. Frunzele trebuie sa fie mereu negre (pentru asta folosim santinela T.nil)
4. Daca un nod e rosu, ambii copii ai lui vor fi negri.
5. Pt fiecare nod, toate path-urile simple de la nod la o frunza contin acelasi nr de noduri negre. (Black Height)

### Rotatii

Cand ai operatii care modifica structura tree-ului (adaugare, stergere nod) exista riscul ca dupa o astfel de operatie tree-ul sa nu mai respecte regulile. Astfel, dupa o operatie, arborele trebuie **rebalansat**. 

Pentru a il rebalansa, fac operatia de *rotatie* la stanga sau la dreapta. Aceasta operatie se face in O(1) (doar mut niste pointeri).


Exemplu: Left-Rotate x
* Am nodul parinte X si nodul Y, fiu de dreapta al lui X. Aplic operatia de left rotate:
* subtree-ul dreapta al lui Y ramane pe loc.
* subtree-ul stanga al lui Y devine subtree dreapta pentru X.
* Y devine parent, X devine fiu stanga pentru Y

La fel si pentru Right Rotate, cu l/r flipped.


### Inserarea

Putem insera un nod in RB tree in O(log n). Inseram un nod in tree, si il coloram cu rosu.
Pentru ca asta ar putea crea o configuratie care incalca regulile unui RB tree corect, trebuie sa recoloram graful.

Algoritmul de recolorare pentru insert functioneaza asa: (z nodul nou)

1. daca unchiul lui z e rosu => colorez unchiul si parintele negru. urc in tree cu z = z.p.p si repet cat timp e nevoie
2. daca unchiul lui z e negru si z e fiu dreapta => fac left rotate. z devine fiu stanga. aplic cazul 3.
3. unchiul lui z e negru si z fiu stanga => unchiul lui z e negru(de la cazul 1). asadar, fac right rotate si recolorare a.i. nu mai am 2 noduri rosii unul dupa altul.
4,5,6:la fel ca 1,2,3 dar mirrored left cu right.

