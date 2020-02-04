def binary_search(v,start,end,n):

    if start>end:
        return -1
    else:
        mij = (start+end)//2
        if v[mij] == n:
            return 1
        elif n < v[mij]:
            return binary_search(v,start,mij-1,n)
        else:
            return binary_search(v,mij+1,end,n)


with open("tis.txt","r") as f:
    text = [t.strip() for t in f.readlines()]
    v = [int(x) for x in text[0].split(' ')]
    n = int(text[1])
    print(v,n)
    t = binary_search(v,0,len(v)-1,n)
    print(t)