#include <bits/stdc++.h>

using namespace std;

ifstream f("heapuri.in");
ofstream g("heapuri.out");
multiset<int> min_heap;
vector<int> cron;

void add(int x)
{
    min_heap.insert(x);
    cron.push_back(x);
}

void del(int x)
{
    min_heap.erase(cron[x]);
}
int main()
{

    int n;
    f >> n;
    while (n--)
    {
        int c, x;
        f >> c;
        if (c == 1)
        {
            f >> x;
            add(x);
        }
        if (c == 2)
        {
            f >> x;
            del(x - 1);
        }
        if (c == 3)
        {
            g << *min_heap.begin() << '\n';
        }
    }
}