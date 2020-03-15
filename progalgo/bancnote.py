from pathlib import Path

text = Path("tis.txt").read_text().split('\n')

bancnote =[int(x) for x in text[0].split(' ')]

bancnote.sort(reverse=True)
suma = int(text[1])
for b in bancnote:
    div = suma // b
    if div>0:
        print(b,"*",div, end=" ")
        suma = suma - div*b
    if suma==0:
        break


