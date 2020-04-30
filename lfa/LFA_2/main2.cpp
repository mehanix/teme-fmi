#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
ifstream f("automat.in");

const int NRMAX = 500;
const int LENALFA = 37;
const int NRCHAR = 37;
const char LAMBDA = '$';
struct Automata
{

    map<char, int> encoding;
    set<char> alfabet; //alfabet
    int nrStari;
    int nrMuchii;
    int nrStariFinale;
    set<int> delta[NRMAX][LENALFA]; //matrice de adiacenta

    set<int> lambdaInchidere[NRMAX];
    bool stariFinale[NRMAX];
    int stareInitiala;

    /* Loads automata data into memory */

    void load()
    {
        f >> nrStari >> nrMuchii;
        memset(stariFinale, false, sizeof(stariFinale));

        for (int i = 0; i < nrMuchii; i++)
        {
            int q1, q2;
            char c;
            f >> q1 >> q2 >> c;
            // cu nod 1 si caracter c ajungi in nod 2
            delta[q1][encoding[c]].insert(q2);
            alfabet.insert(c);
        }
        f >> stareInitiala >> nrStariFinale;
        int aux;
        for (int i = 0; i < nrStariFinale; i++)
        {
            f >> aux;
            stariFinale[aux] = true;
        }
    }

    void afisare()
    {
        cout << nrStari << '\n'
             << nrMuchii << '\n';
        for (int q1 = 0; q1 < nrStari; q1++)
        {
            for (auto &ch : alfabet)
            {
                if (!delta[q1][encoding[ch]].empty())
                    for (auto &q2 : delta[q1][encoding[ch]])
                        cout << q1 << ' ' << q2 << ' ' << ch << '\n';
            }
        }
        cout << stareInitiala << '\n'
             << nrStariFinale << '\n';
        for (int i = 0; i < nrStari; i++)
            if (stariFinale[i])
                cout << i << ' ';
        cout << "\n\n\n";
    }
};

/*Generates encoding for each possible character*/
void generateCharacters(Automata &a)
{
    int c = 0;
    for (char letter = 'a'; letter <= 'z'; letter++)
        a.encoding[letter] = c++;
    for (char letter = 'A'; letter <= 'Z'; letter++)
        a.encoding[letter] = c++;
    for (int letter = 0; letter <= 9; letter++)
        a.encoding[letter] = c++;

    a.encoding[LAMBDA] = c++;
}

bool isEqual(int q1, int q2, set<int> delta[NRMAX][LENALFA], Automata &a)
{
    for (auto &c : a.alfabet)
        if (c != LAMBDA)
            if (!(delta[q1][a.encoding[c]] == delta[q2][a.encoding[c]]))
                return false;
    return true;
}

