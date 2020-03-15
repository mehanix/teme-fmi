cnt=0
def binary_search_left(start,end,n):

    print(v[start:end+1])
    global cnt
    cnt+=1
    if start>end:
        return 0
    else:
        mid = (start+end) // 2
        if v[mid] > n:
            return binary_search_left(start, mid-1, n)
        elif v[mid] < n:
            return binary_search_left(mid+1,end,n)
        if v[mid] == n and v[mid-1]!=n:
            return mid
        else:
            return binary_search_left(start, mid - 1, n)



with open("tis.txt","r") as f:
    text = [ t.strip() for t in f.readlines()]
    v = [int(x) for x in text[0].split(' ')]
    n = int(text[1])
    v.sort()
    ap = binary_search_left(0,len(v)-1,n)
    print(ap,cnt)