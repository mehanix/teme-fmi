import copy

x = 1

def patratele(top_left, bottom_right):
    global x
    print(top_left, bottom_right)
    if top_left == bottom_right:
        m[top_left[0]][top_left[1]]  = x
        x = x + 1
        for l in m:
            print(l)
        return 0
    # impart in 4

    mid_i = (bottom_right[0] + top_left[0]) //2
    mid_j = (bottom_right[1] + top_left[1]) //2

    # dr sus
    patratele(tuple([top_left[0], mid_j+1]), tuple([mid_i, bottom_right[1]]))
    # stg jos
    patratele(tuple([mid_i+1, top_left[1]]), tuple([bottom_right[0], mid_j]))
    # stg sus
    patratele(top_left, tuple([mid_i , mid_j]))
    # dr jos
    patratele(tuple([mid_i+1, mid_j+1]), bottom_right)


n = 2
m = [[0 for i in range(2**n)] for j in range(2**n)]

top_left = tuple([0, 0])
bottom_right = tuple([(2**n) - 1, (2 ** n) - 1])
for l in m:
    print(l)
patratele(top_left, bottom_right)
for l in m:
    print(l)