/* turns lambda NFA to NFA*/
Automata lambdaNFAtoNFA(Automata &a)
{
    set<int> deltaStar[NRMAX][LENALFA]; //matrice de adiacenta
    set<int> deltaStariFinale;
    /*1. calculeaza lambda inchiderea fiecarui*/
    for (int node = 0; node < a.nrStari; node++)
    {
        queue<int> q;
        bool visited[a.nrStari];
        memset(visited, 0, sizeof(visited));
        q.push(node);

        while (!q.empty())
        {
            int current = q.front();
            q.pop();

            //iau unde poti sa te duci din el cu lambda si bag in inchidere si queue
            for (auto &x : a.delta[current][a.encoding[LAMBDA]])
            {
                a.lambdaInchidere[node].insert(x);
                q.push(x);
            }
            visited[current] = true;
        }

        // adaug nodul in sine in lambda inchidere
        for (int i = 0; i < a.nrStari; i++)
            a.lambdaInchidere[i].insert(i);
    }

    for (int i = 0; i < a.nrStari; i++)
    {
        for (auto &x : a.lambdaInchidere[i])
            if (a.stariFinale[x] == true)
                deltaStariFinale.insert(i);
    }

    // cout << "DeltaStariFinale:";
    // for (auto &x : deltaStariFinale)
    //     cout << x << ' ';
    // cout << "\n";

    // //afisare
    // for (int i = 0; i < a.nrStari; i++)
    // {
    //     for (auto &x : a.lambdaInchidere[i])
    //         cout << x << " ";
    //     cout << '\n';
    // }

    /*2. calculez deltaStar. iau fiecare nod din automat*/

    for (int i = 0; i < a.nrStari; i++)
    {
        //iau lambda inchiderea fiecarui nod, si iterez prin nodurile alea
        map<char, set<int>> temp;
        for (auto &nod : a.lambdaInchidere[i])
        {
            for (auto &ch : a.alfabet)
                temp[ch].insert(a.delta[nod][a.encoding[ch]].begin(), a.delta[nod][a.encoding[ch]].end());
        }

        //fac lambda star pt fiecare litera
        //iau litera
        for (auto &ch : a.alfabet)
        {
            if (ch != LAMBDA)
            {
                //iterez prin set
                for (auto &x : temp[ch])
                    //dau insert la poz i
                    deltaStar[i][a.encoding[ch]].insert(a.lambdaInchidere[x].begin(), a.lambdaInchidere[x].end());
            }
        }
    }

    /*4.1 gasesc stari redundante*/
    int newStates[a.nrStari];
    fill(newStates, newStates + a.nrStari, -1);

    // for (int i = 0; i < a.nrStari; i++)
    // {
    //     cout << i << ":";
    //     for (auto &ch : a.alfabet)
    //     {
    //         cout << ch << ":";
    //         for (auto &x : deltaStar[i][a.encoding[ch]])
    //             cout << x << ' ';
    //         cout << '\n';
    //     }
    //     cout << '\n';
    // }
    //verific fiecare cu fiecare
    map<int, int> rename;
    int nod = 0;
    for (int i = 0; i < a.nrStari; i++)
    {
        if (newStates[i] != -1)
            continue;

        for (int j = i + 1; j < a.nrStari; j++)
        {
            //daca starea j identica cu starea i pt fiecare litera din alfabet
            if (isEqual(i, j, deltaStar, a))
            {
                // i < j -> toate aparitiile lui j devin i
                newStates[j] = i;
            }
        }
        // daca e unica, se pastreaza
        newStates[i] = i;
        rename[i] = nod++;
    }

    /*4.2 elimin stari redundante*/

    //inlocuiesc aparitiile starilor redundante in deltaStar
    //iau fiecare nod
    for (int i = 0; i < a.nrStari; i++)
    {
        // iau fiecare litera
        for (auto &ch : a.alfabet)
        {
            set<int> temp;
            //iau fiecare element din set
            for (auto &j : deltaStar[i][a.encoding[ch]])
            {
                temp.insert(newStates[j]);
            }
            deltaStar[i][a.encoding[ch]] = temp;
        }
    }

    Automata nfa;
    nfa.alfabet = a.alfabet;
    nfa.encoding = a.encoding;
    //nfa.lambdaInchidere = a.lambdaInchidere;
    nfa.nrStari = 0;
    nfa.nrMuchii = 0;
    nfa.nrStariFinale = a.nrStariFinale;
    nfa.stareInitiala = rename[a.stareInitiala];
    for (int i = 0; i < a.nrStari; i++)
    {
        if (newStates[i] == i)
            nfa.nrStari++;
        if (a.stariFinale[i] == true && newStates[i] == i)
            nfa.stariFinale[rename[i]] = true;

        // cout << nfa.stariFinale[i] << ' ';
    }
    //nfa.stariFinale = a.stariFinale;

    for (int i = 0; i < a.nrStari; i++)
    {
        // copiem deltaStar in nfa, ignorand starile redundante
        if (i == newStates[i])
            for (auto &ch : a.alfabet)
                for (auto &x : deltaStar[i][a.encoding[ch]])
                {
                    nfa.delta[rename[i]][a.encoding[ch]].insert(rename[x]);
                    nfa.nrMuchii++;
                }
    }
    //cout << '\n';

    // for (int i = 0; i < nfa.nrStari; i++)
    // {
    //     cout << i << ":\n";
    //     for (auto &ch : nfa.alfabet)
    //     {
    //         if (ch != LAMBDA)
    //         {
    //             cout << ch << ":";
    //             for (auto &x : nfa.delta[i][a.encoding[ch]])
    //                 cout << x << ' ';
    //             cout << '\n';
    //         }
    //     }
    //     cout << '\n';
    // }

    //stari finale
    nfa.nrStariFinale = 0;
    for (auto &x : deltaStariFinale)
    {
        if (newStates[x] == x)
        {
            nfa.stariFinale[rename[x]] = true;
            nfa.nrStariFinale++;
        }
    }
    return nfa;
}

