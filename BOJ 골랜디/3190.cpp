#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
bool vis[105][105];
bool apple[105][105];
char dir[10005];
int x, y;
int d = 1;
queue<pii> q;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int k, l;
  cin >> n >> k;
  while (k--) {
    int r, c;
    cin >> r >> c;
    r--; c--;
    apple[r][c] = true;
  }
  cin >> l;
  while (l--) {
    int x;
    char c;
    cin >> x >> c;
    dir[x] = c;
  }
  int ans = 0;
  vis[0][0] = true;
  q.push({0, 0});
  while (true) {
    ans++;
    int nx = x + dx[d];
    int ny = y + dy[d];
    q.push({nx, ny});
    if (OOB(nx, ny) || vis[nx][ny]) {
      cout << ans;
      return 0;
    }
    vis[nx][ny] = true;
    x = nx; y = ny;
    if (apple[nx][ny]) apple[nx][ny] = 0;
    else {
      auto tail = q.front(); q.pop();
      vis[tail.X][tail.Y] = false;
    }
    if (dir[ans] == 'L') d = (d + 1 + 4) % 4;
    else if (dir[ans] == 'D') d = (d - 1 + 4) % 4;
  }
}