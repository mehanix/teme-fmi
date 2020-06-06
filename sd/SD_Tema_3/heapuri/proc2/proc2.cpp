#include <bits/stdc++.h>

using namespace std;

ifstream f("proc2.in");
ofstream g("proc2.out");

struct proc
{
    int index;
    int timp;
};

class compTimp
{
public:
    bool operator()(proc a, proc b)
    {
        return a.timp > b.timp;
    }
};
class compIndex
{
public:
    bool operator()(proc a, proc b)
    {
        return a.index > b.index;
    }
};
priority_queue<proc,
               vector<proc>, compIndex>
    heap_liber;
priority_queue<proc,
               vector<proc>, compTimp>
    heap_busy;

int main()
{
    int n, m;
    f >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        proc aux;
        aux.index = i;
        aux.timp = 0;
        heap_liber.push(aux);
    }
    while (m--)
    {
        int s, d;
        f >> s >> d;
        while (!heap_busy.empty() && heap_busy.top().timp < s)
        {
            heap_liber.push(heap_busy.top());
            heap_busy.pop();
        }
        proc ales = heap_liber.top();
        heap_liber.pop();
        g << ales.index << "\n";
        ales.timp = s + d - 1;
        heap_busy.push(ales);
    }
}