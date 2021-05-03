import math

# cu asta iterez stg -> dr
def iter(i,nr):
    while True:
        yield i
        i = (i+1) % nr

# citesc punctele si retin punctul cel mai din stg si din dreapta pe OX
# si cel mai sus,jos pt oy
min_x = min_y = math.inf
max_x = max_y = -math.inf
leftmost = None
rightmost = None
top = None
bottom = None
n = int(input())

# punctele s date in sens trigonometric
puncte = []
for i in range(n):
    x = int(input())
    y = int(input())
    if x > max_x:
        rightmost = i
        max_x = x
    if x < min_x:
        leftmost = i
        min_x = x
    
    if y < min_y:
        min_y = y
        bottom = i
    
    if y > max_y:
        max_y = y
        top = i

    puncte.append((x,y))

print(puncte)

# PENTRU X
#incep din stanga
ok = True

k = iter(leftmost,n)
a = next(k)
b = next(k)
while a != rightmost and ok: # pana am completat lantul
    print(a,b)

    # x-urile trb sa fie mereu in crestere
    if not puncte[a][0] < puncte[b][0]:
        ok = False
    a = b
    b = next(k)


print()
while a != leftmost and ok:
    print(a,b)

    # x-urile trb sa fie mereu in descrestere acum
    if not puncte[a][0] > puncte[b][0]:
        ok = False
    a = b
    b = next(k)
print("x-monoton:",ok)


# PENTRU Y
#incep de jos
ok = True

k = iter(bottom,n)
a = next(k)
b = next(k)
while a != top and ok: # pana am completat lantul
    print(a,b)

    # y-urile trb sa fie mereu in crestere
    if not puncte[a][1] < puncte[b][1]:
        ok = False
    a = b
    b = next(k)


print()
while a != bottom and ok:
    print(a,b)

    # y-urile trb sa fie mereu in descrestere acum
    if not puncte[a][1] > puncte[b][1]:
        ok = False
    a = b
    b = next(k)
print("y-monoton:",ok)