#include <bits/stdc++.h>

using namespace std;

ifstream f("tempest.in");
ofstream g("tempest.out");

struct Muchie {
    long long nod, cost;
};

const long long INF = 1e18;


struct Elem {
    long long nod, cost;
    bool operator<(Elem other) const {
        if (cost == other.cost) return nod > other.nod;
        return cost > other.cost;
    }    
};

int n,m,s,d,t,k;
int main() {
    f>>t;
    while(t--)
    {
        f>>n>>m>>s>>d;
     
        vector<vector<Muchie>> graf(n+1);
        vector<long long> dist(n+1);
        vector<int> costuri_muchii(m+1);

        for(int i=1;i<=m;i++)
        {
            int from,to,cost;
            f>>from>>to>>cost;
            graf[from].push_back({to,cost});
            graf[to].push_back({from,cost});
            costuri_muchii[i]=cost;
        }
        f>>k;

        long long sum=0;
        for(int i=1;i<=k;i++)
        {
            int aux;
            f>>aux;
            sum+=costuri_muchii[aux];
        }

         
    priority_queue<Elem> pq;

    for(int i=1;i<=n;i++) {
        dist[i]=INF;
    }
    dist[d]=0;
    pq.push({d,0});

    while(!pq.empty()){
        Elem from = pq.top();
        pq.pop();

        if (from.cost != dist[from.nod])
            continue;
        
        for(auto &to:graf[from.nod])
        {
            if(dist[to.nod] > dist[from.nod] + to.cost)
            {
                dist[to.nod] = dist[from.nod] + to.cost;
                pq.push({to.nod,dist[to.nod]});
            }
        }
    }
    vector<int> sol;
    for(int i=1;i<=n;i++)
    {
        if(dist[i] <= sum) 
            sol.push_back(i);
    }

    g<<sol.size()<<'\n';
    for(auto &x:sol)
        g<<x<<' ';
    g<<'\n';
    }
  
   
}