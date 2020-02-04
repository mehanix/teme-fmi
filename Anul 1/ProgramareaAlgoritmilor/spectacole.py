from pathlib import Path

text = Path("tis.txt").read_text().split('\n')
spectacole = []
for line in text:
    line = line.replace('-',' ', 1).split(" ", 2)
    spectacole.append(tuple(line))

print(spectacole)

spectacole.sort(key = lambda x: x[0])
print(spectacole)

sala = []

sala.append(spectacole[0])
print(sala)
for spectacol in spectacole[1:]:
    # daca e loc de el, pune-l (adica daca sfarsitu ultimului spectacol e inaintea inceputului spectacolului curent)
    if sala[-1][1] < spectacol[0]:
        sala.append(spectacol)
    #else, daca spectacolul asta se termina mai devreme decat spectacolul anterior, inlocuieste-l
    elif sala[-1][1] > spectacol[1]:
        sala[-1] = spectacol
print(sala)

# merge!!!!!!!!!!!




