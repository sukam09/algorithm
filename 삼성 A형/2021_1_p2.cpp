#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n;
int board[30][30];
// → ↓ ← ↑
int dx1[4] = { 0, 1, 0, -1 };
int dy1[4] = { 1, 0, -1, 0 };
// ↓ → ↑ ←
int dx2[4] = { 1, 0, -1, 0 };
int dy2[4] = { 0, 1, 0, -1 };
int ans;
vector<pii> spiral;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

void init() {
  int x = n / 2;
  int y = n / 2 - 1;
  int len = 3;
  while (len <= n) {
    // x, y: 기준점
    int x1 = x - 1; int y1 = y;
    int x2 = x1 + len - 1; int y2 = y1;
    int x3 = x2; int y3 = y2 + len - 1;
    int x4 = x1; int y4 = y3;
    for (int i = x; i <= x2; i++)
      spiral.push_back({ i, y });
    for (int j = y2 + 1; j <= y3; j++)
      spiral.push_back({ x2, j });
    for (int i = x3 - 1; i >= x4; i--)
      spiral.push_back({ i, y3 });
    for (int j = y4 - 1; j >= y1; j--)
      spiral.push_back({ x4, j });
    x--; y--;
    len += 2;
  }
}

// 공격 방향: d, 공격 칸 수: p
void solve(int d, int p) {
  // 1
  int x = n / 2;
  int y = n / 2;
  while (p--) {
    int nx = x + dx1[d];
    int ny = y + dy1[d];
    ans += board[nx][ny];
    board[nx][ny] = 0;
    x = nx; y = ny;
  }
  // 2
  vector<int> v;
  for (auto s : spiral) {
    if (board[s.X][s.Y] == 0) continue;
    v.push_back(board[s.X][s.Y]);
  }
  // 3
  while (true) {
    bool chk = true;
    int cnt = 0;
    int recent = -1;
    for (int i = 0;i < (int)v.size(); i++) {
      if (recent == -1 || recent == v[i]) cnt++;
      else if (cnt >= 4) {
        chk = false;
        for (int j = i; j > i - cnt; j--) v[j] = 0;
        cnt = 0;
        recent = -1;
      }
    }
    vector<int> nv;
    for (auto x : v) {
      if (x != 0) nv.push_back(x);
    }
    nv = v;
    if (chk) break;
  }
  // 4
  vector<int> ret;
  int recent = -1;
  int cnt = 0;
  for (auto x : v) {
    if (recent == -1 || recent == x) cnt++;
    else {
      ret.push_back(cnt);
      ret.push_back(recent);
      recent = -1;
      cnt = 0;
    }
  }
  int idx = 0;
  for (auto& s : spiral) {
    if (idx < (int)ret.size()) board[s.X][s.Y] = ret[idx++];
    else board[s.X][s.Y] = 0;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m;
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      cin >> board[i][j];
  init();
  while (m--) {
    int d, p;
    cin >> d >> p;
    solve(d, p);
  }
  cout << ans;
}