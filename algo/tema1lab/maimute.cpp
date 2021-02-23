#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

ifstream in("maimute.in");
ofstream out("maimute.out");

vector<int> g[100002];
int intrare[100002], iesire[100002];
int n, m, t;

void dfs(int from)
{
    t++;
    intrare[from] = t;
    for (auto &to : g[from])
    {
        if (intrare[to] == 0)
            dfs(to);
    }
    iesire[from] = t;
}

bool isStramos(int x, int y)
{
    //x stramos lu y
    if (intrare[y] <= intrare[x] && iesire[x] <= iesire[y])
        return true;
    return false;
}
int main()
{
    in >> n;
    t = 0;
    for (int i = 0; i < n - 1; i++)
    {
        int x, y;
        in >> x >> y;
        g[y].push_back(x);
        g[x].push_back(y);
    }
    dfs(1);

    int nr;
    in >> nr;
    while (nr--)
    {
        int x, y;
        in >> x >> y;
        if (isStramos(x, y) || isStramos(y, x))
            out << "DA\n";
        else
        {
            out << "NU\n";
        }
    }
}