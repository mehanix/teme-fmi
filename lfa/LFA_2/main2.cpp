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
        memset(stariFinale, false, NRMAX);

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
            cout << stariFinale[i] << ' ';
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
void lambdaNFAtoNFA(Automata &a)
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
            bool isFinal = false;
            for (auto &x : a.delta[current][a.encoding[LAMBDA]])
            {
                a.lambdaInchidere[node].insert(x);
                q.push(x);

                if (a.stariFinale[x] == true)
                    isFinal = true;
            }
            /*3. calculez noile stari finale*/
            if (isFinal)
                deltaStariFinale.insert(current);
            visited[current] = true;
        }

        // adaug nodul in sine in lambda inchidere
        for (int i = 0; i < a.nrStari; i++)
            a.lambdaInchidere[i].insert(i);
    }

    //afisare
    for (int i = 0; i < a.nrStari; i++)
    {
        for (auto &x : a.lambdaInchidere[i])
            cout << x << " ";
        cout << '\n';
    }

    /*2. calculez deltaStar. iau fiecare nod din automat*/

    for (int i = 0; i < a.nrStari; i++)
    {
        cout << "pentru " << i << '\n';
        //iau lambda inchiderea fiecarui nod, si iterez prin nodurile alea
        map<char, set<int>> temp;
        for (auto &nod : a.lambdaInchidere[i])
        {
            cout << "!!" << nod << "\n";
            for (auto &ch : a.alfabet)
                temp[ch].insert(a.delta[nod][a.encoding[ch]].begin(), a.delta[nod][a.encoding[ch]].end());
        }

        //fac lambda star pt fiecare litera
        //iau litera
        for (auto &ch : a.alfabet)
        {
            //iterez prin set
            for (auto &x : temp[ch])
                //dau insert la poz i
                deltaStar[i][a.encoding[ch]].insert(a.lambdaInchidere[x].begin(), a.lambdaInchidere[x].end());
        }
    }

    /*4.1 gasesc stari redundante*/
    int newStates[a.nrStari];
    fill(newStates, newStates + a.nrStari, -1);

    for (int i = 0; i < a.nrStari; i++)
    {
        cout << i << ":";
        for (auto &ch : a.alfabet)
        {
            cout << ch << ":";
            for (auto &x : deltaStar[i][a.encoding[ch]])
                cout << x << ' ';
            cout << '\n';
        }
        cout << '\n';
    }
    //verific fiecare cu fiecare
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
    }

    for (auto &x : newStates)
        cout << x << ' ';

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
    nfa.nrMuchii = a.nrMuchii;
    nfa.nrStari = a.nrStari;
    nfa.nrStariFinale = a.nrStariFinale;
    nfa.stareInitiala = a.stareInitiala;
    for (int i = 0; i < a.nrStari; i++)
    {
        nfa.stariFinale[i] = a.stariFinale[i];
        cout << nfa.stariFinale[i] << ' ';
    }
    //nfa.stariFinale = a.stariFinale;

    for (int i = 0; i < a.nrStari; i++)
    {
        // copiem deltaStar in nfa, ignorand starile redundante
        if (i == newStates[i])
            for (auto &ch : a.alfabet)
                nfa.delta[i][a.encoding[ch]] = deltaStar[i][a.encoding[ch]];
    }
    a = nfa;
    cout << '\n';

    for (int i = 0; i < nfa.nrStari; i++)
    {
        cout << i << ":\n";
        for (auto &ch : nfa.alfabet)
        {
            if (ch != LAMBDA)
            {
                cout << ch << ":";
                for (auto &x : nfa.delta[i][a.encoding[ch]])
                    cout << x << ' ';
                cout << '\n';
            }
        }
        cout << '\n';
    }
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

int main()
{
    Automata a;

    // genereaza mapa caractere pt encoding
    generateCharacters(a);
    // populeaza automatul
    a.load();
    a.afisare();
    //lambdaNFAtoNFA(a);
    a = NFAtoDFA(a);
    a.afisare();
}