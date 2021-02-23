#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int mat[1002][1002], cost[1002][1002];
const int WALL = 10000000;
const int UNVISITED = 999999;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int n, m;
ifstream in("padure.in");
ofstream out("padure.out");
struct point
{
    int x;
    int y;
    int cost;
} start, endd;
queue<point> q;

void dfs(point from, int val) // val = in cel valoare facem fill
{
    cost[from.x][from.y] = from.cost;
    for (int i = 0; i < 4; i++)
    {

        int newX = from.x + dx[i];
        int newY = from.y + dy[i];
        if (mat[newX][newY] != WALL)
        {
            if (mat[newX][newY] == val && cost[newX][newY] == UNVISITED)
            {
                dfs({newX, newY, from.cost}, val);
            }
            if (mat[newX][newY] != val && cost[newX][newY] == UNVISITED)
            {
                q.push({newX, newY, from.cost + 1});
            }
        }
    }
}

int main()
{
    in >> n >> m >> start.x >> start.y >> endd.x >> endd.y;

    //bordez
    for (int i = 0; i <= n + 1; i++)
    {
        //orizontale
        mat[i][0] = WALL;
        mat[i][m + 1] = WALL;
    }

    for (int i = 0; i <= m + 1; i++)
    {
        //verticale
        mat[0][i] = WALL;
        mat[n + 1][i] = WALL;
    }

    // marchez ca nevizitat in cost
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cost[i][j] = UNVISITED;

    // citesc copacii
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            in >> mat[i][j];

    // bfs
    start.cost = 0;
    q.push(start);
    while (!q.empty())
    {
        point el = q.front();
        q.pop();
        if (cost[el.x][el.y] == UNVISITED)
        {
            dfs(el, mat[el.x][el.y]);
        }
    }
    out << cost[endd.x][endd.y];
}