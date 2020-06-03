#include <bits/stdc++.h>

using namespace std;

int deq[5000005], v[5000005]; //wow
ifstream f("deque.in");
ofstream g("deque.out");

int main()
{
    int n, k, x;
    long long s = 0;
    f >> n >> k;
    int i = 0, j = -1;
    for (int a = 1; a <= n; a++)
    {
        f >> v[a];
        if (a < k)
        {
            while (i <= j && v[deq[j]] >= v[a])
            {
                j--;
            }
            deq[++j] = a;
        }
        else
        {
            while (i <= j && v[deq[j]] >= v[a])
            {
                j--;
            }
            deq[++j] = a;
            if (a - deq[i] + 1 > k)
            {
                i++;
            }
            s += v[deq[i]];
        }
    }
    g << s;
    return 0;
}