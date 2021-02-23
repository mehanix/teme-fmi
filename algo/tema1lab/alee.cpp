#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int mat[200][200];

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int n, m;
ifstream in("alee.in");
ofstream out("alee.out");
struct point
{
    int x;
    int y;
} start, endd;
queue<point> q;
int main()
{
    in >> n >> m;

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

    // citesc copacii
    for (int i = 0; i < m; i++)
    {
        int x, y;
        in >> x >> y;
        mat[x][y] = -1;
    }
    in >> start.x >> start.y >> endd.x >> endd.y;
    // bfs
    q.push(start);
    mat[start.x][start.y] = 1;
    while (!q.empty())
    {

        point curent;
        curent = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            if (mat[curent.x + dx[i]][curent.y + dy[i]] == 0)
            {
                mat[curent.x + dx[i]][curent.y + dy[i]] = mat[curent.x][curent.y] + 1;
                q.push({curent.x + dx[i], curent.y + dy[i]});
            }
        }
    }
    out << mat[endd.x][endd.y];
}