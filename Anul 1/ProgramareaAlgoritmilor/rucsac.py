from pathlib import Path
text = Path("tis.txt").read_text().split('\n')

n = int(text[0])
s = int(text[-1])
ob = []

def cost_per_kg(x):
    return x[0]/x[1]

for line in text[1:-1]:
    obj = [int(x) for x in line.split(' ')]
    ob.append(tuple(obj))
print(ob)
ob.sort(key= lambda x:cost_per_kg(x),reverse=True)
rucsac=[]
for o in ob:
    if o[1]< s:
        s-=o[1]
        rucsac.append(o)
    else:
        cost_kg = o[0] / o[1]
        rucsac.append(cost_kg*s)

print(rucsac)

print(ob)