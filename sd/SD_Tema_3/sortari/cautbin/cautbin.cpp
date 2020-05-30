#include <fstream>

using namespace std;

ifstream f("cautbin.in");
ofstream g("cautbin.out");

int nrElem, v[100001], t;

int findMax(int nr, int l, int r)
{
    int last = -2;
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
        }
    }
    return last + 1;
}

int ex1(int nr, int l, int r)
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
    return last + 1;
}

int ex2(int nr, int l, int r)
{
    int last = -1;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        if (v[mid] == nr)
        {
            last = mid;
            r = mid - 1;
        }
        else if (nr < v[mid])
        {
            r = mid - 1;
            last = mid;
        }
        else
        {
            l = mid + 1;
        }
    }
    return last + 1;
}

int main()
{
    f >> nrElem;
    for (int i = 0; i < nrElem; i++)
    {
        f >> v[i];
    }

    f >> t;
    while (t > 0)
    {
        t--;
        int tip, x;
        f >> tip >> x;

        switch (tip)
        {
        case 0:
            g << findMax(x, 0, nrElem - 1) << '\n';
            break;
        case 1:
            g << ex1(x, 0, nrElem - 1) << '\n';
            break;
        case 2:
            g << ex2(x, 0, nrElem - 1) << '\n' break;
        }
    }
}