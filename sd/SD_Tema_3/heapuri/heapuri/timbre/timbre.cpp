#include <bits/stdc++.h>

using namespace std;

struct p
{
    int index;
    int dreapta;
    int cost;
};
class comp
{
public:
    bool operator()(p a, p b)
    {
        return a.cost > b.cost;
    }
};

bool compDreapta(p a, p b)
{
    return a.dreapta > b.dreapta;
}
priority_queue<p, vector<p>, comp> heap;

ifstream f("timbre.in");
ofstream g("timbre.out");
vector<p> inter;

int main()
{
    int n, m, k;
    int cost = 0;
    f >> n >> m >> k;
    for (int i = 1; i <= m; i++)
    {
        p aux;
        f >> aux.dreapta >> aux.cost;
        aux.index = i;
        inter.push_back(aux);
    }

    //sortez descrescator dupa capat dreapta
    sort(inter.begin(), inter.end(), compDreapta);
    int nivel = n;
    int curent = 0;
    while (nivel > 0)
    {
        while (curent < m && inter[curent].dreapta >= nivel)
        {
            heap.push(inter[curent]);
            curent++;
        }
        p ales = heap.top();
        cost += ales.cost;
        nivel -= k;
        heap.pop();
    }
    g << cost;
}