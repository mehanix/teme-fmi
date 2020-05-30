#include <iostream>

using namespace std;

long long nr;
int n;
int v[10];

void calculeaza(long long nr)
{
    while (nr > 0)
    {
        int c = nr % 10;
        nr = nr / 10;

        if (c == 2 || c == 3 || c == 5 || c == 7)
        {
            v[c]++;
        }
        else
            switch (c)
            {
            case 4:
                v[3]++;
                v[2] += 2;
                break;
            case 6:
                v[5]++;
                v[3]++;
                break;

            case 8:
                v[7]++;
                v[2] += 3;
                break;
            case 9:
                v[7]++;
                v[3] += 2;
                v[2]++;
                break;
            }
    }
}
int main()
{
    cin >> n >> nr;
    calculeaza(nr);

    for (int i = 9; i >= 2; i--)
    {
        while (v[i] > 0)
        {
            v[i]--;
            cout << i;
        }
    }
    cout << '\n';
}