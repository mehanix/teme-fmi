#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

ifstream in("darb.in");
ofstream out("darb.out");

vector<int> g[100002];
int viz[100002];
int n, m;
int nod_max, h_max;
void dfs(int from, int nivel = 0)
{
    if (nivel > h_max)
    {
        h_max = nivel;
        nod_max = from;
    }
    viz[from] = nivel;
    for (auto &to : g[from])
    {
        if (viz[to] == -1)
            dfs(to, nivel + 1);
    }
}

void reset_viz()
{
    for (int i = 1; i <= n; i++)
        viz[i] = -1;
}
int main()
{
    in >> n;
    reset_viz();
    for (int i = 0; i < n - 1; i++)
    {
        int x, y;
        in >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    //dfs 1

    dfs(1);

    reset_viz();
    //dfs 2

    dfs(nod_max);
    out << h_max + 1;
}