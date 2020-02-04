from pathlib import Path

text = Path("tis.txt").read_text().split('\n')
n = int(text[0])
cuburi = []
for line in text[1:]:
    cuburi.append(tuple(line.split(' ')))
print(cuburi)
cuburi.sort(key = lambda x: int(x[0]),reverse=True)
print(cuburi)

turn = []

#incepem turnu cu primu cub

turn.append(cuburi[0])

for cub in cuburi[1:]:
    # daca au culori diferite, pune-l si gata
    if cub[1] != turn[-1][1]:
        turn.append(cub)
    # altfel, daca au aceeasi culoare, nu face nimic?
print(turn)