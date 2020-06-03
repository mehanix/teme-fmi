#include <bits/stdc++.h>

using namespace std;

ifstream f("schi.in");
ofstream g("schi.out");
int answer;
int sol[30005];
int v[30005];
int arbint[120050];
void update(int nod, int st, int dr, int poz, int val)
{
    if (st == dr)
    {
        arbint[nod] = val;
        return;
    }
    int mid = (st + dr) / 2;
    if (poz <= mid)
    {
        update(2 * nod, st, mid, poz, val);
    }
    else
    {
        update(2 * nod + 1, mid + 1, dr, poz, val);
    }
    //dupa ce s-a pus 1 unde trebuie, update tot ce e in sus
    arbint[nod] = arbint[2 * nod] + arbint[2 * nod + 1];
}
void find(int nod, int st, int dr, int val)
{
    if (st == dr)
    {
        answer = st;
        return;
    }
    int mid = (st + dr) / 2;
    // if stg < val go dr
    if (arbint[2 * nod] < val)
    {
        find(2 * nod + 1, mid + 1, dr, val - arbint[2 * nod]);
    }
    else
    {
        find(2 * nod, st, mid, val);
    }
}
int main()
{
    int n;
    f >> n;
    // memset(sol, 1, n * sizeof(int));
    // suma pe intervale arbint
    for (int i = 1; i <= n; i++)
    {
        update(1, 1, n, i, 1);
    }

    for (int i = 1; i <= n; i++)
    {
        f >> v[i];
    }

    for (int i = n; i >= 1; i--)
    {
        answer = 0;
        find(1, 1, n, v[i]);
        sol[answer] = i;
        update(1, 1, n, answer, 0);
    }
    for (int i = 1; i <= n; i++)
    {
        g << sol[i] << '\n';
    }
}