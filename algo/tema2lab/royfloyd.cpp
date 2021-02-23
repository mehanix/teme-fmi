#include <bits/stdc++.h>

using namespace std;

int graf[105][105];
int n;
ifstream f("royfloyd.in");
ofstream g("royfloyd.out");
int main()
{
    f>>n;
    for(int i=1;i<=n;i++) {
        for(int j=1;j<=n;j++) {
            f>>graf[i][j];
            if(graf[i][j] == 0 && i!=j) {
                graf[i][j] = INT_MAX/2;
            }
        }
    }

    for(int k=1;k<=n;k++) {
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=n;j++) {
                graf[i][j] = min(graf[i][j],graf[i][k]+graf[k][j]);
            }
        }
    }
    for(int i=1;i<=n;i++) {
        for(int j=1;j<=n;j++) {
            if(graf[i][j]==INT_MAX/2)
                g<<"0 ";
            else
                g<<graf[i][j]<<' ';
        }
        g<<"\n";
    }
}