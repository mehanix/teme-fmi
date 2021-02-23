#include <bits/stdc++.h>

using namespace std;

struct Muchie
{
    int to; // nod dest (from e index in lst adiacenta)
    int flow; // cat are in ea
    int cap; // cat poate tine
    int rev; // index muchie inversa in lst adiacenta
};

class Graf
{
public:

    int n;
    int *level; //vector nivele
    vector<Muchie> *graf;
    Graf(int N)
    {
        graf = new vector<Muchie>[N+1];
        this->n = N;
        level = new int[n+1];
    }

    void add(int from, int to, int cap)
    {
        Muchie ob1 = {to,0,cap,graf[to].size()};
        Muchie ob2 = {from,0,0,graf[from].size()};
        //inserez front si back edge cu cap corespunzatoare
        graf[from].push_back(ob1);
        graf[to].push_back(ob2);
    }

    bool bfs(int s, int t)
    {
        /** Calculez nivelele nodurilor*/

        for(int i=1;i<=n;i++)
            level[i]=-1;
        
        level[s] = 0;

        queue<int>q;
        q.push(s);
        while(!q.empty())
        {
            int from = q.front();
            q.pop();

            for(auto &nod:graf[from])
            {
                // daca nu am mai fost pe aici & muchia nu e saturata
                if(level[nod.to] < 0 && nod.flow < nod.cap)
                {
                    level[nod.to] = level[from] +1;

                    q.push(nod.to);
                }
            }
        }
        
        return level[t] > 0;
    }

    int dfs(int from, int flow, int t, int start[])
    {
        if (from == t)
            return flow;
        
        //trec pe rand prin toate muchiile adiacente
        // in start[from] tin nr muchii vizitate
        for(; start[from] < graf[from].size(); start[from]++)
        {
            Muchie &m = graf[from][start[from]];
            if(level[m.to] == level[from] +1 && m.flow < m.cap )
            {
                int curr_flow = min(flow, m.cap - m.flow);
                int temp_flow = dfs(m.to,curr_flow,t,start);
                if(temp_flow > 0)
                {
                    m.flow+=temp_flow;
                    graf[m.to][m.rev].flow -= temp_flow;
                    return temp_flow;
                }
            }
        }
        return 0;
    }
    int maxflow(int s, int t){
        if(s==t)
            return -1;
        
        int total = 0;
        
        int *start = new int[n+1];
        while(bfs(s,t) == true)
        {
            fill(start,start+n+1,0);
            while(int flow = dfs(s,INT_MAX,t,start))
                total+=flow;
        }
        return total;
    }
};

int n,a,b;
vector<int>team_a;
vector<int>team_b;
vector<pair<int,int>>sol;
bool current_team[301];
int main()
{
    cin>>n>>a;
    for(int i=1;i<=a;i++)
    {
        int x;
        cin>>x;
        team_a.push_back(x);
        current_team[x]=1;
    }
    for(int i=1;i<=a;i++)
    {
        int x;
        cin>>x;
        team_b.push_back(x);
    }

    Graf gr(n+2);

    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
        {
            char x;
            cin>>x;
            if(x=='1')
                gr.add(i,j,INT_MAX);
        }
    
    int s=n+1;
    int d=n+2;
    n=n+2;
    for(auto &x:team_a)
    {
        gr.add(s,x,1);
    }
        for(auto &x:team_b)
    {
        gr.add(x,d,1);
    }
    if(gr.maxflow(s,d) == a)
    {
        cout<<"YES\n";
        int ok;
        do 
        {
        ok=0;
         for(int i=1;i<=n-2;i++)
         {
             
             if(current_team[i]==1)
                for(auto &to:gr.graf[i])
                {
                    if(to.flow > 0 && current_team[to.to]==0 && to.to<d)
                    {
                        ok=1;
                        to.flow--;
                        sol.push_back({i,to.to});
                        current_team[i]=0;
                        current_team[to.to]=1;
                        break;
                    }
                }
         }
        } while(ok);
        cout<<sol.size()<<'\n';
        for(auto &x:sol)
        {
            cout<<x.first<<' '<<x.second<<'\n';
        }
    }
    else
    {
        cout<<"NO\n";
    }
}