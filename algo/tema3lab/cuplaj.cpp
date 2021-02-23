#include <bits/stdc++.h>

using namespace std;

int n,m,e;

vector<int>muchie[10001];
ifstream f("cuplaj.in");
ofstream g("cuplaj.out");

int stg[10001]; //capatul dreapta al nodului x din stg
int dr[10001];  //capatul stanga al nodului x din dr
int used[10001];
int gasit=0;
bool dfs(int from)
{
    used[from]=1;
    //incerc sa leg direct
    for(auto &to:muchie[from])
    {
        if (dr[to]!=0)
            continue;
        stg[from]=to;
        dr[to]=from;
        gasit=1;
        return 1;
    }

    //lant alternant
    for(auto &to:muchie[from])
    {
        if(!used[dr[to]])
        {
          
            if(dfs(dr[to]))
            {
                dr[to]=from;
                stg[from]=to;
                return 1;
            }
        }
    }
    return 0;
}
int main()
{
    f>>n>>m>>e;
    for(int i=1;i<=e;i++)
    {
        int x,y;
        f>>x>>y;
        muchie[x].push_back(y);
    }
    do
    {
        gasit = 0;
        fill(used+1,used+n+1,0);
        for(int i=1;i<=n;i++)
        {
            if(stg[i]==0)
            {
                dfs(i);
            }
        }
    } while (gasit);

    vector<pair<int,int>>rez;
    for(int i=1;i<=n;i++)
    {
        if(stg[i]!=0)
            rez.push_back({i,stg[i]});
    }
    g<<rez.size()<<'\n';
    for(auto &x:rez)
    {
        g<<x.first<<' '<<x.second<<'\n';
    }
}