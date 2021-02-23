#include <bits/stdc++.h>

using namespace std;

vector<int> graf1[100002],graf2[100002];

int viz[100002];
int n,m,x;
int d;
int cnt;
unsigned long long sum1,sum2;

unsigned long long calculeaza_combinari(int x) {
    //if (x<2) return 0;
    if(x%2 == 0)
      return (x/2)*(x-1);

return ((x-1)/2)*x;

}
void dfs(int i, vector<int> graf[100002]) {
    viz[i]=d;
    cnt++;
    for(auto &x:graf[i])
        if(viz[x]==0)
          dfs(x,graf);
}

int main()
{
    cin>>n>>m>>x;
    for(int i=1;i<=m;i++)
    {
        int from,to,cost;
        cin>>from>>to>>cost;
        // graf 1:toate muchiile cu cost <=x
        // graf 2:toate muchiile cu cost <=x-1
        if(cost <= x)
            {
                graf1[from].push_back(to);
                graf1[to].push_back(from);

            }
        if(cost <= x-1)
            {
                graf2[from].push_back(to);
                graf2[to].push_back(from);

            }
    }

    // for(int i=1;i<=n;i++)
    // {
    //     for(auto &x:graf1[i]) {
    //         cout<<i<<' '<<x<<'\n';
    //     }
    // }
    // cout<<"\n\n\n";

    

    // gasit componente conexe graf 1
    d=0;
    for(int i=1;i<=n;i++) {
        if(viz[i]==0) {
            cnt=0;
            d++;
            dfs(i,graf1);
            sum1+= calculeaza_combinari(cnt);
         //   cout<<cnt<<'\n';
        }
    }

    // gasit componente conexe graf 2
    d=0;
    fill(viz,viz+n+1,0);
    for(int i=1;i<=n;i++) {
        if(viz[i]==0) {
            cnt=0;
            d++;
            dfs(i,graf2);
            sum2+= calculeaza_combinari(cnt);
         //   cout<<cnt<<'\n';
        }
    }
    cout<<sum1-sum2<<'\n';
}