def maxPathSum(mat,n):
   for i in range(n-1,-1,-1):
       for j in range(i+1):
           mat[i][j]+=max(mat[i+1][j],mat[i+1][j+1])
   print(mat)
   return mat[0][0]


tri = [[1, 0, 0],
       [4, 8, 0],
       [1, 5, 3]]
print(maxPathSum(tri, 2))