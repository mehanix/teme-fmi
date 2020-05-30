#include <cstdio>

using namespace std;

int main()
{
    int t, n, k;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d%d", &n, &k);
        if (n % 2 == k % 2 && 1LL * k * k <= n)
            printf("YES\n");

        else
            printf("NO\n");
    }
}