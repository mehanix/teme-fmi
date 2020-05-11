#include <bits/stdc++.h>
using namespace std;

typedef map<string, set<string>> Grammar;
const string EPSILON = "#";
Grammar g, g1;

set<string> g_epsilon; // neterminalii din G care au N->epsilon
string g1_start;
ifstream f("input.in");

set<string> g1_symbols; //toate nodurile care vor fi in g1;
struct Automat
{
    map<string, set<pair<string, char>>> delta;
    string start;
    set<string> ends;
    int nr_stari = 0;
    int nr_muchii = 0;
} M;

int main()
{
    ////// Regular Grammar to Epsilon Free RG //////
    string lhs, rhs;
    while (f >> lhs >> rhs)
    {
        g[lhs].insert(rhs);
        // pas 1
        if (rhs != EPSILON)
        {
            g1[lhs].insert(rhs);
            g_epsilon.insert(lhs);
        }
    }

    // pas 2

    // pt fiecare N->epsilon
    for (auto &lhs : g_epsilon)
    {
        //trec prin tot mapu
        for (auto const &[key, rhs] : g1)
        {
            for (auto &x : rhs)
            {
                if (auto poz = x.find(lhs); poz != string::npos)
                {
                    // cout << lhs << ' ' << key << ' ' << x << ' ' << poz << '\n';

                    string aux = x;
                    aux.erase(poz, lhs.length());
                    g1[key].insert(aux);
                }
            }
        }
    }

    //pas 3 -> dc S are epsilon creez S1
    if (g["S"].find(EPSILON) != g["S"].end())
    {
        g1["S1"].insert(EPSILON);
        for (auto &x : g1["S"])
        {
            g1["S1"].insert(x);
        }
        g1_start = "S1";
    }
    else
    {
        g1_start = "S";
    }
    ////// END Regular Grammar to Epsilon Free RG //////

    M.start = g1_start;
    M.ends.insert("D0");
    if (g1[g1_start].find(EPSILON) != g1[g1_start].end())
        M.ends.insert(g1_start);

    //trec prin tot mapu
    for (auto const &[lhs, val] : g1)
    {
        for (auto &rhs : val)
        {
            //parsez rhs
            if (rhs != EPSILON)
            {
                if (rhs.length() == 1)
                {
                    M.delta[lhs].insert(make_pair("D0", rhs[0]));
                }
                else
                {

                    // forma xY sau Yx.. figure out which
                    int pozTerm, pozNeterm;
                    if (rhs[0] >= 'a' && rhs[0] <= 'z')
                    {
                        pozTerm = 0;
                        pozNeterm = 1;
                    }
                    else
                    {
                        pozTerm = 1;
                        pozNeterm = 0;
                    }
                    M.delta[lhs].insert(make_pair(string(1, rhs[pozNeterm]), rhs[pozTerm]));
                }
            }
        }
    }

    for (auto const &[key, rhs] : g1)
    {
        cout << key << ' ';
        for (auto &x : rhs)
        {
            cout << x << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
    cout << '\n';
    cout << '\n';

    for (auto const &[key, val] : M.delta)
    {
        for (auto &p : val)
        {
            M.nr_muchii++;
            g1_symbols.insert(key);
            g1_symbols.insert(p.first);
        }
    }
    cout << g1_symbols.size() << '\n'
         << M.nr_muchii << '\n';
    for (auto const &[key, val] : M.delta)
    {
        for (auto &p : val)
        {
            cout << key << ' ' << p.first << ' ' << p.second << '\n';
        }
    }
    cout << g1_start << '\n'
         << M.ends.size() << '\n';
    for (auto &x : M.ends)
        cout << x << ' ';
}
