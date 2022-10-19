#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>;
//using pii = pair<int, int>;
#define X first
#define Y second

int n;
// 하, 우, 상, 좌
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
vector<vector<int>> board(105, vector<int>(105, -1));
int ans;
int x, y; // 술래 위치
int dir = 2; // 술래 방향
int turn = 1;
bool tree[105][105];
vector<ti3> route;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

// make spiral route
void init() {
  int len = 3;
  // 기준점
  int x = n / 2 - 1;
  int y = n / 2;
  int x1, x2, y1, y2;
  x1 = x;
  x2 = x1 + len - 1;
  y1 = y - 1;
  y2 = y1 + len - 1;
  while (len <= n) {
    for (int j = y; j < y2; j++)
      route.push_back({ x1, j, 1 });
    //
    for (int j = y; j < y2; j++)
      route.push_back({ x1, j, 1 });
    for (int j = y; j < y2; j++)
      route.push_back({ x1, j, 1 });
    for (int j = y; j < y2; j++)
      route.push_back({ x1, j, 1 });
    x--; y--;
    len += 2;
  }
}

void solve() {
  // 도망자
  for (int i = 0;i < n;i++) {
    for (int j = 0;j < n;j++) {
      if (board[i][j] == -1) continue;
      int d = board[i][j];
      int nx = i + dx[d];
      int ny = j + dy[d];
      if (OOB(nx, ny)) {
        d = (d + 2 + 4) % 4;
        nx = i + dx[d];
        ny = j + dy[d];
      }
      if (nx == x && ny == y) continue;
      board[nx][ny] = d;
      board[i][j] = -1;
    }
  }
  // 술래

}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m, h, k;
  cin >> n >> m >> h >> k;
  while (m--) {
    int x, y, d;
    cin >> x >> y >> d;
    if (d == 1) d = 1;
    else d = 0;
    x--; y--;
    board[x][y] = d;
  }
  while (h--) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    tree[x][y] = true;
  }
  x = n / 2; y = n / 2;
  init();
  while (k--) {
    solve();
    turn++;
  }
  cout << ans;
}