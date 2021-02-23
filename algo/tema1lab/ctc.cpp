#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

ifstream in("ctc.in");
ofstream out("ctc.out");

vector<int> g[100002];
int discoverTime[100002];
int lowTime[100002];
bool onStack[100002];
int id;
stack<int> s;
vector<int> rasp[100000];
int n, m, nr_componente;

void dfs(int from)
{
    id++;
    s.push(from);
    onStack[from] = true;
    discoverTime[from] = lowTime[from] = id;

    for (auto &to : g[from])
    {
        if (discoverTime[to] == 0)
        {
            dfs(to);
        }
        if (onStack[to])
        {
            lowTime[from] = min(lowTime[from], lowTime[to]);
        }
    }
    if (lowTime[from] == discoverTime[from])
    {
        while (s.top() != from)
        {
            rasp[nr_componente].push_back(s.top());
            lowTime[s.top()] = min(lowTime[from], lowTime[s.top()]);
            onStack[s.top()] = false;
            s.pop();
        }
        rasp[nr_componente].push_back(s.top());
        onStack[s.top()] = false;
        s.pop();
        ++nr_componente;
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
    }
    for (int i = 1; i <= n; i++)
    {
        if (discoverTime[i] == 0)
        {
            dfs(i);
        }
    }
    out << nr_componente << '\n';
    for (int i = 0; i < nr_componente; i++)
    {
        for (auto &el : rasp[i])
        {
            out << el << ' ';
        }
        out << '\n';
    }
}