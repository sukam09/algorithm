#include <bits/stdc++.h>
using namespace std;

int n, m;
int x, y, d;
int board[55][55];
bool vis[55][55];
// 북, 동, 남, 서
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
bool power = true;

void move() {
  for (int i = 0; i < 4; i++) {
    int nx = x + dx[(d + 3) % 4];
    int ny = y + dy[(d + 3) % 4];
    if (!vis[nx][ny] && board[nx][ny] == 0) {
      vis[nx][ny] = true;
      // 좌회전하고 한칸 전진
      d = (d + 3) % 4;
      x = nx; y = ny;
      return;
    }
    // 좌회전
    d = (d + 3) % 4;
  }
  // 후진
  int nx = x - dx[d];
  int ny = y - dy[d];
  if (board[nx][ny] == 1) {
    power = false;
    return;
  }
  x = nx; y = ny;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  cin >> x >> y >> d;
  for (int i = 0 ;i < n; i++)
    for (int j = 0; j < m; j++)
      cin >> board[i][j];
  vis[x][y] = true;
  while (power) move();
  int ans = 0;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (vis[i][j]) ans++;
  cout << ans;
}