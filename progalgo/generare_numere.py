#generam numere cu cifre distincte si suma n

#waw
def valid(k):
    if st[k] not in st[1:k]:
        return True
    return False

def solutie(k):
    if sum(st[1:k+1]) == n:
        return True
    return False

def print_with_zero(st):
    if 0 not in st:
        print("".join([str(x) for x in st]),end="")
        print("0")
def back(k):
    if k==1:
        start=1
    else:
        start=0
    for i in range(start, 10-k+1):
        st[k] = i

        if valid(k):
            if solutie(k):
                print("".join(str(x) for x in st[1:k+1]))
                print_with_zero(st[1:k+1])
            else:
                back(k+1)

n=4
st = [0] * 11
back(1)