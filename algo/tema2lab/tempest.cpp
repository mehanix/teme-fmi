#include <bits/stdc++.h>

using namespace std;

ifstream f("tempest.in");
ofstream g("tempest.out");


vector<pair<int,int>>graf[100005];
int costuri_muchii[100005];
int n,m,s,d,t,k;
vector<pair<int,int>> drum;
int dist[100005];
const int INF = 0x3f3f3f3f;

struct e {
    int nod;
    int dist;
    int remaining;
};
int main() 
{
    f>>t;
    while(t--)
    {
        f>>n>>m>>s>>d;
        for(int i=1;i<=m;i++)
        {
            int from,to,cost;
            f>>from>>to>>cost;
            graf[from].push_back({to,cost});
            graf[to].push_back({from,cost});
            costuri_muchii[i]=cost;
        }
        f>>k;
        //strang punctele care s pe drum, calculez lungime
        int sum=0;
        for(int i=1;i<=k;i++)
        {
            int aux;
            f>>aux;
            sum+=costuri_muchii[aux];
        }
    }
}