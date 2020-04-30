#include <iostream>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

const int NRMAX = 500;

struct Muchie
{
    int dest;
    char letter;
};

struct Automata
{
    int nrStari;
    int nrMuchii;
    int nrStariInitiale;
    int nrStariFinale;

    set<Muchie> g[NRMAX];
    bool stariInitiale[NRMAX], stariFinale[NRMAX];

    //todo add
};

void lambdaNFAtoNFA(Automata &a)
{
    for (int v1 = 0; v1 < a.nrStari; v1++)
    {
        // adauga muchii noi unde aveam #
        set<Muchie> toBeAdded;
        for (Muchie &m : g[v1])
        {
            if (m.letter == '#')
            {
                int v2 = m.dest;
                for (Muchie &m2 : g[v2])
                {
                    toBeAdded.insert(m2);
                }

                // step 3
                if (a.stariInitiale[v1] == true)
                    a.stariInitiale[m.dest] = true;

                // step 4
                if (a.stariFinale[m.dest] == true)
                    a.stariFinale[v1] = true;
            }
        }
        // sterge muchii #
        bool deleted = false;
        do
        {
            deleted = false;
            for (auto it = a.g[v1].begin(); it != a.g[v1].end(); it++)
            {
                if ((*it).letter == '#')
                {
                    a.g[v1].erase(it);
                    deleted = true;
                }
            }
        } while (deleted == true);

        for (auto &m : toBeAdded)
        {
            a.g[v1].insert(m);
        }
    }
}

void NFAtoDFA(Automata &a)
{
    Automata b;
    vector<set<int>> q;

    // adaug noduri start
    for (int i = 0; i < NRMAX; i++)
        if (a.stariInitiale[i] == true)
        {
            q.push_back(set<int>(1, i));
            b.stariInitiale[q.size() - 1] = true;
        }
    b.nrStariInitiale = a.nrStariInitiale;
    int index = 0;
    while (index < q.size())
    {
        bool eStareFinala = false;
        //lista cu nodul/nodurile starii curente
        set<int> current = q[index];
        map<char, set<int>> temp;

        // iterez prin elem din starea curenta
        for (auto &n : current)
        {

            if (a.stariFinale[n] == true)
            {
                eStareFinala = true;
            }
            // creez tempstates

            // iterez prin muchii
            for (auto &m : a.g[n])
            {
                temp[m.letter].insert(m.dest);
            }
        }

        // iterez prin starile noi
        for (auto it = temp.begin(); it != temp.end(); ++it)
        {
            // daca nu e deja tratata
            if (find(q.begin(), q.end(), it->second) != q.end())
            {
                //adauga starea noua in queue
                q.push_back(it->second);
                b.g[index].insert({q.size() - 1, it->first});
            }
        }
        index++;
        b.nrStariFinale += eStareFinala;
        b.stariFinale[index] = eStareFinala;
    }
}

int main()
{
}