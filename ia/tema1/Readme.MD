# Tema 1 IA

## Cerinta

[Problema unui lacat, de aici](http://irinaciocan.ro/inteligenta_artificiala/exemple-teme-a-star.php)

## Rulare

### Recomandare
In `Makefile`, modifica parametrii, apoi `make run`.

### Sintaxa
`
python main.py -i path_to_input_folder -o path_to_output_folder -n NSOL -t TIMEOUT
`

Unde NSOL = numarul de solutii, TIMEOUT = in secunde.

### Exemple
```python
python main.py -i input -o output -n 2 -t 4
```


## Format fisier intrare:
```
Nume fisier: test_n.in, unde n e un numar

n siruri de caractere, fiecare cu k caractere din {d,g,i}, reprezentand cate o cheie
```
### Exemplu:
```
test_0.in

dgi
gid
gdi
```

## Euristici folosite

### Banala
```python
    if nod != self.scopuri:
        return 1
    return 0
```
Estimez costul ca fiind 1 daca nu am ajuns in starea scop, si 0 daca am ajuns. Astfel, o data ce se gaseste o solutie, ea va fi pusa la inceputul cozii pentru a putea fi afisata.
### Admisibila 1
```python
    return max([x.get() for x in nod])
```
Estimez costul ca fiind incuietoarea care a fost incuiata de cele mai multe ori in starea curenta. Aceasta euristica este admisibila deoarece stim sigur ca pentru o incuietoare de forma `i_n` este imposibil sa o descuiem cu mai putin de n mutari (o cheie poate descuia maxim 1 data).

Aceasta euristica face ca algoritmul sa prefere starile cu incuietori "cat mai descuiate".

### Admisibila 2
```python
    return min([x.get() for x in nod])
```
Aceasta euristica prefera starile care au macar 1 incuietoare descuiata, avand ca efect evitarea starilor care se indeparteaza de starea scop (de exemplu, dintre `i  d  i` si `i i2 i` voi prefera prima stare, care intr-adevar e mai aproape de solutie. )

### Neadmisibila
Euristica neadmisibila atribuie fiecarei stari un scor in functie de cate ori e incuiata fiecare portiune a lacatului. Acest scor reprezinta numarul de mutari estimat ca trebuie facute pentru a ajunge in starea scop.
De exemplu:

```
d  i  d  i  d  i -> scor 3

i3 d  i  d  d  d -> scor 4
```
Cu cat scorul e mai mic, cu atat starea este considerata ca fiind mai aproape de starea scop.
```
d  d  d  d  -> scor 0, si e stare scop
```
### Demonstratie ca este neadmisibila:
Fie nodul cu informatia:
```
i i d i -> scor 3
```
Euristica estimeaza ca voi folosi _3 chei_ pentru a ajunge la starea scop `d d d d `, deci _3 mutari_. h' = 3.

Fie fisierul de intrare ce contine cheia:
```
d d g d
```
Cu aceasta cheie, eu pot ajunge din nodul dat in nodul scop in _1 mutare_. h = 1

Cum in acest caz h' > h, rezulta ca euristica este neadmisibila.

