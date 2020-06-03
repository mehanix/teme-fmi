#include <bits/stdc++.h>

using namespace std;

const int MOD = 666013;

vector<int> hashh[MOD];
ifstream f("hashuri.in");
ofstream g("hashuri.out");

void add(int val)
{
    int m = val % MOD;

    int ok = 1;
    for (auto &x : hashh[m])
    {
        if (val == x)
        {
            ok = 0;
            break;
        }
    }
    if (ok == 1)
    {
        hashh[m].push_back(val);
    }
}
void del(int val)
{
    int m = val % MOD;

    for (auto it = hashh[m].begin(); it != hashh[m].end(); ++it)
    {
        if (val == *it)
        {
            hashh[m].erase(it);
            return;
        }
    }
}

bool fin(int val)
{
    int m = val % MOD;
    for (auto it = hashh[m].begin(); it != hashh[m].end(); ++it)
    {
        if (val == *it)
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    int n;
    f >> n;
    while (n--)
    {
        int x, y;
        f >> x >> y;
        if (x == 1)
        {
            add(y);
        }
        if (x == 2)
        {
            del(y);
        }
        if (x == 3)
        {
            g << fin(y) << '\n';
        }
    }
}