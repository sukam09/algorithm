#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m;
int board[55][55];
int num; // num of virus
vector<pii> hospital;
queue<pii> q;
int dist[55][55];
int ans = 0x7f7f7f7f;
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

void solve() {
  int cnt = 0; // max time
  int k = num; // virus num
  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    if (board[cur.X][cur.Y] == 0) {
      cnt = max(cnt, dist[cur.X][cur.Y]);
      k--;
    }
    // 모든 바이러스가 제거될 경우 성공
    if (k == 0) {
      ans = min(cnt, ans);
      return;
    }
    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (OOB(nx, ny) || board[nx][ny] == 1 || dist[nx][ny] != -1)
        continue;
      dist[nx][ny] = dist[cur.X][cur.Y] + 1;
      q.push({ nx, ny });
    }
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0;i < n; i++) {
    for (int j = 0;j < n; j++) {
      cin >> board[i][j];
      if (board[i][j] == 0) num++;
      else if (board[i][j] == 2) hospital.push_back({ i, j });
    }
  }
  int sz = hospital.size();
  vector<int> brute(sz);
  fill(brute.begin() + m, brute.end(), 1);
  do {
    for (int i = 0;i < n;i++)
      fill(dist[i], dist[i] + n, -1);
    while (!q.empty()) q.pop();
    for (int i = 0; i < sz; i++) {
      if (brute[i] == 0) {
        q.push({ hospital[i].X, hospital[i].Y });
        dist[hospital[i].X][hospital[i].Y] = 0;
      }
    }
    solve();
  } while (next_permutation(brute.begin(), brute.end()));
  if (ans == 0x7f7f7f7f) ans = -1;
  cout << ans;
}