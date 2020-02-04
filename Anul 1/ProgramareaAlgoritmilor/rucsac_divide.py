f = open("tis.txt","r")

text = [ t.strip() for t in f.readlines()]

cap = int(text[0])

obiecte = [tuple([int(x) for x in t.split(' ')]) for t in text[1:]]
obiecte.sort()

for i in range (1,cap+1):
    
print(obiecte)