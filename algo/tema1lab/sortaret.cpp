#include <fstream>

#include <iostream>

#include <vector>

#include <queue>

using namespace std;

ifstream in("sortaret.in");

ofstream out("sortaret.out");

vector<int> g[100002];

int viz[100002];

int n, m;

void dfs(int from)

{

    viz[from] = 1;

    for (auto &to : g[from])

    {

        if (viz[to] == 0)

            dfs(to);
    }

    out << from << ' ';
}

int main()

{

    in >> n >> m;

    for (int i = 0; i < m; i++)

    {

        // fac graful pe dos

        int x, y;

        in >> x >> y;

        g[y].push_back(x);
    }

    for (int i = 1; i <= n; i++)

    {

        if (viz[i] == 0)

        {

            dfs(i);
        }
    }
}