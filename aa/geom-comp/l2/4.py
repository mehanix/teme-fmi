import numpy as np 

eps = 1e-12
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

def th(x_a,y_a,x_b,y_b,x_c,y_c,x_d,y_d):

    theta = np.array([[x_a, y_a, x_a*x_a + y_a*y_a, 1],
                      [x_b, y_b, x_b*x_b + y_b*y_b, 1],
                      [x_c, y_c, x_c*x_c + y_c*y_c, 1],
                      [x_d, y_d, x_d*x_d + y_d*y_d, 1]])

    res =  np.linalg.det(theta)
    if -eps <= res <= eps:
        return 0
    else:
        return res


#citire
x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())
x_d = float(input())
y_d = float(input())

# verific AC => punctul D e in interiorul cercului circumscris ABC ?

res = th(x_a,y_a,x_b,y_b,x_c,y_c,x_d,y_d)
if  res > 0:
    print("AC muchie ilegala")

# verific BD => punctul C in interiorul cercului ABD ?

res = th(x_a,y_a,x_b,y_b,x_d,y_d,x_c,y_c)
if  res > 0:
    print("BD muchie ilegala")