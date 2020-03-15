from pathlib import Path


def median_of_medians(v):
    if len(v) <= 5:
        return sorted(v)[len(v)//2]

    groups = [v[i:i+5] for i in range(0,len(v),5)]
    groups = [sorted(group) for group in groups]
    medians = [group[len(group)//2] for group in groups]
    return median_of_medians(medians)


def quickselect(v, k):

    pivot = median_of_medians(v)
    lows = [x for x in v if x < pivot]
    eq = [x for x in v if x == pivot]
    highs = [x for x in v if x > pivot]

    if k < len(lows):
        return quickselect(lows,k)
    elif k < len(lows) + len(eq):
        return eq[0]
    else:
        return quickselect(highs, k-len(lows)-len(eq))




txt = Path("input.txt").read_text().split('\n')
v = [int(x) for x in txt[0].split(' ')]
k = int(txt[1])

print(quickselect(v,k))