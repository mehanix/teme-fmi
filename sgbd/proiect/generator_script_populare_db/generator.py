# generez inserturile cu care voi popula baza de date

from pathlib import Path
import random
import time
import datetime
#### Clienti ####
nume = Path("nume.txt").read_text().split('\n');
prenume = Path("prenume.txt").read_text().split('\n');

clienti = []
piese = []
genuri = []
artisti = []
case_discuri = []
albume = []
index = 1;
for n in nume:
    for p in prenume:
        index+=1
        clienti.append([index,n,p,random.randint(16,40)])



### Piese ###
# generez titlu (1-3 cuvinte) si durata
d_piese = Path("piese.txt").read_text().split('\n');


numar_piese = 200
while numar_piese > 0:
    numar_piese-=1;
    numar_cuvinte=random.randint(1,4);
    titlu = ""
    while numar_cuvinte > 0:
        titlu += random.choice(d_piese) + " ";
        numar_cuvinte-=1;
    titlu.strip();
    index+=1
    numar_piese-=1
    piese.append([index,titlu,random.randint(2,6)])
print(piese)


### Genuri muzicale ###

d_genuri = Path("genuri.txt").read_text().split('\n');
for g in d_genuri:
    index+=1
    genuri.append([index, g]);
    
### Case de discuri ###

d_case =Path("case_discuri.txt").read_text().split('\n'); 
for c in d_case:
    index+=1
    case_discuri.append([index, c]);

### Artisti ###

d_artisti = Path("artisti.txt").read_text().split('\n');
for a in d_artisti:
    index+=1
    artisti.append([index, a]);

### Albume ###

d_albume = Path("albume.txt").read_text().split('\n');
for a in d_artisti:
    index+=1
    #id, id_casa, id_gen, nume, pret, an
    albume.append([index,random.choice(case_discuri)[0],random.choice(genuri)[0], a, random.randint(10,100), random.randint(1965,2019)]);

### Comenzi ###
nr_comenzi = 50
comenzi = []
while nr_comenzi>0:
    index+=1
    now = datetime.datetime.now()
    comenzi.append([index,random.choice(clienti)[0],now.strftime('%Y-%m-%d %H:%M:%S')])

    nr_comenzi-=1



### Album_Artist ###
# un album poate fi compus de 1-3 artisti
album_artist = []
for album in albume:
    nr_albume = random.randint(1,3);
    while nr_albume > 0:
        index+=1
        album_artist.append([index,album[0],random.choice(artisti)[0]])
        nr_albume-=1

## Comanda_Album ###
# o comanda poate contine mai multe albume
# id_album_comanda, id_comanda, id_album
comanda_album = []
for comanda in comenzi:
    # o comanda poate avea intre 1 si 5 albume
    nr_albume = random.randint(1,5)
    while nr_albume > 0:
        index+=1
        comanda_album.append([index,comanda[0],random.choice(albume)[0]])
        nr_albume-=1

### Album_Gen ###
#id album_gen, id_album, id_gen
album_gen = []
for album in albume:
    nr_genuri = random.randint(1,3)
    while nr_genuri > 0:
        index+=1
        nr_genuri=-1
        album_gen.append([index,album[0],random.choice(genuri)[0]])

with open("output.txt",'a') as output:
    for c in clienti:
        output.write("INSERT INTO Clienti (id_client, nume, prenume, varsta) VALUES ({0}, {1}, {2});\n".format(c[0],c[1],c[2]));
    for p in piese:
        output.write("INSERT INTO Piese (id_piesa, titlu, durata) VALUES ({0}, {1}, {2});\n".format(p[0],p[1],p[2]));
    for g in genuri:
        output.write("INSERT INTO Genuri (id_gen, denumire) VALUES ({0}, {1});\n".format(g[0],g[1]));
    for c in case_discuri:
        output.write("INSERT INTO Case_Discuri (id_casa, denumire) VALUES ({0}, {1});\n".format(c[0],c[1]));
    for a in artisti:
        output.write("INSERT INTO Artisti (id_artist, nume) VALUES ({0}, {1});\n".format(a[0],a[1]));
    for a in albume:
        output.write("INSERT INTO Albume (id_album, id_casa, id_gen, titlu, pret, an_aparitie) VALUES ({0}, {1}, {2}, {3}, {4}, {5});\n".format(a[0],a[1],a[2],a[3],a[4],a[5]))
    for aa in album_artist:
        output.write("INSERT INTO Album_Artist (id_album_artist, id_album, id_artist) VALUES ({0}, {1}, {2});\n".format(aa[0],aa[1],aa[2]))
    for ca in comanda_album:
        output.write("INSERT INTO Comanda_Album (id_comanda_album, id_comanda, id_album) VALUES ({0}, {1}, {2});\n".format(ca[0],ca[1],ca[2]))
    for ca in comanda_album:
        output.write("INSERT INTO Album_Gen (id_album_gen, id_album, id_gen) VALUES ({0}, {1}, {2});\n".format(ca[0],ca[1],ca[2]))
