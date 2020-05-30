#include <iostream>

using namespace std;
int lastPoz[100001];
int sum[100001];
int main()
{
    int t, n;
    int nr = 0;
    cin >> n >> t;
    int v[n];

    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        lastPoz[v[i]] = i;
    }

    for (int i = n - 1; i >= 0; i--)
    {
        if (i == lastPoz[v[i]])
        {
            sum[i] = ++nr;
        }
        else
        {
            sum[i] = nr;
        }
    }
    for (int i = 0; i < t; i++)
    {
        int a;
        cin >> a;
        cout << sum[a - 1] << '\n';
        //  cout << v[i] << " " << lastPoz[v[i]] << ' ' << sum[i] << '\n';
    }
}