#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

ifstream in("dfs.in");
ofstream out("dfs.out");

vector<int> g[100002];
int viz[100002];
int n, m, nr_componente;

void dfs(int from)
{
    viz[from] = 1;
    for (auto &to : g[from])
    {
        if (viz[to] == 0)
            dfs(to);
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
        if (viz[i] == 0)
        {
            nr_componente++;
            dfs(i);
        }
    }
    out << nr_componente;
}