#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int>> graf[50005];
int dist[50005];
int viz[50005];
int n,m;

ifstream f("bellmanford.in");
ofstream g("bellmanford.out");
int main() {
    f>>n>>m;
    for(int i=1;i<=m;i++) {
        int x,y,c;
        f>>x>>y>>c;
        graf[x].push_back({y,c});
    }

    fill(dist,dist+n+1,INT_MAX);
    dist[1]=0;
    queue<int> q;
    q.push(1);
    
    while(!q.empty())
    {
        int from = q.front();
        q.pop();
        viz[from]++;
        if(viz[from] == n+1){
            g<<"Ciclu negativ!";
            return 0;
        }
        for(auto &x:graf[from])
        {
            int to = x.first;
            int cost = x.second;
            if(dist[to] > dist[from] + cost) {
                dist[to] = dist[from] + cost;
               q.push(to);
            }
            
        }
    }

    for(int i=2;i<=n;i++)
    {
        if (dist[i] == INT_MAX) {
                dist[i] = 0;
            }
        g<<dist[i]<<' ';
	
    }
}