#include <bits/stdc++.h>

// pt claritate :)
#define RED true
#define BLACK false

using namespace std;

ifstream fin("abce.in");
ofstream fout("abce.out");

struct RBNode
{
    int key; // valoarea nodului

    // pointeri spre copii stg/dr, si parent
    RBNode *left;
    RBNode *right;
    RBNode *p;

    bool color;
    // constructor
    RBNode(int val = 0, RBNode *l = nullptr, RBNode *r = nullptr, RBNode *parent = nullptr, bool c = BLACK) : key(val), left(l), right(r), p(parent), color(c){};
};

class RBTree
{

public:
    RBNode *root;
    RBNode *nil;

    RBTree()
    {
        nil = new RBNode(-1, nullptr, nullptr, nullptr, BLACK);
        root = nil;
    }

    /// Rotates around node, helps with balan fing O(1) (pointer magic)
    void leftRotate(RBNode *x)
    {
        // save right subtree of x.
        RBNode *y = x->right;
        // set y's left subtree as x's right subtree.
        x->right = y->left;
        if (y->left != nil)
            y->left->p = x;
        if (x->p == nil)
            root = y;
        else if (x == x->p->left)
            x->p->left = y;
        else
            x->p->right = y;
        y->left = x;
        x->p = y;
    }

    void rightRotate(RBNode *x)
    {
        RBNode *y = x->left;
        x->left = y->right;
        if (y->right != nil)
            y->right->p = x;
        if (x->p == nil)
            root = y;
        else if (x == x->p->right)
            x->p->right = y;
        y->right = x;
        x->p = y;
    }

    void insert(RBNode *z)
    {
        RBNode *y = nil;
        RBNode *x = root;
        while (x != nil)
        {
            y = x;
            if (z->key < x->key)
                x = x->left;
            else
                x = x->right;
        }
        z->p = y;
        if (y == nil)
            root = z;
        else if (z->key < y->key)
            y->left = z;
        else
            y->right = z;
        z->left = nil;
        z->right = nil;
        z->color = RED;
    }

    void insert_fix(RBNode *z)
    {
        RBNode *y;
        if (z->p == z->p->p->left)
        {
            y = z->p->p->right;
            if (y->color == RED)
            {
                z->p->color = BLACK;
                y->color = BLACK;
                z->p->p->color = RED;
                z = z->p->p;
            }
            else if (z == z->p->right)
            {
                z = z->p;
                leftRotate(z);
            }
            z->p->color = BLACK;
            z->p->p->color = RED;
            rightRotate(z->p->p);
        }
        else
        {
            y = z->p->p->left;
            if (y->color == RED)
            {
                z->p->color = BLACK;
                y->color = BLACK;
                z->p->p->color = RED;
                z = z->p->p;
            }
            else if (z == z->p->left)
            {
                z = z->p;
                rightRotate(z);
            }
            z->p->color = BLACK;
            z->p->p->color = RED;
            leftRotate(z->p->p);
        }
        root->color = BLACK;
    }

    RBNode *minimum(RBNode *z)
    {
        while (z->left != nil)
        {
            z = z->left;
        }
        return z;
    };

    int succesor(int val)
    {

        int last = -1;
        RBNode *x = root;
        while (x != nil)
        {
            if (x->key == val)
                return val;

            else if (val < x->key)
            {
                last = x->key;
                x = x->left;
            }
            else
            {
                x = x->right;
            }
        }
        return last;
    }

    int predecesor(int val)
    {
        int last = -1;
        RBNode *x = root;
        while (x != nil)
        {
            if (x->key == val)
                return val;

            else if (val < x->key)
            {
                x = x->left;
            }
            else
            {
                last = x->key;
                x = x->right;
            }
        }
        return last;
    }

    void transplant(RBNode *u, RBNode *v)
    {
        if (u->p == nil)
            root = v;
        else if (u == u->p->left)
            u->p->left = v;
        else
            u->p->right = v;
        v->p = u->p;
    }

