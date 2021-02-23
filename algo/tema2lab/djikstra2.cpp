#include <bits/stdc++.h>

using namespace std;

int n,m;
vector<pair<int,int>> graf[50005]; //lista de adiacenta

int dist[50005];
const int INF = 0x3f3f3f3f;

ifstream f("dijkstra.in");
ofstream g("dijkstra.out");

set<pair<int,int>>s;
int main() {
    // citesc graf
    f>>n>>m;
    for(int i=0;i<m;i++){
        int src,dst,cost;
        f>>src>>dst>>cost;
        graf[src].push_back(make_pair(cost,dst));
    }

    dist[1] = 0;
    for(int i=2;i<=n;i++) {
        dist[i] = INF;
    }
    set<pair<int,int>>s;
    s.insert({0,1});

    while(!s.empty())
    {
        int from = s.begin()->second;
        s.erase(s.begin());
        for(auto &v:graf[from])
        {
            int to = v.second;
            int cost = v.first;
            if(dist[to] > dist[from] + cost)
            {
                if(dist[to] != INF)
                    s.erase(s.find({dist[to],to}));
                dist[to] = dist[from] + cost;
                s.insert({dist[to],to});
            }
        }
    }
    for(int i=2;i<=n;i++)
    {
         if (dist[i] == INF) {
            dist[i] = 0;
        }
        g<<dist[i]<<' ';
    }
}