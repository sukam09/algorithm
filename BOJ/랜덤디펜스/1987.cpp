#include <bits/stdc++.h>
using namespace std;

int r, c;
string board[25];
bool vis[26];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int ans = 0;

bool OOB(int x, int y) {
  return x < 0 || x >= r || y < 0 || y >= c;
}

int c2i(char c) {
  return c - 'A';
}

void dfs(int x, int y, int d) {
  ans = max(ans, d);
  for (int dir = 0;dir < 4; dir++) {
    int nx = x + dx[dir];
    int ny = y + dy[dir];
    if (OOB(nx, ny) || vis[c2i(board[nx][ny])])
      continue;
    vis[c2i(board[nx][ny])] = true;
    dfs(nx, ny, d + 1);
    vis[c2i(board[nx][ny])] = false;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> r >> c;
  for (int i =0;i < r ;i++) {
    string s;
    cin >> s;
    board[i] = s;
  }
  vis[c2i(board[0][0])] = true;
  dfs(0, 0, 1);
  cout << ans;
}