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
    print(theta)
    res =  np.linalg.det(theta)
    if -eps <= res <= eps:
        return 0
    else:
        return res

x_a = int(input())
y_a = int(input())
x_b = int(input())
y_b = int(input())
x_c = int(input())
y_c = int(input())
x_d = int(input())
y_d = int(input())

semn = 1

if not testeaza_viraj((x_a,y_a), (x_b,y_b), (x_c,y_c)) == "viraj stanga":
    semn = -1


res = th(x_a,y_a,x_b,y_b,x_c,y_c,x_d,y_d) * semn
print(res)
if  res > 0:
    print("inauntru")
elif res == 0:
    print("pe cerc")
else:
    print("in afara")