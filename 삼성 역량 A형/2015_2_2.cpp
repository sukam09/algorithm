#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> board;
// 상, 좌, 우, 하
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
int rx, ry; // 빨간 사탕 좌표
int bx, by; // 파란 사탕 좌표
int ox, oy; // 출구 좌표
int ans = 11;

bool isbluefirst(int dir) {
  if (dir == 0) return bx < rx;
  else if (dir == 1) return by < ry;
  else if (dir == 2) return by > ry;
  else return bx > rx;
}

void tiltred(int dir) {
  while (true) {
    int nx = rx + dx[dir];
    int ny = ry + dy[dir];
    if (nx == ox && ny == oy) {
      rx = nx; ry = ny; return;
    }
    if (board[nx][ny] == '#' || (nx == bx && ny == by)) return;
    rx = nx; ry = ny;
  }
}

void tiltblue(int dir) {
  while (true) {
    int nx = bx + dx[dir];
    int ny = by + dy[dir];
    if (nx == ox && ny == oy) {
      bx = nx; by = ny; return;
    }
    if (board[nx][ny] == '#' || (nx == rx && ny == ry)) return;
    bx = nx; by = ny;
  }
}

void dfs(int cnt) {
  if (cnt >= ans) return;
  if (bx == ox && by == oy) return;
  if (rx == ox && ry == oy) {
    ans = min(ans, cnt);
    return;
  }
  for (int i = 0; i < 4; i++) {
    int rrx = rx, rry = ry, bbx = bx, bby = by;
    if (isbluefirst(i)) {
      tiltblue(i); tiltred(i);
    } else {
      tiltred(i); tiltblue(i);
    }
    dfs(cnt + 1);
    // 재귀를 빠져나올때 사탕의 위치를 원래대로 돌려줘야 함
    rx = rrx, ry = rry, bx = bbx, by = bby;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    board.push_back(s);
    for (int j = 0; j < m; j++) {
      if (board[i][j] == 'R') {
        rx = i; ry = j;
      } else if (board[i][j] == 'B') {
        bx = i; by = j;
      } else if (board[i][j] == 'O') {
        ox = i; oy = j;
      }
    }
  }
  dfs(0);
  if (ans == 11) ans = -1;
  cout << ans;
}