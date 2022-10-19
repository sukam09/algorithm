#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m;
int board[25][25];
int ans;
// 하, 우, 상, 좌
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
//   5
// 4 1 3
//   2
//   6
// 1이 윗면, 6이 아랫면
vector<int> dice = { 5, 4, 1, 3, 2, 6 };
int x, y;
int dir = 1;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

void bfs(int x, int y) {
  queue<pii> q;
  q.push({x, y});
  vector<vector<bool>> vis(n, vector<bool>(n));
  vis[x][y] = true;
  int target = board[x][y];
  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    ans += board[cur.X][cur.Y];
    for (int d = 0; d < 4; d++) {
      int nx = cur.X + dx[d];
      int ny = cur.Y + dy[d];
      if (OOB(nx, ny) || vis[nx][ny] || board[nx][ny] != target) continue;
      vis[nx][ny] = true;
      q.push({nx, ny});
    }
  }
}

void roll(int dir) {
  vector<int> nxt(6);
  if (dir == 0) {
    nxt = { dice[5], dice[1], dice[0], dice[3], dice[2], dice[4] };
  }
  else if (dir == 1) {
    nxt = { dice[0], dice[5], dice[1], dice[2], dice[4], dice[3] };
  }
  else if (dir == 2) {
    nxt = { dice[2], dice[1], dice[4], dice[3], dice[5], dice[0] };
  }
  else {
    nxt = { dice[0], dice[2], dice[3], dice[5], dice[4], dice[1] };
  }
  dice = nxt;
}

void solve() {
  int nx = x + dx[dir];
  int ny = y + dy[dir];
  if (OOB(nx, ny)) {
    dir = (dir + 2 + 4) % 4;
    nx = x + dx[dir];
    ny = y + dy[dir];
  }
  roll(dir);
  bfs(nx, ny);
  int bottom = dice[5];
  if (bottom > board[nx][ny]) {
    dir = (dir - 1 + 4) % 4;
  }
  else if (bottom < board[nx][ny]) {
    dir = (dir + 1 + 4) % 4;
  }
  x = nx; y = ny;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0;i < n; i++)
    for (int j = 0;j < n;j++)
      cin >> board[i][j];
  while (m--) solve();
  cout << ans;
}