#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int board[25][25];
bool wall[25][25][4];
int cool[25][25];
int ans;
// 0, 2, 4, 6: 좌, 상, 우, 하
int dx[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };
int dy[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
vector<int> wd[8];

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

bool is_cool() {
  for (int i = 0;i < n; i++) {
    for (int j = 0;j < n;j++) {
      if (board[i][j] != 1) continue;
      if (cool[i][j] < k) return false;
    }
  }
  return true;
}

void run(int x, int y, int z, int dir) {
  cool[x][y] += z;
  if (z == 1) return;
  int leftup = (dir - 1 + 8) % 8;
  int rightup = (dir + 1 + 8) % 8;
  int nx, ny, w1, w2;
  // straight
  nx = x + dx[dir];
  ny = y + dy[dir];
  w1 = wd[dir][0];
  if (!OOB(nx, ny) && !wall[nx][ny][w1]) run(nx, ny, z - 1, dir);
  // leftup
  nx = x + dx[leftup];
  ny = y + dy[leftup];
  w1 = wd[dir][1];
  w2 = wd[dir][2];
  if (!OOB(nx, ny) && !wall[nx][ny][w1] && !wall[nx][ny][w2]) run(nx, ny, z - 1, dir);
  // rightup
  nx = x + dx[rightup];
  ny = y + dy[rightup];
  w1 = wd[dir][3];
  w2 = wd[dir][4];
  if (!OOB(nx, ny) && !wall[nx][ny][w1] && !wall[nx][ny][w2]) run(nx, ny, z - 1, dir);
}

void solve() {
  // 1
  for (int i = 0;i < n;i++) {
    for (int j = 0;j < n;j++) {
      if (board[i][j] < 2) continue;
      // 2, 3, 4, 5 -> 0, 2, 4, 6
      int dir = (board[i][j] - 2) * 2;
      run(i, j, 5, dir);
    }
  }
    for (int i =0;i < n;i++) {
    for (int j =0;j < n;j++)
      cout << cool[i][j] << ' ';
    cout << '\n';
  }
  // 2
  vector<vector<int>> nxt(n, vector<int>(n));
  vector<int> v = { 3, 0, 2, 0, 1, 0, 0, 0 }; // 방향에 따라 체크해야할 벽
  for (int i = 0;i < n; i++) {
    for (int j = 0;j < n;j++) {
      for (int dir = 0; dir < 8; dir += 2) {
        int nx = i + dx[dir];
        int ny = j + dy[dir];
        if (OOB(nx, ny) || cool[i][j] <= cool[nx][ny] || wall[nx][ny][v[dir]]) continue;
        nxt[nx][ny] += cool[i][j] / 4;
      }
    }
  }
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n;j++)
      cool[i][j] += nxt[i][j];
  // 3
  for (int i = 0;i < n; i++) {
    if (cool[i][0] == 0) continue;
    cool[i][0]--;
  }
  for (int i = 0;i < n; i++) {
    if (cool[i][n - 1] == 0) continue;
    cool[i][n - 1]--;
  }
  for (int j = 1;j <= n - 2; j++) {
    if (cool[0][j] == 0) continue;
    cool[0][j]--;
  }
  for (int j = 1;j <= n - 2; j++) {
    if (cool[n - 1][j] == 0) continue;
    cool[n - 1][j]--;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m >> k;
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n; j++)
      cin >> board[i][j];
  while (m--) {
    int x, y, s;
    cin >> x >> y >> s;
    x--; y--;
    wall[x][y][s] = true;
    if (s == 0) wall[x - 1][y][2] = true;
    else wall[x][y - 1][3] = true;
  }
  // 0, 2, 4, 6 방향에 대해 straight, leftup 2개, rightup 2개
  // 좌표는 nx, ny 기준
  wd[0] = {3, 0, 3, 2, 3};
  wd[2] = { 2, 2, 3, 1, 2 };
  wd[4] = { 1, 1, 2, 0, 1 };
  wd[6] = { 0, 0, 1, 0, 3 };
  while (true) {
    if (is_cool()) {
      cout << ans;
      return 0;
    }
    ans++;
    solve();
  }
}