import math
from p1 import testeaza_viraj
def iter(i,nr):
    while True:
        yield i
        i = (i+1) % nr

def iter_rev(i,nr):
    while True:
        yield i
        i = i-1
        if i < 0:
            i = nr-1
    

def cautbin(pct,L,sens):
    segmente = []
    if sens == 1:
        segmente = [[L[i],L[i+1]] for i in range(len(L)-1)]
    else:
        segmente = [[L[i],L[i-1]] for i in range(len(L)-1,0,-1)]
    st = 0
    dr = len(segmente)-1

    while st <= dr:
        mid = (st+dr)//2

        if segmente[mid][0][0] <= pct[0] and pct[0] <= segmente[mid][1][0]:
            if sens == 1:
                return segmente[mid]
            else:
                rev = [segmente[mid][1], segmente[mid][0]]
                return rev
        elif segmente[mid][1][0] < pct[0]:
            st = mid+1
        else:
            dr = mid-1
    return -1,-1 # e clar inafara poligonului



if __name__ == "__main__":
    with open("p2.in") as f:
        nr = int(f.readline().strip())
        lista_puncte = []
        leftmost = -1
        rightmost = -1
        min_x = math.inf
        max_x = -math.inf
        for i in range(nr):
            p = [int(x) for x in f.readline().strip().split()]
            print(p)
            lista_puncte.append(p)

            if p[0] < min_x:
                leftmost = i
                min_x = p[0]
            if p[0] > max_x:
                rightmost = i
                max_x = p[0]

        punct = [0,0]
        print("punct:")
        punct[0] = float(input())
        punct[1] = float(input())
        # frontiera inferioara        
        k = iter(leftmost,nr)
        Li = [lista_puncte[next(k)],lista_puncte[next(k)]]
        i = next(k)
        while i != leftmost: # pana am completat poligonul
            Li.append(lista_puncte[i])
            while len(Li) > 2 and testeaza_viraj(Li[-3],Li[-2],Li[-1]) != "viraj stanga":
                Li.remove(Li[-2])
            i = next(k)
        print("Frontiera inferioara:",Li)
        # frontiera superioara, merg invers
        k = iter_rev(rightmost,nr)
        Ls = [lista_puncte[next(k)],lista_puncte[next(k)]]
        i = next(k)
        while i != rightmost: # pana am completat poligonul
            Ls.append(lista_puncte[i])
            while len(Li) > 2 and testeaza_viraj(Ls[-3],Ls[-2],Ls[-1]) != "viraj stanga":
                Ls.remove(Ls[-2])
            i = next(k)
        print("Frontiera superioara:",Ls)

        # caut binar pe Li, Ox segmentul care delimiteaza punctul cel mai bine
        P,Q = cautbin(punct,Li,1)
        if P == -1 and Q == -1: # clar inafara
            print("exterior")
        else:        
            raspuns_li = testeaza_viraj(P,Q,punct)

            # caut binar pe Ls, Ox segmentul care delimiteaza punctul cel mai bine
            P,Q = cautbin(punct,Ls,-1)
            raspuns_ls = testeaza_viraj(P,Q,punct)

            if raspuns_li == raspuns_ls == "viraj stanga":
                print("interior")
            elif raspuns_li == "pe dreapta" or raspuns_ls == "pe dreapta":
                print("pe laturi")
            else:
                print("exterior")
            