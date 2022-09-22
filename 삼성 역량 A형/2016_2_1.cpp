#include <bits/stdc++.h>
using namespace std;

int n, m;
int board[25][25];
int x, y; // 주사위 위치
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int dice[6]; // 0은 위, 1은 아래

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= m;
}

void roll(int dir) {
  int tmp[6];
  fill(tmp, tmp + 6, -1);
  if (dir == 0) {
    // 동
    tmp[3] = dice[1];
    tmp[0] = dice[3];
    tmp[4] = dice[0];
    tmp[1] = dice[4];
  } else if (dir == 1) {
    // 서
    tmp[3] = dice[0];
    tmp[0] = dice[4];
    tmp[4] = dice[1];
    tmp[1] = dice[3];
  } else if (dir == 2) {
    // 북
    tmp[2] = dice[0];
    tmp[0] = dice[5];
    tmp[5] = dice[1];
    tmp[1] = dice[2];
  } else {
    // 남
    tmp[2] = dice[1];
    tmp[0] = dice[2];
    tmp[5] = dice[0];
    tmp[1] = dice[5];
  }
  for (int i = 0; i < 6; i++)
    if (tmp[i] != -1) dice[i] = tmp[i];
}

// 칸이 0이면 바닥 -> 칸
// 칸이 0이 아니면 칸 -> 바닥, 칸은 0이됨
// 출력은 주사위 윗칸
// 0 ~ 3 -> 동, 서, 북, 남
void solve(int dir) {
  int nx = x + dx[dir], ny = y + dy[dir];
  if (OOB(nx, ny)) return;
  roll(dir);
  x = nx, y = ny;
  if (board[x][y] == 0) {
    board[x][y] = dice[1];
  } else {
    dice[1] = board[x][y];
    board[x][y] = 0;
  }
  cout << dice[0] << '\n';
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int k;
  cin >> n >> m >> x >> y >> k;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      cin >> board[i][j];
  while (k--) {
    int dir;
    cin >> dir;
    // dir: 1 ~ 4 -> 0 ~ 3
    solve(dir - 1);
  }
}