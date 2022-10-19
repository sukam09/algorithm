#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>;
using ti4 = tuple<int, int, int, int>;

int m, t;
int x, y; // 팩맨 위치
// 상, 좌, 하, 우
int dx1[4] = {-1, 0, 1, 0};
int dy1[4] = {0, -1, 0, 1};
// ↑, ↖, ←, ↙, ↓, ↘, →, ↗
int dx2[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy2[8] = {0, -1, -1, -1, 0, 1, 1, 1};
vector<int> monster[4][4];
int dead[4][4]; // 가장 최근에 몬스터 시체가 생성된 턴, 없으면 0
int turn = 1;

bool OOB(int x, int y) {
  return x < 0 || x >= 4 || y < 0 || y >= 4;
}

int move(int i, int j, int k) {
  vector<vector<int>> tmp(4, vector<int>(4));
  for (int i = 0;i <4 ;i++)
    for (int j =0;j < 4;j++)
      tmp[i][j] = (int)monster[i][j].size();
  int cnt = 0;
  int xx = x;
  int yy = y;
  for (auto z : {i, j, k}) {
    int nx = xx + dx1[z];
    int ny = yy + dy1[z];
    if (OOB(nx, ny)) return -1;
    cnt += tmp[nx][ny];
    tmp[nx][ny] = 0;
    xx = nx;
    yy = ny;
  }
  return cnt;
}

ti3 brute() {
  vector<ti4> ret;
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        int cnt = move(i, j, k);
        if (cnt == -1) continue; // invalid
        ret.push_back({ -cnt, i, j, k });
      }
    }
  }
  sort(ret.begin(), ret.end());
  for (auto& r : ret) {
    int a, b, c, d;
    tie(a, b, c, d) = r;
  }
  int cnt, i, j, k;
  tie(cnt, i, j, k) = ret[0];
  return { i, j, k };
}

void solve() {
  // 1
  vector<ti3> egg;
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4;j++) {
      for (auto d : monster[i][j]) {
        egg.push_back({ i, j, d });
      }
    }
  }
  // 2
  vector<int> nxt[4][4];
  for (int i = 0;i < 4;i++) {
    for (int j = 0;j < 4;j++) {
      for (auto d : monster[i][j]) {
        bool chk = false;
        for (int dir = 0; dir < 8; dir++) {
          int nd = (d + dir + 8) % 8;
          int nx = i + dx2[nd];
          int ny = j + dy2[nd];
          if (OOB(nx, ny) || dead[nx][ny] != 0 || (nx == x && ny == y))
            continue;
          nxt[nx][ny].push_back(nd);
          chk = true; break;
        }
        // 몬스터가 움직이지 않음
        if (!chk) nxt[i][j].push_back(d);
      }
    }
  }
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4;j++) {
      monster[i][j] = nxt[i][j];
    }
  }
  // 3
  int i, j, k;
  tie(i, j, k) = brute();
  // 팩맨 이동
  for (auto z : { i, j, k }) {
    int nx = x + dx1[z];
    int ny = y + dy1[z];
    if (!monster[nx][ny].empty()) {
      dead[nx][ny] = turn;
      monster[nx][ny].clear();
    }
    x = nx; y = ny;
  }
  // 4
  for (int i = 0;i < 4; i++) {
    for (int j = 0;j < 4; j++) {
      if (dead[i][j] + 2 == turn)
        dead[i][j] = 0;
    }
  }
  // 5
  for (auto& e : egg) {
    int r, c, d;
    tie(r, c, d) = e;
    monster[r][c].push_back(d);
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> m >> t;
  cin >> x >> y;
  x--; y--;
  for (int i = 0;i < m; i++) {
    int r, c, d;
    cin >> r >> c >> d;
    r--; c--; d--;
    monster[r][c].push_back(d);
  }
  while (t--) {
    solve();
    turn++;
  }
  int ans = 0;
  for (int i =0;i <4; i++)
    for (int j = 0;j < 4;j++)
      ans += (int)monster[i][j].size();
  cout << ans;
}