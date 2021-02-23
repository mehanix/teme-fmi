#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> g[100002];
int n, m, s;

ifstream in("bfs.in");
ofstream out("bfs.out");

queue<int> q;
int viz[100002];
int cost[100002];
int main()
{
    in >> n >> m >> s;
    for (int i = 1; i <= n; i++)
        cost[i] = -1;

    for (int i = 0; i < m; i++)
    {
        int x, y;
        in >> x >> y;
        g[x].push_back(y);
    }

    q.push(s);
    cost[s] = 0;
    while (!q.empty())
    {
        int from = q.front();
        q.pop();
        //  cout << from << " ";
        for (auto &to : g[from]) // from -> to
        {
            //   cout << to << " ";
            if (cost[to] == -1)
            {
                q.push(to);
                cost[to] = cost[from] + 1;
            }
        }
    }
    for (int i = 1; i <= n; i++)
        out << cost[i] << " ";
}