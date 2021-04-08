# Explicatie:

# Formez sume partiale intr-o matrice dp[k][n] unde:
# i = la primele cate elemente ma uit
# j = suma partiala maxima pe care vreau sa o obtin ( cu primele i elemente, vreau sa obtin suma maxima <=j)

# La pasul dp[i][j], ma decid daca adaug obiectul s[i-1] sumei partiale curente sau nu (s e 0-indexed):
#  - daca nu-l adaug, dp[i][j] = dp[i-1][j] (suma maxima <=j fara elem i)
#  - daca-l adaug, si fac asta doar daca nu depasesc j, dp[i][j] = dp[i-1][j-s[i-1]] + s[i-1] (elementul s[i-1] + suma maxima care mai incape pe langa el (din sumele fara i, aleg suma partiala maxima <= j-s[i-1], de exemplu pt j=7 si s[i-1]=3, daca aleg sa il iau pe 3, suma maxima va fi 3 + suma maxima pe care o pot obtine fara elementul 3 si cu valoarea maxima <=4)
 
# In dp[n][k] voi avea suma maxima obtinuta cu toate cele N elemente si valoarea <=k.

# Complexitate: O(n*k) timp, pseudopolinomiala pt ca depinde de K, spatiu se poate reduce la O(2*k) daca retin doar ultimele 2 randuri pt ca doar de alea ma folosesc.

n = int(input())
k = int(input())
s = []
for i in range(n):
    s.append(int(input()))

dp = [[0 for i in range (k+1)] for j in range(n+1)]
for i in range(n):
    for j in range(1,k+1):
        elem = 0
        if  dp[i-1][j-s[i-1]] + s[i-1] <=j:
            elem = dp[i-1][j-s[i-1]] + s[i-1]
        dp[i][j]=max(dp[i-1][j],elem)


print (dp[n-1][k])
