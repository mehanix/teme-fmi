from pathlib import Path


def partition(start,end):
    i = start - 1
    p = v[end]

    for j in range(start,end):
        if v[j] < p:
            i +=1
            v[i],v[j] = v[j],v[i]

    i += 1
    v[i],v[end] = v[end],v[i]
    return i

def quickselect(start,end,k):
    poz = partition(start,end)

    if k-1 == poz:
        return v[poz]
    elif k-1 < poz: #stanga
        return quickselect(start,poz-1,k)
    else: return quickselect(poz+1,end,k)

txt = Path("input.txt").read_text().split('\n')
v = [int(x) for x in txt[0].split(' ')]
k = int(txt[1])
print (quickselect(0, len(v)-1,k))