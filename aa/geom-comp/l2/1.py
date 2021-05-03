
def testeaza_viraj(P,Q,R):
    a = np.array([[1, 1,  1],
                [P[0],Q[0],R[0]],
                [P[1],Q[1],R[1]]])

    det_a = np.linalg.det(a)

    if det_a == 0:
        return "pe dreapta"
    elif det_a < 0:
        return "viraj dreapta"
    return "viraj stanga"


def e_in_poligon(n, puncte, q):
    if n<3: # trebuie minim 3 pct pt un poligon
        return False

    # aleg punct pe 0x)
    q = (10**9,q[1])
    nr = 0
    #primul punct din poligon
    a = 0

    while True:
        #al 2lea punct din poligon
        b = (i+1) % n

        #daca ab intersecteaza pq
        if(intersecteaza(a,b,p,q))

n = int(input())

puncte = []
for i in range(n):
    x = int(input())
    y = int(input())
    puncte.append((x,y))

q_x = int(input())
q_y = int(input())

print(e_in_poligon(n, puncte,(q_x,q_y)))