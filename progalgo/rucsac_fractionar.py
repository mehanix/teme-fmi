from pathlib import Path

txt = Path("input.txt").read_text().split('\n')
n,capacitate = [int(x) for x in txt[0].split(' ')]
print(n,capacitate)
obj = [tuple(int(x) for x in l.split(' ')) for l in txt[1:]]
raport = []

print(obj)
for i in range(len(obj)):
    raport.append(tuple([i,obj[i][0]//obj[i][1]]))

raport.sort(key=lambda x:x[1],reverse=True)

for i, rap in raport:

    if capacitate > obj[i][1]:
        print (i+1,"100")
        capacitate -= obj[i][1]
    else:
        print(i+1, capacitate/obj[i][1]*100)
        break
