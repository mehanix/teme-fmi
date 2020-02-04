from pathlib import Path

txt = Path("input.txt").read_text().split('\n')
spectacole = [tuple([x for x in l.split(' ')]) for l in txt]
print(spectacole)
spectacole.sort(key= lambda x:x[0])
print(spectacole)
sali = [ [spectacole[1]]]

for sp in spectacole[1:]:
    for sala in sali:
       if sala[-1][1] <= sp[0]:
        sala.append(sp)
        break
    else:
        sali.append([sp])

print(sali,end='\n')
