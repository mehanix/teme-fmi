import numpy as np
puncte = []

def testeaza_viraj(P,Q,R):
    a = np.array([[1, 1,  1],
                [P[0],Q[0],R[0]],
                [P[1],Q[1],R[1]]])

    det_a = np.linalg.det(a)
    
    if det_a == 0:
        return det_a
    elif det_a > 0:
        return 1
    else:
        return -1


def pe_segment(a,b,c):
    return min(a[0],b[0]) <= c[0] <= max(a[0],b[0]) \
           and \
           min(a[1],b[1]) <= c[1] <= max(a[1],b[1])

def intersecteaza(a,b,c,d):
    d1 = testeaza_viraj(c,d,a)
    d2 = testeaza_viraj(c,d,b)
    d3 = testeaza_viraj(a,b,c)
    d4 = testeaza_viraj(a,b,d)

    
    # daca intersecteaza e ok
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    
    # daca e pe segment e ok

    return (d1 == 0 and pe_segment(c,d,a)) or \
           (d2 == 0 and pe_segment(c,d,b)) or \
           (d3 == 0 and pe_segment(a,b,c)) or \
           (d4 == 0 and pe_segment(a,b,d))

            


def e_in_poligon(n, puncte, Q):
    if n<3: # trebuie minim 3 pct pt un poligon
        return False

    # aleg punct pe 0x)
    R = (10**9,Q[1])
    nr = 0
    #primul punct din poligon
    a = 0
    b = 1
    A = puncte[a]
    B = puncte[b]
    nr_muchii = 0
    while b!=0:
        A = puncte[a]
        B = puncte[b]
        #daca ab intersecteaza pq
        if(intersecteaza(A,B,Q,R)):
            nr_muchii +=1
            if pe_segment(A,B,Q):
                return True
        a=b
        b = (a+1) % n
    return nr_muchii % 2 == 1

    
n = int(input())

for i in range(n):
    x = int(input())
    y = int(input())
    puncte.append((x,y))

q_x = int(input())
q_y = int(input())

print(e_in_poligon(n, puncte,(q_x,q_y)))