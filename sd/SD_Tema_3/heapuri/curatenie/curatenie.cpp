#include <bits/stdc++.h>

using namespace std;

int n;
int pre[500001];
int ino[500001];

int ll[500001], rr[500001];

struct node
{
    node *left;
    node *right;
    int val;
    node(int vl)
    {
        val = vl;
    }
};
ifstream f("curatenie.in");
ofstream g("curatenie.out");

int M = 0;
void construct(int l, int r, node *&root)
{
    if (l > r)
        return;
    int mij = ino[pre[++M]];
    root = new node(pre[M]);
    construct(l, mij - 1, root->left);
    construct(mij + 1, r, root->right);

    ll[root->val] = (root->left != nullptr) ? root->left->val : 0;
    rr[root->val] = (root->right != nullptr) ? root->right->val : 0;
}

int main()
{
    f >> n;
    for (int i = 1; i <= n; i++)
    {
        int x;
        f >> x;
        ino[x] = i;
    }
    for (int i = 1; i <= n; i++)
    {
        int x;
        f >> x;
        pre[i] = x;
    }
    node *r;
    construct(1, n, r);
    for (int i = 1; i <= n; i++)
    {
        g << ll[i] << ' ' << rr[i] << '\n';
    }
}