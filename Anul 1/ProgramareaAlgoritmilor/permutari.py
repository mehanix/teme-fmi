def printt():
    for l in board:
        print(l)
    print()

def isSafe(i,j):
    # verif orizontala, verticala
    for a in range(n):
        if board[a][j]==1:
            return 0

    for row,col in zip(range(i,-1,-1), range(j,-1,-1)): #diagonala "principala"
        if board[row][col]==1:
            return 0

    for row,col in zip(range(i,n,1), range(j,n,1)): #diagonala "secundara"
        print(row,col)
        if board[row][col]==1:
            return 0


    return 1

def back(k): # k= col curenta
    if k>=n:
        printt()
        return True
    for i in range(n):
        if isSafe(k,i):
            board[k][i]=1
            back(k+1)
            board[k][i] = 0


n=4
board = [[0 for i in range(n)] for j in range(n)]
back(0)