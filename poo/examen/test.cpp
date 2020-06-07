#include <iostream>
using namespace std;

int main()
{
    int a = 20;
    int &ref = a;
    cout << a << " " << ref << endl; // 20 20
    int b = 50;
    ref = b;
    ref--;
    cout << a << " " << ref << endl; // 49 49
    return 0;
}