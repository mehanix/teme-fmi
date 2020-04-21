#include <bits/stdc++.h>

// pt claritate :)
#define RED true
#define BLACK false

using namespace std;

struct RBNode
{
    int key; // valoarea nodului

    // pointeri spre copii stg/dr, si parent
    RBNode *left;
    RBNode *right;
    RBNode *p;

    bool color;

public:
    // constructor
    RBNode(int val = 0, RBNode *l = nullptr, RBNode *r = nullptr, RBNode *parent = nullptr, bool c=BLACK) : key(val), left(l), right(r), p(parent), color(c){};

    // flips red <-> black
    void flipColor()
    {
        color = (color == RED) ? BLACK : RED;
    }
};

class RBTree
{
    RBNode *root;

    // nodul null
    RBNode *nil = new RBNode(-1, nullptr, nullptr, nullptr, BLACK);

public:
    RBTree();
    RBTree(int val) //creates tree with val as root value
    {
        root = new RBNode(val);
    }

    /// Rotates around node, helps with balancing O(1) (pointer magic)
    void leftRotate(RBTree *tree, RBNode *x)
    {
        // save right subtree of x.
        RBNode *y = x->right;
        // set y's left subtree as x's right subtree.
        x->right = y->left;
        if (y->left != tree->nil)
            y->left->p = x;
        if (x->p == tree->nil)
            tree->root = y;
        else if (x == x->p->left)
            x->p->left = y;
        else
            x->p->right = y;
        y->left = x;
        x->p = y;
    }

    void rightRotate(RBTree *tree, RBNode *x)
    {
        RBNode *y = x->left;
        x->left = y->right;
        if (y->right != tree->nil)
            y->right->p = x;
        if (x->p == tree->nil)
            tree->root = y;
        else if (x == x->p->right)
            x->p->right = y;
        y->right = x;
        x->p = y;
    }

    void insert(RBTree *tree, RBNode *z)
    {
        RBNode *y = tree->nil;
        RBNode *x = root;
        while (x != tree->nil)
        {
            y = x;
            if (z->key < x->key)
                x = x->left;
            else
                x = x->right;
        }
        z->p = y;
        if (y == tree->nil)
            tree->root = z;
        else if (z->key < y->key)
            y->left = z;
        else
            y->right = z;
        z->left = tree->nil;
        z->right = tree->nil;
        z->color = RED;
    }

    void insert_fix(RBTree *tree, RBNode *z)
    {
        RBNode* y;
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
                leftRotate(tree, z);
            }
            z->p->color = BLACK;
            z->p->p->color = RED;
            rightRotate(tree, z->p->p);
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
                rightRotate(tree, z);
            }
            z->p->color = BLACK;
            z->p->p->color = RED;
            leftRotate(tree, z->p->p);
        }
        tree->root->color = BLACK;
    }
    RBNode* minimum(RBNode* z) {};
    void transplant(RBTree *tree, RBNode *u, RBNode *v)
    {
        if (u->p == tree->nil)
            tree->root = v;
        else if (u == u->p->left)
            u->p->left = v;
        else
            u->p->right = v;
        v->p = u->p;
    }

    void rbDelete(RBTree* tree, RBNode* z) 
    {
        RBNode* y = z;
        RBNode* x;
        bool y_originalColor = y->color;

        if(z->left == tree->nil)
        {
            x = z->right;
            transplant(tree,z,z->right);
        }
        else if (z->right == tree->nil) 
        {
            x = z->left;
            transplant(tree,z,z->left);
        }
        else {
            y = minimum(z->right);
            y_originalColor = y->color;
            x = y->right;
            if(y->p == z)
                x->p = y;
            else {
                transplant(tree,y,y->right);
                y->right = z->right;
                y->right->p = y;
            }
            transplant(tree,z,y);
            y->left = z->left;
            y->left->p = y;
            y->color = z->color;
        }
        //if(y_originalColor == BLACK)
            //delete_fix(tree,x);
    }
};

int main()
{
    cout << "hello";
};