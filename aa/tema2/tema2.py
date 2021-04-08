# format input:
# dimensiune_pop
# a b (capetele domeniului de definitie)
# a b c (coeficientii polinomului de grad 2)
# p (nr zecimale precizie)
# p_recombinare (probabilitate recombinare)
# p_mutatie (probabilitate mutatie)
# nr_etape (nr etape algoritm)
import random, math, copy


##### Functii #####

# returneaza 1 bit random
def random_bit():
    x = random.random()
    if x <0.5:
        return 1
    return 0

# genereaza cromozom de lungime length
def generate_chromosome(length):
    return [random_bit() for y in range(length)]

# genereaza prima populatie
def generate_random_population():
    # random.seed(10) # for testing
    tmp = [ generate_chromosome(lungime_cromozom) for x in range(dimensiune_pop)]
    return tmp

# functia de fitness e chiar functia data de noi
def fct(x):
    #return coef_functie[0]*x*x + coef_functie[1]*x + coef_functie[2]
    return x*x*x + 3*(x*x) - 4*x + 7

# cromozom = x in baza 2
# translatez in 10
def get_x(cromozom):

    x = 0
    for bit in cromozom:
        x = (x << 1) | bit

    return (dom_definitie[1]-dom_definitie[0])/(pow(2,lungime_cromozom))*x+dom_definitie[0]

# returneaza lista cu toate valorile cromozomilor, trecute prin functia de fitness
def get_all_values(populatie):
    return [fct(get_x(ch)) for ch in populatie]

# print cromozom (baza 2)
def p_cromozom(lst):
    return "".join(map(str,lst))

# afiseaza populatia
def print_population(populatie):
    if iteratie == 1:
        for i in range(1,len(populatie)+1):
            x = get_x(populatie[i-1])
            fl.write(str(i) + ": ")
            fl.write(p_cromozom(populatie[i-1]) + ", x=")
            fl.write('{: f}, '.format(x))
            fl.write(str(fct(x)))
        
            fl.write('\n')
        fl.write('\n\n')
    return

# returneaza array cu prob de selectie
def get_prob_selectie(populatie):

    valori_cromozomi = get_all_values(populatie)
    F = sum(valori_cromozomi)
    tmp = []
    for f_x in valori_cromozomi:
        # favorabil / posibil = probabilitate
        tmp.append(f_x/F)

    if iteratie == 1:
        fl.write("Probabilitati selectie:\n")
        for i in range(1,dimensiune_pop+1):
            fl.write("Cromozom " + format(i,'3') +' -> probabilitate: ' + str(tmp[i-1]) + '\n')
        fl.write("\n\n")
    return tmp
    
#transforma probabilitatile de selectie in intervale de selectie
def get_intervale_selectie(prob_selectie):
    tmp = []
    s = 0
    for p in prob_selectie:
        tmp.append(s) 
        s+= p 
    tmp.append(1.0)

    if iteratie == 1:
        fl.write("Intervale probabilitati selectie:\n")
        for t in tmp:
            fl.write(str(t) + ' ')
        fl.write("\n\n")
    return tmp

def metoda_ruletei():
    pop = []
    for i in range(1,dimensiune_pop+1):
        # aleg nr random intre [0,1] si gasesc intervalul in care se incadreaza si adaug cromozomul asociat intervalului in populatia noua
        u = random.random()
        v = random.random()
        j=1
        k=1
        while not(intervale_prob_selectie[j-1] <= u and u <= intervale_prob_selectie[j]):
            j+=1
        while not(intervale_prob_selectie[k-1] <= v and v <= intervale_prob_selectie[k]):
            k+=1
        
        if fct(get_x(populatie[j-1])) > fct(get_x(populatie[k-1])):
            if iteratie == 1:
                fl.write("u=" + str(u) + " selectam cromozomul " + str(j)+"\n")
            pop.append(copy.deepcopy(populatie[j-1]))
            
        else:
            if iteratie == 1:
                fl.write("v=" + str(v) + " selectam cromozomul " + str(k)+"\n")
            pop.append(copy.deepcopy(populatie[k-1]))               

    return pop

def get_crossover_candidates(populatie,p_recombinare):
    # aleg nr random intre [0,1] pt fiecare dintre cromozomi si daca nr < probabilitate_recombinare atunci il adaug in lista de cromozomi ce vor fi recombinati
    tmp = []
    for i in range(1,dimensiune_pop+1):
        sansa = random.random()
        msg = ""
        msg +=(str(i) + ": ")
        msg+=(p_cromozom(populatie[i-1]) + ", u=")
        msg+=(str(sansa))
        if sansa < p_recombinare:
            tmp.append(i-1)
            msg+="<" + str(p_recombinare) + " participa"
        if iteratie == 1:
            fl.write(msg + '\n')
    return tmp

