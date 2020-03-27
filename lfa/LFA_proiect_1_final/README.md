# LFA_proiect_1
Tema 1 la Limbaje Formale si Automate, Anul 1 UniBuc

![screenshot-proiect](https://i.imgur.com/860BKjs.png)
![screenshot-generare](https://i.imgur.com/HoAyPyp.png)

## Cerinta temei
1) Sa se scrie un program care incarca in memorie un DFA/NFA, apoi verifica daca automatul accepta cuvintele date de utilizator.

2) Sa se genereze cele mai scurte 100 cuvinte acceptate de automat.

## Implementare
Am folosit o structura de date custom pentru a salva graful in memorie. (vector de map(lista de noduri), care mapeaza literele alfabetului la vectori cu directiile unde poti pleca din acel nod) `vector<map<char,vector<int>>>`

Am mai folosit si o matrice de vizitati, unde tineam evidenta drumului meu curent, pentru a evita sa ma duc de 2 ori cu aceeasi lungime curenta inspre acelasi nod. `vector<vector<bool>>, unde nr_linii = nr_noduri, si nr_coloane = word.length()`

Verificarea apartenentei unui cuvant in automat este un DFS, practic.

Generarea celor mai scurte cuvinte se face cu algoritmul BFS si cu un queue in care tin drumurile gasite. La fiecare pas, scot drumul curent din coada, iau ultimul element, si daca nu este element final, verific unde pot sa plec din el, si adaug la sfarsitul cozii noile drumuri create.

Totodata, folosesc matricea de vizite pentru a avea grija sa nu ma blochez in bucle.

## Features
* Incarcare automat custom din fisierul automat_custom.in
* Incarcare automat generat (cel cu 3004 noduri si 2002002 muchii) pentru a demonstra functionalitatea matricii de vizitati
* Testarea cuvintelor in automat
* Generarea cele mai scurte 100 cuvinte acceptate de automat

## Structura fisier intrare
```
numar_noduri
numar_muchii
nod_x nod_y caracter (de numar_muchii ori)
nod_start
numar_noduri_finish
nod_finish_x (de numar_noduri_finish ori)
```
