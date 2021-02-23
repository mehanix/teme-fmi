#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

ifstream in("grarb.in");
ofstream out("grarb.out");

vector<int> g[100002];
int discTime[100002];
int n, m, nr_componente;
int t = 0, nr = 0;
void dfs(int from)
{
    discTime[from] = nr_componente;
    for (auto &to : g[from])
    {
        if (discTime[to] == 0)
        {
            cout << from << ' ' << to << '\n';
            nr++;
            dfs(to);
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
        if (discTime[i] == 0)
        {
            nr_componente++;
            dfs(i);
        }
    }
    out << m - nr << '\n'
        << nr_componente - 1;
    // cout << nr;
}