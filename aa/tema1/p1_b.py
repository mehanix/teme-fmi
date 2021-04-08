

# L -> lista de numere
# Algoritmul compune o suma incercand sa se apropie cat mai mult de valoarea K parcurgand sirul de elemente L si adunand numarul L[i] daca "mai este loc" pentru el (daca spatiul ramas permite sa-l mai adun si pe L[i] fara sa depasesc K)
# In timp ce fac parcurgerea, mai calculez si valoarea maxima din L si aleg maximul dintre s si aceasta pt a obtine o solutie 1/2-aproximativa.

# Cum stiu ca s[i] <= K, am 2 situatii in functie de maxim:
# 	daca m >= k/2, OPT(i) < 2 * ALG(i)
# 	daca m < k/2, cum m e cel mai mare nr din lista => toata lista e formata din numere < k/2 si parcurgand toata lista voi obtine o suma >=k/2 deoarece garantat voi putea aduna numere pana cand depasesc k/2, deci OPT(i) < 2 * ALG(I)


n = int(input())
k = int(input())
s = 0
m = -1
while n>0:
    n-=1
    x = int(input())
    if x <= k - s:
        s += x
    if x > m and x <=k:
        m = x

print(max(s,m))
