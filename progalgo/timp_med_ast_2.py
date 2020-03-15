from pathlib import Path

v = [int(x) for x in Path("input2.txt").read_text().split(' ')]

v.sort()

s=0 #suma timpilor asteptare
current_wait=0 #timp asteptare curent
for x in v:
    s+=current_wait

    print("client= {},a asteptat={},suma timp asteptare={}".format(x,current_wait,s))
    current_wait += x
print(s//len(v))