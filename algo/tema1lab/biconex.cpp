#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
using namespace std;

ifstream in("biconex.in");
ofstream out("biconex.out");

vector<int> g[100002];
int discoverTime[100002];
int lowTime[100002];
int parentOf[100002];
int n, m, nr_componente;
int t = 0;
vector<set<int>> rasp;
stack<pair<int, int>> st;
void dfs(int from)
{
    t++;
    discoverTime[from] = lowTime[from] = t;
    for (auto &to : g[from])
    {
        if (discoverTime[to] == 0)
        {
            parentOf[to] = from;
            st.push(make_pair(from, to));
            dfs(to);
            if (lowTime[to] >= discoverTime[from]) //daca e pct de articulatie
            {
                nr_componente++;
                set<int> s;
                while (st.top() != (make_pair(from, to)))
                {
                    s.insert(st.top().first);
                    s.insert(st.top().second);
                    st.pop();
                }
                s.insert(st.top().first);
                s.insert(st.top().second);
                st.pop();
                rasp.push_back(s);
            }
            lowTime[from] = min(lowTime[from], lowTime[to]);
        }
        else
        {
            if (parentOf[from] != to)
            {
                lowTime[from] = min(lowTime[from], discoverTime[to]);
            }
        }
    }
}
int main()
{
    in >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int x, y;
        in >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    for (int i = 1; i <= n; i++)
    {
        if (discoverTime[i] == 0)
        {
            dfs(i);
        }
    }
    out << rasp.size() << '\n';
    for (auto &s : rasp)
    {
        for (auto &x : s)
        {
            out << x << ' ';
        }
        out << '\n';
    }
}