import random
import sys
def pivot(list, left, right):
    i = left
    j = right
    di = 0
    dj = 1

    while i < j:
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
            di,dj = dj,di

        i += di
        j -= dj

    return i


def quicksort(list, left, right, pas):

    global copylist
    if pas == 0:
        copylist = list.copy()
        pas = 1

    if left < right:
        x = pivot(copylist, left, right)
        quicksort(copylist, left, x - 1, pas)
        quicksort(copylist, x + 1, right, pas)
    return copylist
#
# Driver code to test above 
arr = [0]*10000000
sys.setrecursionlimit(99999999)
for i in range(10000000):
    arr[i] = random.randrange(0,1000)
n = len(arr) 
quicksort(arr,0,n-1,0) 
print("done")