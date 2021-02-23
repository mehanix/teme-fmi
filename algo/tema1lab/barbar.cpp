#include <fstream>
#include <iostream>
#include <queue>
using namespace std;
int n, m;
int mat[1005][1005], viz[1005][1005];
const int WALL = 10000000;
const int UNVISITED = 999999;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int sol = -1;
ifstream f("barbar.in");
ofstream g("barbar.out");
char line[1005];
struct point
{
    int x;
    int y;
} start, endd;
queue<point> q;

void reset()
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            viz[i][j] = 0;
}

void dfs(point from, int bound)
{
    // cout << "sunt in " << from.x << ' ' << from.y << "val:" << mat[from.x][from.y] << " bound:" << bound << '\n';
    if (mat[from.x][from.y] < bound)
        return;
    viz[from.x][from.y] = 1;
    for (int i = 0; i < 4; i++)
    {
        int x = from.x + dx[i];
        int y = from.y + dy[i];
        if (!viz[x][y] && mat[x][y] >= bound && mat[x][y] != WALL)
            dfs({x, y},
                bound);
    }
}

void cautbin(int left, int right)
{
    if (left > right)
        return;
    int mid = (left + right) / 2;
    reset();
    dfs(start, mid);
    if (viz[endd.x][endd.y] == 1)
    {
        sol = mid;
        cautbin(mid + 1, right);
    }
    else
    {
        cautbin(left, mid - 1);
    }
}

int main()
{
    f >> n >> m;
    f.getline(line, m + 1);
    for (int i = 1; i <= n; i++)
    {
        f.getline(line, m + 1);
        cout << line << "\n";
        for (int j = 1; j <= m; j++)
        {
            switch (line[j - 1])
            {
            case '.':
            {
                mat[i][j] = UNVISITED;
                break;
            }
            case 'I':
            {
                mat[i][j] = UNVISITED;

                start.x = i;
                start.y = j;
                break;
            }
            case 'O':
            {
                mat[i][j] = UNVISITED;

                endd.x = i;
                endd.y = j;
                break;
            }
            case '*':
            {
                mat[i][j] = WALL;
                break;
            }
            case 'D':
            {
                mat[i][j] = 0;
                q.push({i, j});
                break;
            }
            break;
            }
        }
    }

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
    //bfs din dragoni lol
    while (!q.empty())
    {
        point from = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int x = from.x + dx[i];
            int y = from.y + dy[i];
            if (mat[x][y] != WALL && mat[x][y] == UNVISITED)
            {
                mat[x][y] = mat[from.x][from.y] + 1;
                q.push({x, y});
            }
        }
    }
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = 1; j <= m; j++)
    //         cout << mat[i][j] << ' ';
    //     cout << '\n';
    // }
    cautbin(0, n * m);
    g << sol << '\n';
}