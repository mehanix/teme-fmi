# cel mai simplu exemplu de divide


def sum_rec(v):
    if len(v) <= 1:
        return sum(v)

    mid = len(v)//2
    l = v[:mid]
    r = v[mid:]
    sum_l = sum_rec(l)
    sum_r = sum_rec(r)
    print(sum_l + sum_r)
    return sum_l + sum_r

from pathlib import Path

v = [int(x) for x in Path("input.txt").read_text().split(' ')]

print(sum_rec(v))