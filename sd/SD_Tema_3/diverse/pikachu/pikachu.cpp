#include <bits/stdc++.h>

using namespace std;

ifstream f("pikachu.in");
ofstream g("pikachu.out");

vector<int> v;
set<int> st;
int n, k, m = 100000;
int stanga, dreapta;
int main()
{
    f >> n >> k;
    for (int i = 0; i < n; i++)
    {
        int aux;
        f >> aux;
        v.push_back(aux);
    }

    int ind = 0;
    while (ind < k)
    {
        st.insert(v[ind]);
        ind++;
    }
    /// calculez suma stanga suma dreapta
    auto it = st.begin();
    int i = 0;
    while (i < k / 2)
    {
        stanga += *it;
        it++;
        i++;
    }
    auto med = it;
    //acum, it e pe mediana
    it++;
    while (it != st.end())
    {
        dreapta += *it;
        it++;
    }
    while (ind <= n)
    {
        // for (auto &x : st)
        // {
        //     cout << x << ' ';
        // }
        //cout << "\nstanga:" << stanga << " dreapta:" << dreapta << '\n';
        //cout << "mediana:" << *med << '\n';
        // calculez pt secv curenta
        int sum = (k / 2) * (*med) - stanga + dreapta - (k - k / 2 - 1) * (*med);
        m = min(m, sum);
        // cout << "cost:" << sum << '\n'
        //      << '\n';
        //inserat, scos, recalculat mediana
        //pe ind se afla elementul de adaugat
        //pe ind-k se afla elem de scos

        //compar v[ind] cu mediana sa vad daca il pun in dreapta sau stanga

        //daca e in stanga, med++(e un iterator)
        int med_veche = *med;
        st.insert(v[ind]);

        if (v[ind] < *med)
        {
            dreapta += *med;
            med--;
            // stanga += v[ind];
            if (*med != v[ind])
            {
                stanga -= *med;
                stanga += v[ind];
            }
        }
        else
        {
            stanga += *med;
            med++;
            //dreapta += v[ind];
            if (*med != v[ind])
            {
                dreapta -= *med;
                dreapta += v[ind];
            }
        }
        if (v[ind - k] < *med)
        {
            stanga -= v[ind - k];
        }
        else
        {
            dreapta -= v[ind - k];
        }

        st.erase(v[ind - k]);

        ind++;
    }
    g << m;
}