#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream f("binar.in");
ofstream g("binar.out");

int main()

{

    int t, c;

    string aux;

    f >> t >> c;

    vector<pair<char, int>> words(c);

    for (int i = 0; i < c; i++)

    {

        words[i].second = i;
    }

    for (int p = 0; p < t; p++)

    {

        f >> aux;

        int len = aux.length();

        for (int i = 0; i < len; i++)

            words[i].first += aux[i];
    }

    sort(words.begin(), words.end());

    for (auto &x : words)

        g << x.second + 1 << ' ';
}