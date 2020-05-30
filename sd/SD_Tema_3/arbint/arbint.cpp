#include <bits/stdc++.h>

using namespace std;

int v[400050];
ifstream f("arbint.in");
ofstream g("arbint.out");

int answer;

void update(int nod, int st, int dr, int poz, int val)
{
    if (st == dr)
    {
        v[nod] = val;
        return;
    }
    int mij = (st + dr) / 2;
    if (poz <= mij)
    {
        update(2 * nod, st, mij, poz, val);
    }
    else
    {
        update(2 * nod + 1, mij + 1, dr, poz, val);
    }

    v[nod] = max(v[nod * 2], v[nod * 2 + 1]);
}

void query(int nod, int st_nod, int dr_nod, int st_query, int dr_query)
{
    if (st_query <= st_nod && dr_nod <= dr_query)
    {
        answer = max(answer, v[nod]);
        return;
    }
    int mid = (st_nod + dr_nod) / 2;
    if (st_query <= mid)
        query(2 * nod, st_nod, mid, st_query, dr_query);
    if (mid + 1 <= dr_query)
        query(2 * nod + 1, mid + 1, dr_nod, st_query, dr_query);
}
int main()
{
    int n, m;
    f >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        int x;
        f >> x;
        update(1, 1, n, i, x);
    }
    while (m--)
    {
        int q, a, b;
        f >> q >> a >> b;
        if (q == 0)
        {
            query(1, 1, n, a, b);
            g << answer << '\n';
            answer = -1;
        }
        else
        {
            update(1, 1, n, a, b);
        }
    }
}