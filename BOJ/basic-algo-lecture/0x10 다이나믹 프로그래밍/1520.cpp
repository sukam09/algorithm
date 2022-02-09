#include <bits/stdc++.h>
using namespace std;

int m, n;
int a[505][505];
int d[505][505];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

bool oob(int x, int y) {
    return x < 0 || x >= m || y < 0 || y >= n;
}

int solve(int x, int y) {
    if (x == m - 1 && y == n - 1) return 1;
    if (d[x][y] != -1) return d[x][y];
    d[x][y] = 0;
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (oob(nx, ny) || a[x][y] <= a[nx][ny]) continue;
        d[x][y] += solve(nx, ny);
    }
    return d[x][y];
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >> n;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> a[i][j], d[i][j] = -1;
    cout << solve(0, 0);
}