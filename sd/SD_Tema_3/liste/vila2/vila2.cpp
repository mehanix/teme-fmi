#include <bits/stdc++.h>

using namespace std;

ifstream f("vila2.in");
ofstream g("vila2.out");

deque<int> deq_min; // min pe interval cu lungime k+1
deque<int> deq_max; // max pe interval ...

int v[100005], minn, maxx, dif_max = -9999999;
int main()
{
    int n, k;
    f >> n >> k;
    k++;
    for (int i = 1; i <= n; i++)
    {
        f >> v[i];

        //min
        while (!deq_min.empty() && v[deq_min.back()] >= v[i])
        {
            deq_min.pop_back();
        }
        deq_min.push_back(i);
        if ((deq_min.back() - deq_min.front() + 1) > k)
            deq_min.pop_front();

        //max
        while (!deq_max.empty() && v[deq_max.back()] <= v[i])
        {
            deq_max.pop_back();
        }
        deq_max.push_back(i);
        if ((deq_max.back() - deq_max.front() + 1) > k)
            deq_max.pop_front();

        dif_max = max(dif_max, v[deq_max.front()] - v[deq_min.front()]);
    }
    g << dif_max;
}