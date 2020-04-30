#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
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

        for (int aux, i = 0; i < nrStariFinale; i++)
        {
            f >> aux;
            stariFinale[aux] = true;
        }
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
    /*for (int i = 0; i < a.nrStari; i++)
    {
        cout << i << ":";
        for (auto &ch : a.alfabet)
        {
            cout << ch << ":";
            for (auto &x : a.delta[i][a.encoding[ch]])
                cout << x << ' ';
            cout << '\n';
        }
        cout << '\n';
    }*/
    /*1. calculeaza lambda inchiderea fiecarui*/
    for (int node = 0; node < a.nrStari; node++)
    {
        queue<int> q;
        bool visited[a.nrStari] = {false};
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
    //algoritmul secolului
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
                //deltaStar[i][a.encoding[ch]].erase(j);
                //deltaStar[i][a.encoding[ch]].insert(newStates[j]);
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
void NFAtoDFA(Automata &a)
{
    Automata b;
    vector<set<int>> q;
    set<int> t;
    t.insert(a.stareInitiala);
    q.push_back(t);
    int index = 0;
    int count = 0;
    map<set<int>, int> states;
    while (index < q.size())
    {
        // iau starea curent
        set<int> current = q[index];
        if (!current.empty())
        {
            cout << count << ". pentru ";
            for (auto &c : current)
            {
                cout << c << " ";
            }
            cout << '\n';

            bool isFinalState = false;
            b.nrStari++;

            // iau fiecare elem din starea curenta
            map<char, set<int>> temp;

            for (auto &x : current)
            {
                if (a.stariFinale[x] == true)
                {
                    isFinalState = true;
                }
                for (auto &ch : a.alfabet)
                {
                    for (auto &n : a.delta[x][a.encoding[ch]])
                    {
                        // cout << "cu " << ch << " ajung in " << n << "\n";
                        temp[ch].insert(n);
                    }
                }
            }
            cout << "temp\n";
            for (auto &ch : a.alfabet)
            {
                cout << ch;
                for (auto &s : temp[ch])
                {
                    cout << s;
                }
                cout << "\n";
            }
            cout << "\n";

            //bag starea in automat
            for (auto &c : a.alfabet)
            {
                states[temp[c]] = count;
                b.delta[count][a.encoding[c]].insert(temp[c].begin(), temp[c].end());
            }
            count++;
            //vad de ce stari noi mai am nevoie in continuare
            for (auto &ch : a.alfabet)
            {
                if (find(q.begin(), q.end(), temp[ch]) == q.end())
                {
                    q.push_back(temp[ch]);
                    cout << "gasit ";
                    for (auto &a : temp[ch])
                        cout << a;
                    cout << '\n';
                }
            }
        }
        else
        {
            count++;
        }
        index++;
    }

    b.nrStari = count;

    b.stareInitiala = a.stareInitiala;
    for (auto &x : a.stariFinale)
    {
        b.stariFinale[x] = true;
    }

    // a = b;
    for (int i = 0; i < b.nrStari; i++)
    {
        cout << i << ":";
        for (auto &ch : a.alfabet)
        {
            cout << ch << ":";
            for (auto &x : b.delta[i][a.encoding[ch]])
                cout << x << ' ';
            cout << '\n';
        }
        cout << '\n';
    }
}

int main()
{
    Automata a;

    // genereaza mapa caractere pt encoding
    generateCharacters(a);
    // populeaza automatul
    a.load();

    //lambdaNFAtoNFA(a);
    NFAtoDFA(a);
}