#include <bits/stdc++.h>

using namespace std;

int n,m;

int graf[1001][1001];
ifstream f("maxflow.in");
ofstream g("maxflow.out");

bool bfs(int rGraf[1001][1001], int s, int t, int parinti[])
{
    bool viz[n+1];
    memset(viz,0,sizeof(viz));
    queue<int>q;
    q.push(s);
    viz[s]=true;
    parinti[s]=-1;

    while(!q.empty())
    {
        int from = q.front();
        q.pop();
        for(int to=1;to<=n;to++)
        {
            if(viz[to]==false && rGraf[from][to]>0)
            {
                q.push(to);
                parinti[to]=from;
                viz[to]=true;
            }
        }
    }

        return viz[t]==true;

}
int ford_fulkerson(int s, int t)
{
    int u,v;

    //graf rezidual, initial e identic cu graful original
    int rGraf[1001][1001];

    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            rGraf[i][j]=graf[i][j];
    
    // in asta stochez pathul gasit de bfs
    int parinti[1001];

    int max_flow=0;

    // caut un drum valid
    while(bfs(rGraf,s,t,parinti))
    {
        //parcurg drum rezultat si aflu bottleneck
        int flow = INT_MAX;
        for(int child=t;child!=s;child=parinti[child])
        {
            int parent = parinti[child];
            flow = min(flow,rGraf[parent][child]);
        }

        //dau update valorior in drum, pe front edge scad, pe back adun
        for(int child=t;child!=s;child=parinti[child])
        {
            int parent = parinti[child];
            rGraf[parent][child]-=flow;
            rGraf[child][parent]+=flow;
        }

        max_flow+=flow;
    }

    return max_flow;

}

int main()
{
    f>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int x,y,z;
        f>>x>>y>>z;
        graf[x][y]=z;
    }
    g<<ford_fulkerson(1,n);

}