#include <bits/stdc++.h>

using namespace std;

int n,m;

int graf[401][401];
int dist[401];
void bfs(int culoare)
{
    queue<int> q;
    q.push(1);
    fill(dist,dist+n+1,-1);
    dist[1]=0;
    while(!q.empty())
    {
        int curent = q.front();
        q.pop();
        for(int i=1;i<=n;i++)
        {
            if(graf[curent][i] == culoare && dist[i]==-1)
            {
                dist[i] = dist[curent] + 1;
                q.push(i);

            }
        }
    }
}
int main() {

    cin>>n>>m;
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin>>x>>y;
        graf[x][y]=1;
        graf[y][x]=1;
    }

    // o culoare 1 cealalalta 0
    bfs(1-graf[1][n]);
    cout<<dist[n];

    return 0;
}