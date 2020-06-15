#include <iostream>
using namespace std;

template <class X>
X f(X x, X y)
{
    return *x + *y;
}
int f(double *x, int y)
{

    return *(x + y);
}

int main()
{

    double a = 10.7, *b = new double(21);
    cout << f(*b, *b);
    return 0;
}
