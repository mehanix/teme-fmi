#include <bits/stdc++.h>

using namespace std;

ifstream f("cmcm.in");
ofstream g("cmcm.out");
struct Muchie
{
    int to;
    int flow;
    int cap;
    int cost;
    int rev;
    int ind;
};

struct Nod
{
    int nod;
    int cost;
    bool operator >(const Nod &other) const
    {
        return cost > other.cost;
    }
};
const int nmax=610;
class fmcm
{
public:
    vector<Muchie> graf[1 + nmax];
    int dist_bell[1+nmax];
    int dist_dijkstra[1+nmax];
    int plusflow[1+nmax];
    Muchie* prevmuchie[1+nmax];
    int prevnod[1+nmax];
    int n;
    fmcm(int n)
    {
        this->n=n;
    }

    void add(int s, int d, int cap, int cost, int ind)
    {
        Muchie ob1 = {d,0,cap,cost,graf[d].size(), ind};
        Muchie ob2 = {s,0,0,-cost,graf[s].size(), -1};

        graf[s].push_back(ob1);
        graf[d].push_back(ob2);
    }

    void bellmanford(int s)
    {
        fill(dist_bell+1,dist_bell+n+1,INT_MAX / 2);
        queue<int>q;
        q.push(s);
        dist_bell[s]=0;
        while(!q.empty())
        {
            int from = q.front();
            q.pop();

            for(auto &e:graf[from])
            {
                if(e.flow < e.cap && dist_bell[e.to] > dist_bell[from] + e.cost)
                {
                    dist_bell[e.to] = dist_bell[from] + e.cost;
                    q.push(e.to);
                }
            }
        }
    }

    void dijkstra(int s)
    {
        fill(dist_dijkstra+1,dist_dijkstra+n+1,INT_MAX / 2);
        dist_dijkstra[s]=0;
        plusflow[s]=INT_MAX / 2;
        priority_queue<Nod,vector<Nod>,greater<Nod>> pq;

        pq.push({s,dist_dijkstra[s]});
        while(!pq.empty())
        {
            Nod from = pq.top();
            pq.pop();
            for(auto &e:graf[from.nod])
            {
                if(e.flow < e.cap && dist_dijkstra[e.to] > dist_dijkstra[from.nod] + e.cost + dist_bell[from.nod] - dist_bell[e.to])
                {
                    dist_dijkstra[e.to] = dist_dijkstra[from.nod] + e.cost + dist_bell[from.nod] - dist_bell[e.to];
                    pq.push({e.to,dist_dijkstra[e.to]});

                    prevnod[e.to]=from.nod;
                    prevmuchie[e.to] = &e;
                    plusflow[e.to] = min(plusflow[from.nod],e.cap - e.flow);
                }
            }
        }
    }

    void dfs(int from, vector<int> &rasp) {
        for(auto &e: graf[from]) {
            if(e.flow > 0) {
                e.flow --;
                if(e.ind > 0) {
                    rasp.push_back(e.ind);
                }
                dfs(e.to, rasp);
            }
        }
    }

    void MinCutMaxFlow(int s, int d)
    {
        vector <int> rasp;
        bellmanford(s);
        dijkstra(s);
        int flow=0;
        int flowcost=0;
        while(dist_dijkstra[d]<INT_MAX / 2)
        {
            int current_flow = plusflow[d];
            flow+=current_flow;

            for(int to=d; to!=s; to=prevnod[to])
            {
                prevmuchie[to]->flow+=current_flow;
                assert(to==prevmuchie[to]->to);
                graf[to][prevmuchie[to]->rev].flow-=current_flow;
                flowcost+=current_flow*prevmuchie[to]->cost;
            }

            for(int i=1; i<=n; i++)
            {
                dist_bell[i]+=dist_dijkstra[i];
            }
            dijkstra(s);
        }

        dfs(s, rasp);
        //assert(rasp.size() == flow);
        g << flow << ' ' << flowcost << '\n';
        for(auto &x: rasp) {
            g << x << " ";
        }
    }

};


int main()
{
    int n, m, nr_muchii;
    f >> n >> m >> nr_muchii;
    fmcm gr(302 + m);
    int s=300+m+1;
    int d=s + 1;
    for(int i=1; i<=nr_muchii; i++)
    {
        int x, y, cost;
        f >> x >> y >> cost;
        y += 300;

        gr.add(x, y, 1, cost, i);
    }
    for(int i = 1; i <= n; i ++)
        gr.add(s,i,1,0,-1);
    for(int i = 1; i <= m; i ++)
        gr.add(i + 300,d,1,0,-1);


    gr.MinCutMaxFlow(s,d);

    return 0;
}