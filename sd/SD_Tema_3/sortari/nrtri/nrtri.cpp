#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int aux;
vector<int> v;
ifstream f("nrtri.in");
ofstream g("nrtri.out");

int sum = 0;

int cautbin(int l, int r, int nr)
{
    int last = -1;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        if (v[mid] == nr)
        {
            last = mid;
            l = mid + 1;
        }
        else if (nr < v[mid])
        {
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
            last = mid;
        }
    }
    return last;
}
int main()
{
    int nr;
    f >> nr;
    int x = 0;
    for (int i = 0; i < nr; i++)
    {
        f >> aux;
        v.push_back(aux);
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < nr - 2; i++)
    {
        for (int j = i + 1; j < nr - 1; j++)
        {
            int head = v[i] + v[j];
            int c = cautbin(j, nr - 1, head);
            if (c - j > 0)
            {
                sum += c - j;
            }
        }
    }
    g << sum;
}