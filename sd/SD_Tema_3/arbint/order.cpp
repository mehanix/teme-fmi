#include <bits/stdc++.h>

using namespace std;

ifstream f("order.in");
ofstream g("order.out");

int arbint[120005];
int answer;
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
void query(int nod, int st_nod, int dr_nod, int st_query, int dr_query)
{
    if (st_query <= st_nod && dr_nod <= dr_query)
    {
        answer += arbint[nod];
        return;
    }
    int mid = (st_nod + dr_nod) / 2;
    if (st_query <= mid)
        query(2 * nod, st_nod, mid, st_query, dr_query);
    if (mid + 1 <= dr_query)
        query(2 * nod + 1, mid + 1, dr_nod, st_query, dr_query);
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
    // arbint sume partiale
    for (int i = 1; i <= n; i++)
    {
        update(1, 1, n, i, 1);
    }
    int curent = 1;
    for (int i = 1; i <= n; i++)
    {
        answer = 0;
        query(1, 1, n, 1, curent);
        int add = answer;
        answer = 0;
        int pas;
        if ((i + add) % (n - i + 1) == 0)
        {
            pas = n - i + 1;
        }
        else
        {
            pas = (i + add) % (n - i + 1);
        }

        find(1, 1, n, pas);
        g << answer << ' ';
        update(1, 1, n, answer, 0);
        curent = answer;
    }
}