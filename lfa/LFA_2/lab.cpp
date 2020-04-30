#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

template <class T>
class Exemplu
{
    static int i;

public:
    Exemplu()
    {
        i++;
        cout << i << '\n';
    }
    static int get_i()
    {
        return i;
    }
};
template <class T>
int Exemplu<T>::i = 0;

template <class A>
std::vector<A> MySort(std::vector<A> v)
{
    std::sort(v.rbegin(), v.rend());
    return v;
}

template <>
std::vector<char> MySort<char>(std::vector<char> v)
{
    int f[255];
    memset(f, 0, sizeof(f));

    for (int i = 0; i < v.size(); i++)
    {
        f[v[i]]++;
    }

    std::vector<char> sorted;
    for (int i = 0; i < 255; i++)
    {
        while (f[i]--)
        {
            sorted.push_back(i);
        }
    }

    return sorted;
}

template <class B, int x>
void afis(vector<B> v)
{
    for (int i = 0; i < min(x, (int)v.size()); ++i)
        cout << v[i] << " ";
}

int main()
{
    /*Exemplu<int> a;
   Exemplu<int> b;
   Exemplu<char> c;
   cout << Exemplu<int>::get_i() << '\n';
   cout << Exemplu<char>::get_i() << '\n';*/
    /* vector<int> v = MySort<int>({1,-9,-8,4,5});
   for(auto i:v)
        cout << i << "  ";

    vector<char> c = MySort<char>({'a','9', '.', 'A', 'z'});
   for(auto i:c)
        cout << i << "  ";

*/
    //afis<char, 4>({'m', '?', '5', '[', 'T', 'U'});

    vector<int> v = {1, 5, 9, 8, -9, -8, 7, 44};

    auto mySort2 = [&v]() {
        sort(v.begin(), v.end());
    };
    for_each(v.begin(), v.end(), [](int a) { cout << a << " "; });
    cout << "\n";
    mySort2();
    for_each(v.begin(), v.end(), [](int a) { cout << a << " "; });
    return 0;
}
