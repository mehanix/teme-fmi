def nr_pozitive(array):
    if len(array) == 1:
        if array[0] > 0:
            return 1
        return 0
    left = nr_pozitive(array[0:len(array)//2])
    right = nr_pozitive(array[len(array)//2:])
    return left+right

with open("tis.txt", "r") as f:
    array = [int(x) for x in f.read().strip().split(' ')]
    print(array)
    print(nr_pozitive(array))

#moama