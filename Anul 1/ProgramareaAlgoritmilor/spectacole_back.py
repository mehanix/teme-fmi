#spectakole ku baktraking

from pathlib import Path
max_k=0
def valid(k):
    if k==1:
        return True
    if st[k-1][1] < st[k][0]:
        return True
    return False

def solutie(k):
    global max_k
    if k>max_k:
        max_k=k
        return True
    elif max_k == k:
        return True
    return False

def back(k):
    for i in range(k-1,n):
        st[k] = spectacole[i]

        if valid(k):
            back(k + 1)
            if solutie(k):
                print(k,st[1:k+1])




text = Path("tis.txt").read_text().split('\n')
spectacole = []
for line in text:
    line = line.replace('-',' ', 1).split(" ", 2)
    spectacole.append(tuple(line))

spectacole.sort(key = lambda x: x[0])
print(spectacole)
n = len(spectacole)
st = [0] * (len(spectacole)+1)

back(1)