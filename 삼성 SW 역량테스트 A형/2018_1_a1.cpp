#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m;
int k; // 말 개수
int board[10][10];
int nb[10][10]; // 격자 방문 여부
int ans = 100;
int dx[4] = { -1, 0, 1, 0 }; // 상, 우, 하, 좌
int dy[4] = { 0, 1, 0, -1 };
vector<vector<int>> obj; // obj[0]은 더미
vector<int> obj1 = { 0 };
vector<int> obj2= { 1, 3 };
vector<int> obj3 = { 0, 1 };
vector<int> obj4 = { 0, 1, 3 };
vector<int> obj5 = { 0, 1, 2, 3 };
vector<pii> pos; // 아군 말의 위치

bool OOB(int x, int y) {
    return x < 0 || x >= n || y < 0 || y >= m;
}

void solve(int cnt, int dir) {
    int x = pos[cnt].X;
    int y = pos[cnt].Y;
    int z = board[x][y];
    vector<int> v = obj[z];
    for (auto dd : v) {
        int d = (dir + dd) % 4;
        int xx = x;
        int yy = y;
        while (true) {
            int nx = xx + dx[d];
            int ny = yy + dy[d];
            if (OOB(nx, ny) || board[nx][ny] == 6)
                break;
            nb[nx][ny] = 1;
            xx = nx;
            yy = ny;
        }
    }
}

void dfs(int cnt) {
    if (cnt == k) {
        int res = 0;
        for (int i = 0;i < n; i++) {
            for (int j = 0;j < m; j++) {
                if (nb[i][j] == 0) res++;
            }
        }
        ans = min(ans, res);
        return;
    }
    for (int dir = 0;dir < 4; dir++) {
        int tmp[10][10] = {};
        for (int i = 0; i < n; i++)
            for (int j = 0;j < m; j++)
                tmp[i][j] = nb[i][j];
        solve(cnt, dir);
        dfs(cnt + 1);
        for (int i = 0; i < n; i++)
            for (int j = 0;j < m; j++)
                nb[i][j] = tmp[i][j];
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for (int i = 0;i < n; i++)
        for (int j = 0;j < m; j++) {
            cin >> board[i][j];
            if (board[i][j] > 0 && board[i][j] < 6) {
                k++;
                pos.push_back({ i, j });
                nb[i][j] = 1;
            }
            else if (board[i][j] == 6) nb[i][j] = 1;
        }
    obj = { {}, obj1, obj2, obj3, obj4, obj5 };
    dfs(0);
    cout << ans;
}