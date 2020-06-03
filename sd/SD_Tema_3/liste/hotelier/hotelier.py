x = int(input())
st = input()

rooms = [0 for _ in range(10)]


for ltr in st:
    if ltr == 'L':
        x=0
        while(rooms[x]==1):
            x+=1
        rooms[x]=1
    elif ltr =='R':
        x=9
        while(rooms[x]==1):
            x-=1
        rooms[x]=1
    else:
        rooms[int(ltr)]=0
print ("".join(str(x) for x in rooms))