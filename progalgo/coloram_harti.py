# backtracking eeww
# coloram harti

def valid(k):
    touches = adiacente[k]
    # sprint(k, touches)
    # print(touches)
    for t in touches:
        if t<=k:
            if st[k] == st[t]:
                return False

    return True

def solutie(k):
    return k==6


def back(k):

    for i in range(1,5):  # trec prin toate culorile
        st[k] = i


        if valid(k):  # daca nu exista 2 tari cu aceeasi culoare

            if solutie(k): # daca sunt toate tarile colorate
                print(st[1:])
            else:
                back(k + 1)


with open("tis.txt", "r") as f:
    txt = [t.strip() for t in f.readlines()]
    nr_culori = int(txt[0])
    atingeri = [tuple(int(x) for x in t.split(' ')) for t in txt[1:]]

    adiacente = {}
    for tara_1, tara_2 in atingeri:
        if tara_1 not in adiacente:
            adiacente[tara_1] = set()
        if tara_2 not in adiacente:
            adiacente[tara_2] = set()
        adiacente[tara_1].add(tara_2)
        adiacente[tara_2].add(tara_1)

    print("adiac", adiacente)
    st = [0] * (len(adiacente.keys()) + 1)
    back(1)
