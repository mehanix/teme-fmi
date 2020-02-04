from pathlib import Path

text = Path("tis.txt").read_text().split('\n')
n = int(text[0])

activitati = []

for line in text[1:]:
    activitati.append(tuple([int(x) for x in line.split(' ')]))
activitati.sort(key= lambda x: x[1])
current_time = 0
total_delay = 0
for a in activitati:
    #le luam in ordinea deadlineului
    new_time = current_time + a[0] #timp curent + durata
    total_delay += max(0,  new_time - a[1])
    print(a, new_time,total_delay)
    current_time = new_time

print(activitati)
print(total_delay)