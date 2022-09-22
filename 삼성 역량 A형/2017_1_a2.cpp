#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
int n, m;
int board[205][205];
vector<vector<pii>> block;
int ans;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= m;
}

void insert(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
  pii p1 = {x1, y1}, p2 = {x2, y2}, p3 = {x3, y3}, p4 = {x4, y4};
  vector<pii> el = {p1, p2, p3, p4};
  block.push_back(el);
}

int cal(int x, int y, vector<pii> el) {
  int sum = 0;
  for (auto p : el) {
    int dx, dy;
    tie(dx, dy) = p;
    int nx = x + dx, ny = y + dy;
    if (OOB(nx, ny)) return 0;
    sum += board[nx][ny];
  }
  return sum;
}

void brute(int x, int y) {
  for (auto el : block) {
    int sum = cal(x, y, el);
    ans = max(sum, ans);
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      cin >> board[i][j];
  // block 1
  insert(0, 0, 0, 1, 1, 0, 1, 1);
  // block 2
  insert(0, 0, 0, 1, 0, 2, 0, 3);
  insert(0, 0, 1, 0, 2, 0, 3, 0);
  // block 3
  insert(0, 0, 1, 0, 1, 1, 2, 1);
  insert(-1, 1, 0, 0, 0, 1, 1, 0);
  insert(-1, 1, -1, 2, 0, 0, 0, 1);
  insert(0, 0, 0, 1, 1, 1, 1, 2);
  // block 4-1
  insert(0, 0, 1, 0, 2, 0, 2, 1);
  insert(0, 0, 0, 1, 0, 2, 1, 0);
  insert(0, 0, 0, 1, 1, 1, 2, 1);
  insert(-1, 2, 0, 0, 0, 1, 0, 2);
  // block 4-2 (flipped)
  insert(-2, 1, -1, 1, 0, 0, 0, 1);
  insert(-1, 0, 0, 0, 0, 1, 0, 2);
  insert(0, 0, 0, 1, 1, 0, 2, 0);
  insert(0, 0, 0, 1, 0, 2, 1, 2);
  // block 5
  insert(0, 0, 1, 0, 1, 1, 2, 0);
  insert(0, 0, 0, 1, 0, 2, 1, 1);
  insert(-1, 1, 0, 0, 0, 1, 1, 1);
  insert(-1, 1, 0, 0, 0, 1, 0, 2);

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      brute(i, j);
  cout << ans;
}