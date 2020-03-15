from pathlib import Path

def scm(sir1,sir2):
   m = len(sir1)
   n = len(sir2)
   mat =[[0]*(n+1) for _ in range(m+1)]
   for i in range(1,m+1):
       for j in range(1,n+1):
           if sir1[i-1]==sir2[j-1]:
               mat[i][j]=mat[i-1][j-1]+1
           else:
               mat[i][j]=max(mat[i-1][j],mat[i][j-1])
   return mat

txt = Path("input.txt").read_text().split('\n')
sir1 = [int(x) for x in txt[0].split(' ')]
sir2 = [int(x) for x in txt[1].split(' ')]



print(scm(sir1,sir2))
