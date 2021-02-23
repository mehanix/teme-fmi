#include <bits/stdc++.h>

using namespace std;

struct edge {
    int to, l, r;
};

vector <edge> g[1005];
vector<int> lefts;

int n,m;
int maxx=0;
bool viz[1005];

void dfs(int from, int left, int right)
{
    viz[from]=1;
    for(auto &x:g[from])
    {
        if(viz[x.to] == false)
        {
            if(x.l <= left && right <= x.r)
                dfs(x.to, left,right);
        }
    }
}
bool check_path(int left, int right)
{
    memset(viz,0,sizeof(viz));
    dfs(1,left,right);
    return viz[n];
}
void cautbin(int left) {
    int l=left, r=1000000;
    while(l<=r) {
        int m = (l+r)/2;
        if(check_path(left,m)) {
            l= m+1;
            maxx = max(maxx,m-left+1);
        }
        else
        {
            r=m-1;
        }
        
    }
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int from;
        edge aux;
        cin>>from>>aux.to>>aux.l>>aux.r;
        lefts.push_back(aux.l);
        g[from].push_back(aux);
        swap(from,aux.to);
        g[from].push_back(aux);
    }
    for(auto &left:lefts)
    {
        cautbin(left);
    }
    if(maxx==0)
    {
        cout<<"Nice work, Dima!\n";
    }
    else
    {
        cout<<maxx<<'\n';
    }
    
}