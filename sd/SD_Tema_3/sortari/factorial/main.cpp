#include <fstream>
#include <cmath>
using namespace std;
ifstream f("fact.in");
ofstream g("fact.out");

int legendre(int nr)
{
    int p = 5;
    int exp = 1;
    int result = 0;

    for (int pw = 1; pw < nr; exp++)
    {
        pw = pow(p, exp);
        result += nr / pw;
    }
    return result;
}
int cautbin(int left, int right, int n)
{
    int mid;
    int last = -1;
    while (left <= right)
    {
        mid = left + (right - left) / 2;

        int res = legendre(mid);
        if (res == n)
        {
            last = mid;
            right = mid - 1;
        }
        else if (n < res)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return last;
}
int main()
{
    int x;
    f >> x;
    int res = cautbin(0, x * 5, x);
    if (res == 0)
        g
            << 1;
    else
    {
        g << res;
    }

    f.close();
    g.close();
}