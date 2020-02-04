cnt = 0
def find_vf(start,end):
    global cnt
    cnt+=1
    if start>end:
        return 0
    mid = (start+end) // 2

    if mid==0 and v[mid] >v[mid+1]:
        return v[mid]
    if mid==len(v)-1 and v[mid-1] < v[mid]:
        return v[mid]

    if v[mid-1] < v[mid] > v[mid+1]:
        return v[mid]
    elif v[mid-1] > v[mid]: # go left
        return find_vf(start, mid-1)
    else: #go right
        return find_vf(mid+1,end)


with open("tis.txt","r") as f:
    txt = [t.strip() for t in f.readlines()]
    n = int(txt[0])
    v = [int(x) for x in txt[1].split(' ')]

    print(v,n)
    print(find_vf(0,len(v)-1),cnt)