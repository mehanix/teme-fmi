from pathlib import Path


def merge(left,right):
    i=j=0
    result = []

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    print(result)
    return result

def mergesort(v):

    if len(v)<=1:
        return v

    half = len(v)//2
    left = mergesort(v[:half])
    right = mergesort(v[half:])

    return merge(left,right)


v = [int(x) for x in Path("input.txt").read_text().split(' ')]

print(mergesort(v))