def crossover(candidates):
    fl.write('\n')
    rezultat_1 = []
    rezultat_2 = []
    while len(candidates)>=2:
        # iau 2 cromozomi din cei alesi la etapa anterioara
        sample = random.sample(candidates,2)
        candidates.remove(sample[0])
        candidates.remove(sample[1])

        # aleg pct rupere random
        pct_rupere = random.randrange(0,lungime_cromozom)
        if iteratie == 1:
            fl.write("Recombinare dintre cromozomul {0} cu cromozomul {1}:\n".format(sample[0]+1,sample[1]+1))
            fl.write("{0} {1} punct {2}\n".format(p_cromozom(new_pop[sample[0]]),p_cromozom(new_pop[sample[1]]),pct_rupere))

        # combin bucatile
        rezultat_1 = new_pop[sample[0]][:pct_rupere] + new_pop[sample[1]][pct_rupere:]
        rezultat_2 = new_pop[sample[1]][:pct_rupere] + new_pop[sample[0]][pct_rupere:]

        if iteratie == 1:
            fl.write("Rezultat: {0} {1}\n\n".format(p_cromozom(rezultat_1),p_cromozom(rezultat_2)))
        new_pop[sample[0]] = rezultat_1
        new_pop[sample[1]] = rezultat_2        
    return

def mutate():
    if iteratie == 1:
        fl.write("\nProbabilitatea de mutatie {0}:\nAu fost modificati cromozomii:\n".format(p_mutatie))
    for i in range(dimensiune_pop-1):
        #aleg nr random
        u = random.random()
        #daca e mai mic decat prob_mutatie
        if u < p_mutatie:
            if iteratie == 1:
                fl.write(str(i+1) + ' ')
            # iau un bit random si-l flipuiesc
            poz = random.randrange(0,lungime_cromozom-1)
            new_pop[i][poz] = abs(new_pop[poz][i]-1)
    if iteratie == 1:
        fl.write('\n')
    return

# ia cromozomul cel mai fit(index)
def get_fittest(populatie):
    ind = 0
    maxx = fct(get_x(populatie[0]))
    for i in range(len(populatie)):
        f_x = fct(get_x(populatie[i]))
        if f_x > maxx:
            ind = i 
            maxx = f_x
    return ind

# ia cromozomul cel mai putin fit (index)
def get_least_fit(populatie):
    ind = 0
    minn = fct(get_x(populatie[0]))
    for i in range(len(populatie)):
        f_x = fct(get_x(populatie[i]))
        if minn > f_x:
            ind = i 
            minn = f_x

    return ind

def criteriu_elitist():
    # gasit indicii celui mai bun respectiv prost cromozom si inlocuit
    ind_fittest_old_pop = get_fittest(populatie)
    ind_least_fit_new_pop = get_least_fit(new_pop)

    new_pop[ind_least_fit_new_pop] = copy.copy(populatie[ind_fittest_old_pop])
    return


##### END functii #####

## citire date

print("Computing, please wait...")
fl = open("Evolutie.txt","w")
with open("input.txt") as f:
    lines = f.read().splitlines()

dimensiune_pop = int(lines[0])
dom_definitie = [int(x) for x in lines[1].split()]
coef_functie = [int(x) for x in lines[2].split()]
precizie = int(lines[3])
p_recombinare = float(lines[4])
p_mutatie = float(lines[5])
nr_etape = int(lines[6])
iteratie = 1

# calculez lungimea cromozomului
# discretizez intervalul in (b-a)*10^precizie subintervale
lungime_cromozom = math.floor(math.log((dom_definitie[1] - dom_definitie[0])*(math.pow(10,precizie)), 2))


## PAS 1: generat aleator cromozomi
populatie = generate_random_population()
if iteratie == 1:
    fl.write("Populatia initiala:\n")
    print_population(populatie)

while iteratie <=nr_etape:
    ## PAS 2: afla probabilitatile de selectie pt fiecare cromozom
    prob_selectie = get_prob_selectie(populatie)

    ## PAS 3: afla intervale prob selectie
    intervale_prob_selectie = get_intervale_selectie(prob_selectie)

    ## PAS 4: aplica metoda ruletei
    new_pop = metoda_ruletei()

    if iteratie == 1:
        fl.write("\nDupa selectie:\n")
        print_population(new_pop)

    ## PAS 5: selecteaza pt incrucisare
    index_cr_incrucisare = get_crossover_candidates(new_pop,p_recombinare)

    ## PAS 6: Incrucisez
    crossover(index_cr_incrucisare)

    ## PAS 7: Dupa recombinare
    if iteratie == 1:
        fl.write("\nDupa recombinare:\n")
        print_population(new_pop)

    ## PAS 8: Mutatie
    mutate()
    if iteratie == 1:
        fl.write("Dupa mutatie: \n")
        print_population(new_pop)

    ## PAS 9: Criteriu elitist
    # vreau sa inlocuiesc cel mai bun cromozom din pop initiala cu cel mai prost din populatia noua
    criteriu_elitist()

    if iteratie == 1:
        fl.write("Dupa aplicarea criteriului elitist: \n")
        print_population(new_pop)

    ## PAS 10: Observ evolutia maximului

    # aplic pe populatia noua functia care mi da indicele maximului
    # iau elem din lista, il transform in baza 10 si apoi aplic fct de fitness pe el
    if iteratie == 1:
        fl.write("Evolutia maximului: \n")
    fl.write(str(get_x(new_pop[get_fittest(new_pop)])) +' ' + str(fct(get_x(new_pop[get_fittest(new_pop)]))))
    ## PAS 11: Ma pregatesc pt urmatoarea iteratie
    iteratie+=1
    populatie = copy.deepcopy(new_pop)

    ## Done! 
print("Done!")
