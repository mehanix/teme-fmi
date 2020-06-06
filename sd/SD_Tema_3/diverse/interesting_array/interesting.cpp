#include <bits/stdc++.h>

using namespace std;

struct lim
{
    int l;
    int r;
    int val;
};

vector<lim> limite;

int sume[100005][31];
int sol[100005];
int arbint[400005];
int answer;

void update(int nod, int st, int dr, int poz, int val)
{
    if (st == dr)
    {
        arbint[nod] = val;
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

    arbint[nod] = arbint[nod * 2] & arbint[nod * 2 + 1];
}

void query(int nod, int st_nod, int dr_nod, int st_query, int dr_query)
{
    if (st_query <= st_nod && dr_nod <= dr_query)
    {
        answer = answer & arbint[nod];
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
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        lim aux;
        cin >> aux.l >> aux.r >> aux.val;
        limite.push_back(aux);
        for (int b = 0; b < 30; b++)
        {
            if ((1 << b) & aux.val)
            {
                sume[aux.l][b] += 1;
                sume[aux.r + 1][b] += -1;
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int b = 0; b < 30; b++)
        {
            sume[i][b] += sume[i - 1][b];
            if (sume[i][b] > 0)
            {
                sol[i] |= 1 << b;
            }
        }
        update(1, 1, n, i, sol[i]);
    }
    for (int i = 0; i < m; i++)
    {
        answer = (1LL << 31) - 1;
        query(1, 1, n, limite[i].l, limite[i].r);
        if (answer != limite[i].val)
        {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES\n";
    for (int i = 1; i <= n; i++)
    {
        cout << sol[i] << ' ';
    }
    return 0;
}