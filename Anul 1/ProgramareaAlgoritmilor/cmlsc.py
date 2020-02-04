from pathlib import Path

txt = Path("input.txt").read_text()
v = [int(x) for x in txt.split(' ')]
arr = [1 for i in range(len(v))]

#dinamica

for i in range(1,len(v)):
    for j in range(i):
        if v[j] < v[i] and arr[j]+1 > arr[i]:
            arr[i] = arr[j]+1


print(arr)