#descompunere
#backtracking, cica

def valid(k):
    s=sum(st[1:k+1])
    if s<=n:
        return True
    return False

def solutie(k):
    return sum(st[1:k+1] )== n

def back(k):
    if k==1:
        start= 1
        end = n
    else:
        start = st[k-1]
        end = n-k+1

    for i in range(start,end+1):
        st[k] = i
        print(st)
        if valid(k):
            if solutie(k):
                print(st[1:k+1])
            else:
                back(k+1)

n=4
st = [0] * (n+1)
back(1)