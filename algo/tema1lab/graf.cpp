#include <bits/stdc++.h>

using namespace std;

vector<int> graf[14002];
const int UNVISITED = -1;
int start, endd, n, m;
int dx[14002], dy[14002];
ifstream f("graf.in");
ofstream g("graf.out");

void reset(int v[])
{
    for (int i = 0; i <= n + 1; i++)
        v[i] = UNVISITED;
}
void bfs(int start, int v[])
{
    queue<int> q;
    q.push(start);
    reset(v);
    v[start] = 0;
    while (!q.empty())
    {
        int from = q.front();
        q.pop();
        for (auto &to : graf[from])
        {
            if (v[to] == UNVISITED)
            {
                q.push(to);
                v[to] = v[from] + 1;
            }
        }
    }
}
int main()
{
    f >> n >> m >> start >> endd;
    for (int i = 1; i <= m; i++)
    {
        int x, y;
        f >> x >> y;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
    bfs(start, dx);
    bfs(endd, dy);
    //
    int sol[dx[endd] + 1];
    int total = 0;
    memset(sol, 0, sizeof(sol));
    for (int z = 1; z <= n; z++)
    {
        if (dx[z] + dy[z] == dx[endd])
        {

            if (sol[dx[z]] == 0)
            {
                total++;
            }
            else if (sol[dx[z]] == 1)
            {
                total--;
            }
            sol[dx[z]]++;
        }
    }
    g << total << '\n';
    for (int i = 1; i <= n; i++)
    {
        if (sol[dx[i]] == 1 && dx[i] + dy[i] == dx[endd])
            g << i << ' ';
    }
}