// aoleu
#include <bits/stdc++.h>

using namespace std;

deque<int> st;
ifstream f("alibaba.in");
ofstream g("alibaba.out");
int main()
{
    int n, k;
    int ch;
    int sterse = 0;
    f >> n >> k;
    f.get();
    for (int i = 0; i < n; i++)
    {
        ch = f.get() - '0';
        while (!st.empty() && st.back() < ch && sterse < k)
        {
            st.pop_back();
            sterse++;
        }
        st.push_back(ch);
    }
    while (sterse < k)
    {
        sterse++;
        st.pop_back();
    }
    for (auto &x : st)
    {
        g << x;
    }
}