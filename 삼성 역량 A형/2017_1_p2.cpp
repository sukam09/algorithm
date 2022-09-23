#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int n, m;
int board[10][10];
int nb[10][10];
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
vector<pii> space;
vector<pii> fire;
int ans = 0;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= m;
}

void brute(int x, int y, int z) {
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      nb[i][j] = board[i][j];
  
  int xx, xy;
  int yx, yy;
  int zx, zy;
  tie(xx, xy) = space[x];
  tie(yx, yy) = space[y];
  tie(zx, zy) = space[z];
  nb[xx][xy] = 1;
  nb[yx][yy] = 1;
  nb[zx][zy] = 1;
  
  queue<pii> q;
  bool vis[10][10] = {};
  for (auto f : fire) {
    int x, y;
    tie(x, y) = f;
    vis[x][y] = true;
    q.push({x, y});
  }

  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    int x, y;
    tie(x, y) = cur;
    for (int d = 0; d < 4; d++) {
      int nx = x + dx[d];
      int ny = y + dy[d];
      if (OOB(nx, ny) || vis[nx][ny] || nb[nx][ny] == 1)
        continue;
      vis[nx][ny] = true;
      q.push({nx, ny});
    }
  }

  int area = 0;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      if (!vis[i][j] && nb[i][j] != 1) area++;
  ans = max(ans, area);
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0;i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
      if (board[i][j] == 0) space.push_back({i, j});
      else if (board[i][j] == 2) fire.push_back({i, j});
    }
  }
  int sz = space.size();
  for (int  i = 0; i < sz ; i++)
    for (int j = i + 1; j < sz; j++)
      for (int k = j + 1; k < sz; k++)
        brute(i, j, k);
  cout << ans;
}