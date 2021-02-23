#include <bits/stdc++.h>

using namespace std;
ifstream f("disjoint.in");
ofstream g("disjoint.out");

int t[100005];
int h[100005];
int n,m;

int find_tata(int x) {
    if(x==t[x])
        return x;
    return find_tata(t[x]);
}

void uneste(int x, int y){
  x = find_tata(x);
  y = find_tata(y);
    if(h[x] == h[y]) {
        t[x] = y;
        h[y] ++;
    }
    else if (h[x] < h[y]) {
        t[x]=y;
    }
    else {
        t[y]=x;
    }
    
}
void verifica(int x, int y) {
    x = find_tata(x);
    y = find_tata(y);
    if(x==y)
        g<<"DA\n";
    else
        g<<"NU\n";
    
}
int main() {
    f>>n>>m;
    for(int i=1;i<=n;i++)
    {
        t[i]=i;
        h[i]=1;
    }

    while(m--){
        int tip,x,y;
        f>>tip>>x>>y;
        if(tip==1){
            uneste(x,y);
        }
        else {
            verifica(x,y);
        }
    }
}