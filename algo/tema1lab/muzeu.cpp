#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int mat[255][255];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
const int NOT_VISITED = -1000000;
int n, m;
ifstream in("muzeu.in");
ofstream out("muzeu.out");
struct point
{
    int x;
    int y;
} start, endd;
queue<point> q;
int main()
{
    in >> n;

    //bordez
    for (int i = 0; i <= n + 1; i++)
    {
        //orizontale
        mat[0][i] = -1;
        mat[n + 1][i] = -1;

        //verticale
        mat[i][0] = -1;
        mat[i][n + 1] = -1;
    }

    //marchez ca not viz
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            mat[i][j] = NOT_VISITED;
    //citesc matricea
    char rand[n + 2];
    in.getline(rand, n + 1);
    for (int i = 1; i <= n; i++)
    {
        char rand[n + 2];
        in.getline(rand, n + 1);
        for (int j = 0; j < n; j++)
        {
            if (rand[j] == '#')
                mat[i][j + 1] = -2;
            else if (rand[j] == 'P')
            {
                mat[i][j + 1] = 0;
                q.push({i, j + 1}); //incepem din paznici
                cout << i << ' ' << j + 1 << '\n';
            }
        }
    }
    // bfs
    while (!q.empty())
    {

        point curent;
        curent = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            if (mat[curent.x + dx[i]][curent.y + dy[i]] == NOT_VISITED)
            {
                mat[curent.x + dx[i]][curent.y + dy[i]] = mat[curent.x][curent.y] + 1;
                q.push({curent.x + dx[i], curent.y + dy[i]});
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            if (mat[i][j] == NOT_VISITED)
                out << -1 << ' ';
            else
            {
                out << mat[i][j] << ' ';
            }
        out << '\n';
    }
}