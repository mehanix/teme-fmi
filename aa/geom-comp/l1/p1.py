import numpy as np 

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

if __name__ == "__main__":
    P = [0,0]
    Q = [0,0]
    R = [0,0]

    print("P_x=")
    P[0] = float(input())
    print("P_y=")
    P[1] = float(input())
    
    print("Q_x=")
    Q[0] = float(input())
    print("Q_y=")
    Q[1] = float(input())
    
    print("R_x=")
    R[0] = float(input())
    print("R_y=")
    R[1] = float(input())

    print(testeaza_viraj(P,Q,R))



