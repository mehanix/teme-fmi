def knapSack(W,wt,val,n):
    mat = [[0 for i in range(W+1)] for j in range(n+1)]
    #iterez prin obiecte
    for i in range(1,n+1):
        for j in range(W+1): # iterez prin greutati
            #daca nu pot lua obiectul, adica daca greutatea lui e mai mare decat greutatea curenta
            if wt[i-1] > j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j], mat[i-1][j-wt[i-1]]+val[i-1])


    l = []
    i=n
    j=W
    print(mat)
    while j > 0 and i > 0:
        while mat[i-1][j]==mat[i][j]:
            i-=1
        print(wt[i-1])
        j = j - wt[i-1]

    return mat[n][W]




# Driver program to test above function

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(val)
print(knapSack(W, wt, val, n))