    void rbDelete(RBNode *z)
    {
        RBNode *y = z;
        RBNode *x;
        bool y_originalColor = y->color;

        if (z->left == nil)
        {
            x = z->right;
            transplant(z, z->right);
        }
        else if (z->right == nil)
        {
            x = z->left;
            transplant(z, z->left);
        }
        else
        {
            y = minimum(z->right);
            y_originalColor = y->color;
            x = y->right;
            if (y->p == z)
                x->p = y;
            else
            {
                transplant(y, y->right);
                y->right = z->right;
                y->right->p = y;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->p = y;
            y->color = z->color;
        }
        if (y_originalColor == BLACK)
            delete_fix(x);
    }

    void delete_fix(RBNode *x)
    {
        while (x != root && x->color == BLACK)
        {
            if (x == x->p->left)
            {
                RBNode *w = x->p->right;
                if (w->color == RED)
                {
                    w->color = BLACK;
                    x->p->color = RED;
                    leftRotate(x->p);
                    w = x->p->right;
                }
                if (w->left->color == BLACK && w->right->color == BLACK)
                {
                    w->color = RED;
                    x = x->p;
                }
                else
                {
                    if (w->right->color == BLACK)
                    {
                        w->left->color = BLACK;
                        w->color = RED;
                        rightRotate(w);
                        w = x->p->right;
                    }
                    w->color = x->p->color;
                    x->p->color = BLACK;
                    w->right->color = BLACK;
                    leftRotate(x->p);
                    x = root;
                }
            }
            else
            {
                RBNode *w = x->p->left;
                if (w->color == RED)
                {
                    w->color = BLACK;
                    x->p->color = RED;
                    rightRotate(x->p);
                    w = x->p->left;
                }
                if (w->right->color == BLACK && w->left->color == BLACK)
                {
                    w->color = RED;
                    x = x->p;
                }
                else
                {
                    if (w->left->color == BLACK)
                    {
                        w->right->color = BLACK;
                        w->color = RED;
                        leftRotate(w);
                        w = x->p->left;
                    }
                    w->color = x->p->color;
                    x->p->color = BLACK;
                    w->left->color = BLACK;
                    rightRotate(x->p);
                    x = root;
                }
            }
        }
        x->color = BLACK;
    }

    void print(RBNode *poz)
    {
        if (poz == nil)
            return;
        print(poz->left);
        fout << poz->key << '\n';
        print(poz->right);
    }

    RBNode *find(int val)
    {
        RBNode *poz = root;
        while (poz != nil)
        {
            if (poz->key == val)
                return poz;
            else if (val < poz->key)
            {
                poz = poz->left;
            }
            else
            {
                poz = poz->right;
            }
        }
        return nil;
    }

    void interval(int left, int right)
    {
        int current = succesor(left);
        while (current <= right && current != -1)
        {
            if (find(current) != nil)
            {
                fout << current << ' ';
            }
            current = succesor(current + 1);
        }
        fout << '\n';
    }

    int del(int val)
    {
        int count = 0;
        RBNode *found = find(val);
        while (found != nil)
        {
            count++;
            rbDelete(found);
            found = find(val);
        }
        return count;
    }
};

int main()
{
    int n;
    fin >> n;
    RBTree tree = RBTree();
    for (int i = 0; i < n; i++)
    {
        int q, val;
        fin >> q >> val;
        switch (q)
        {
        case 1:
            tree.insert(new RBNode(val));
            break;
        case 2:
            // fout << tree.del(val) << "\n";
            tree.del(val);
            break;
        case 3:
            fout << (tree.find(val) != tree.nil) << "\n";
            break;
        case 5:
            fout << tree.succesor(val) << "\n";
            break;
        case 4:
            fout << tree.predecesor(val) << "\n";
            break;
        case 6:
            int val2;
            fin >> val2;
            tree.interval(val, val2);
            break;
        }
    }
    fin.close();
    fout.close();
};