/*turns NFA to DFA */
Automata NFAtoDFA(Automata &a)
{
    //pas 1
    vector<set<int>> q;
    set<int> start;
    start.insert(a.stareInitiala);
    q.push_back(start);
    Automata dfa;
    dfa.alfabet = a.alfabet;
    dfa.encoding = a.encoding;
    //nfa.lambdaInchidere = a.lambdaInchidere;
    dfa.nrStari = a.nrStari;
    dfa.stareInitiala = a.stareInitiala;
    memset(dfa.stariFinale, false, NRMAX);

    int nrMuchii = 0;
    int nrStariFinale = 0;
    int i = 0;
    while (i < q.size())
    {
        for (auto &ch : a.alfabet)
        {
            set<int> temp;
            bool isFinal = false;
            for (auto &st : q[i])
            {
                if (a.stariFinale[st])
                    dfa.stariFinale[i] = true;
                temp.insert(a.delta[st][a.encoding[ch]].begin(), a.delta[st][a.encoding[ch]].end());
            }
            if (temp.empty())
                continue;

            bool found = false;
            for (int ii = 0; ii < q.size(); ii++)
            {
                if (q[ii] == temp)
                {
                    dfa.delta[i][a.encoding[ch]].insert(ii);
                    nrMuchii++;
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                q.push_back(temp);
                nrMuchii++;
                dfa.delta[i][a.encoding[ch]].insert(q.size() - 1);
            }
        }
        i++;
    }

    dfa.nrStari = q.size();
    dfa.stareInitiala = a.stareInitiala;
    dfa.nrMuchii = nrMuchii;
    for (int i = 0; i < dfa.nrStari; i++)
        nrStariFinale += dfa.stariFinale[i];
    dfa.nrStariFinale = nrStariFinale;
    return dfa;
}

bool mat[NRMAX][NRMAX];
Automata DFAtoDFAmin(Automata &a)
{
    auto print = [=]() {
        for (int i = 0; i < a.nrStari; i++)
        {
            for (int j = 0; j < i; j++)
                cout << mat[i][j] << ' ';
            cout << '\n';
        }
    };

    for (int i = 0; i < a.nrStari; i++)
        for (int j = 0; j < a.nrStari; j++)
            mat[i][j] = true;

    //marchez perechi diferite
    for (int i = 0; i < a.nrStari; i++)
        for (int j = 0; j < i; j++)
        {
            if (a.stariFinale[i] != a.stariFinale[j])
            {
                mat[i][j] = false;
                mat[j][i] = false;
            }
        }

    bool modified;
    do
    {
        modified = false;
        for (int i = 0; i < a.nrStari; i++)
            for (int j = 0; j < i; j++)
            {
                bool isFalse = false;

                for (auto &ch : a.alfabet)
                {
                    if (a.delta[i][a.encoding[ch]].size() == 0 || a.delta[j][a.encoding[ch]].size() == 0)
                        continue;
                    int x = *a.delta[i][a.encoding[ch]].begin();
                    int y = *a.delta[j][a.encoding[ch]].begin();
                    if (x < y)
                        swap(x, y);
                    if (mat[x][y] == false)
                    {
                        isFalse = true;
                    }
                }
                if (isFalse == true && mat[i][j] == true)
                {
                    modified = true;
                    mat[i][j] = false;
                    break;
                }

                if (modified)
                    break;
            }
    } while (modified == true);

    // pas 2
    vector<set<int>> multimi;
    for (int i = 0; i < a.nrStari; i++)
    {
        bool foundOne = false;

        for (int j = 0; j < i; j++)
        {
            if (mat[i][j] == true)
            {
                for (auto &s : multimi)
                {
                    if (s.find(j) != s.end())
                    {
                        s.insert(i);
                        foundOne = true;
                        break;
                    }
                }
            }
        }
        if (foundOne == false)
        {
            set<int> aux;
            aux.insert(i);
            multimi.push_back(aux);
        }
    }

    Automata dfaMin;
    dfaMin.alfabet = a.alfabet;
    dfaMin.encoding = a.encoding;

    memset(dfaMin.stariFinale, false, sizeof(dfaMin.stariFinale));

    for (int i = 0; i < multimi.size(); i++)
    {
        for (auto &ch : a.alfabet)
        {
            set<int> temp;
            for (auto &x : multimi[i])
            {
                bool found = false;
                if (a.delta[x][a.encoding[ch]].size() > 0)
                {
                    for (int j = 0; j < multimi.size(); j++)
                        if (multimi[j].find(*(a.delta[x][a.encoding[ch]].begin())) != multimi[j].end())
                        {
                            found = true;
                            dfaMin.delta[i][a.encoding[ch]].insert(j);
                            // cout << i << "->" << j << ' ' << ch << '\n';
                            break;
                        }
                }
                if (found)
                    break;
                //temp.insert(*(a.delta[x][a.encoding[ch]].begin()));
            }
            // for (int j = 0; j < multimi.size(); j++)
            //     if (multimi[j] == temp)
            //     {
            //         dfaMin.delta[i][a.encoding[ch]].insert(j);
            //         cout << i << "->" << j << '\n';
            //     }
        }
    }
    dfaMin.nrStari = multimi.size();
    //pasul 3

    for (int i = 0; i < multimi.size(); i++)
    {
        for (int j = 0; j < a.nrStari; j++)
        {
            if (a.stariFinale[j] == true)
                if (multimi[i].find(j) != multimi[i].end() && dfaMin.stariFinale[i] == false)
                {
                    dfaMin.stariFinale[i] = true;
                    dfaMin.nrStariFinale++;
                }
        }

        if (multimi[i].find(a.stareInitiala) != multimi[i].end())
            dfaMin.stareInitiala = i;
    }
    return dfaMin;
}
int main()
{
    Automata a;

    // genereaza mapa caractere pt encoding
    generateCharacters(a);
    // populeaza automatul
    a.load();
    a.afisare();
    //a = lambdaNFAtoNFA(a);
    //a = NFAtoDFA(a);
    a = DFAtoDFAmin(a);
    a.afisare();
}