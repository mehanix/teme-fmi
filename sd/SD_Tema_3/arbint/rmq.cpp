#include <bits/stdc++.h>

using namespace std;

ifstream f("rmq.in");
ofstream g("rmq.out");
int mat[100005][20];
int main()
{
    int n, m;
    f >> n >> m;
    for (int i = 0; i < n; i++)
    {
        f >> mat[i][0];
    }
    for (int j = 1; j < 20; j++)
    {
        for (int i = 0; i + (1 << j) - 1 < n; i++)
        {
            mat[i][j] = min(mat[i][j - 1], mat[i + (1 << (j - 1))][j - 1]);
        }
    }
    while (m--)
    {
        int a, b;
        f >> a >> b;
        b--;
        a--;
        int lg = log2(b - a + 1);
        int x = b - (1 << lg) + 1;
        g << min(mat[a][lg], mat[x][lg]) << '\n';
    }
    return 0;
}