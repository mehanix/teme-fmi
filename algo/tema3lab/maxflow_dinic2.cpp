#include <bits/stdc++.h>

using namespace std;

struct Muchie {
    int to;
    int flow;
    int cap;
    int rev;
};
int rem[1001];
int 

int maxflow(int s,int t){
    int total=0;
    while(bfs()==1) {
        fill(rem+1,rem+n+1,0);
        do {
            int val += dfs(sursa,INT_MAX);
            total += val;
        } while (val > 0);
    }

    return total;
}

vector<Muchie> graf[1001];
ifstream f("maxflow.in");
ofstream g("maxflow.out");
int n,m;
int main()
{
    f>>n>>m;
    for (int i=1;i<=m;i++)
    {
        int x,y,c;
        f>>x>>y>>c;
        graf[x].push_back({y,0,c,graf[y].size()});
        graf[y].push_back({x,0,0,graf[x].size()-1});
    }
    g<<maxflow(1,n));
}