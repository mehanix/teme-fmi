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

        
        # frontiera inferioara        
        k = iter(leftmost,nr)
        Li = [lista_puncte[next(k)],lista_puncte[next(k)]]
        i = next(k)
        while i != leftmost: # pana am completat poligonul
            Li.append(lista_puncte[i])
            print(Li)
            while len(Li) > 2 and testeaza_viraj(Li[-3],Li[-2],Li[-1]) != "viraj stanga":
                Li.remove(Li[-2])
            i = next(k)
        print(Li)
        print()
        # frontiera superioara, merg invers
        k = iter_rev(rightmost,nr)
        Ls = [lista_puncte[next(k)],lista_puncte[next(k)]]
        i = next(k)
        while i != rightmost: # pana am completat poligonul
            Ls.append(lista_puncte[i])
            print(Li)
            while len(Li) > 2 and testeaza_viraj(Ls[-3],Ls[-2],Ls[-1]) != "viraj stanga":
                Ls.remove(Ls[-2])
            i = next(k)
        print(Ls)

        print (Li[:-1] + Ls[:-1])