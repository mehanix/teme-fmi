#include <bits/stdc++.h>

using namespace std;

struct p
{
    int friendship;
    int money;
};
bool comp(p a, p b)
{
    return a.money < b.money;
}
vector<p> prieteni;
int main()
{
    int n, d;
    cin >> n >> d;
    for (int i = 0; i < n; i++)
    {
        p aux;
        cin >> aux.money >> aux.friendship;
        prieteni.push_back(aux);
    }
    sort(prieteni.begin(), prieteni.end(), comp);
    unsigned long long total = 0, t_max = 0;

    int i = 0;
    int j = 0;
    while (i <= j)
    {
        while (prieteni[j].money - prieteni[i].money < d && j < n)
        {
            //cout << i << ' ' << j << '\n';
            total += prieteni[j].friendship;
            t_max = max(t_max, total);
            j++;
        }
        total -= prieteni[i].friendship;
        i++;
    }
    cout << t_max;
}