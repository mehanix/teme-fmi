#include <bits/stdc++.h>

using namespace std;

struct muchie {
    int a;
    int b;
    int cost;
} graf[400005];
vector<int> rasp;
int cost;
int t[200005];
int h[200005];
int n,m;
ifstream f("apm.in");
ofstream g("apm.out");

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
bool verifica(int x, int y) {
    return find_tata(x) == find_tata(y);
}

int main() {
    f>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int x,y,c;
        f>>graf[i].a>>graf[i].b>>graf[i].cost;
    }
    sort(graf+1,graf+m+1,[](muchie a, muchie b){return a.cost<b.cost;});
    for(int i=1;i<=n;i++)
    {
        t[i]=i;
        h[i]=1;
    }
    for(int i=1;i<=m && rasp.size()<n-1;i++)
    {
        if(verifica(graf[i].a,graf[i].b) == false) {
            uneste(graf[i].a,graf[i].b);
            cost+=graf[i].cost;
            rasp.push_back(i);
        }
    }
    g<<cost<<"\n"<<rasp.size()<<'\n';
    for(auto &i:rasp) {
        g<<graf[i].a<<' '<<graf[i].b<<'\n';
    }
}