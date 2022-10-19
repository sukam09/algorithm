#include <bits/stdc++.h>
using namespace std;

int n;
int board[25][25];
int ans;

void rotate() {
  int tmp[25][25] = {};
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      tmp[i][j] = board[i][j];
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      board[i][j] = tmp[n - 1 - j][i];
}

void tilt(int dir) {
  // 왼쪽으로 미는 것만 구현
  while (dir--) rotate();
  for (int i = 0; i < n; i++) {
    int tilted[25] = {};
    int idx = 0;
    for (int j = 0; j < n; j++) {
      if (board[i][j] == 0) continue;
      if (tilted[idx] == 0) tilted[idx] = board[i][j];
      else if (tilted[idx] == board[i][j]) tilted[idx++] *= 2;
      else tilted[++idx] = board[i][j];
    }
    for (int j = 0; j < n; j++)
      board[i][j] = tilted[j];
  }
}

void dfs(int cnt) {
  if (cnt == 10) {
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        ans = max(ans, board[i][j]);
    return;
  }
  int tmp[25][25] = {};
  for (int i = 0; i < 4; i++) {
    for (int r = 0; r < n; r++)
      for (int c = 0; c < n; c++)
        tmp[r][c] = board[r][c];
    tilt(i);
    dfs(cnt + 1);
    // 보드 상태 원래대로
    for (int r = 0; r < n; r++)
      for (int c = 0; c < n; c++)
        board[r][c] = tmp[r][c];
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      cin >> board[i][j];
  dfs(0);
  cout << ans;
}