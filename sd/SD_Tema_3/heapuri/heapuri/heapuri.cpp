#include <bits/stdc++.h>

using namespace std;

ifstream f("heapuri.in");
ofstream g("heapuri.out");
priority_queue<int, vector<int>, greater<int>> min_heap;
int v[200005];
void add(int x)
{
    min_heap.push(x);
}

void del(int x)
{
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
            del(caut(x));
        }
        if (c == 3)
        {
            g << min_heap.top() << '\n';
        }
    }
}