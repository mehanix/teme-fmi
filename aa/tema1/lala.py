def collatz(x,):
    if x == 1:
        return 0
    if x % 2 == 0:
        return 1 + collatz(x//2)
        
    return 1 +collatz(3*x+1)

m = {}
def collatz_iter(x):
    nr = 0
    # if x in m:
    #     return m[x]


    while x != 1:
        if x in m:
            nr+=m[x]
            break
        nr+=1
        if x % 2 == 0:
            x//=2
        else:
            x= 3*x+1
    m[x]=nr
    return nr


print(collatz_iter(3))
print(collatz_iter(6))
print(collatz_iter(3))