#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n;
int board[20][20];
int dx1[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int dy1[8] = {1, 1, 0, -1, -1, -1, 0, 1};
int dx2[8] = {-1, -1, 1, 1};
int dy2[8] = {1, -1, -1, 1};
vector<pii> special;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

// d: 이동 방향, p: 이동 칸 수
void solve(int d, int p) {
  vector<vector<bool>> effected(n, vector<bool>(n));
  for (auto& cur : special) {
    int nx = (cur.X + p * dx1[d] + n) % n;
    int ny = (cur.Y + p * dy1[d] + n) % n;
    cur = { nx, ny };
    board[nx][ny]++; // 높이 1을 먼저 증가시켜줘야함
    effected[cur.X][cur.Y] = true;
  }
  // 대각선으로 인접한 높이 1 이상의 리브로수의 개수 만큼 높이가 증가
  for (auto& cur : special) {
    int cnt = 0;
    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.X + dx2[dir];
      int ny = cur.Y + dy2[dir];
      if (OOB(nx, ny)) continue;
      cnt += board[nx][ny] >= 1;
    }
    board[cur.X][cur.Y] += cnt;
  }
  vector<pii> nxt;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (effected[i][j]) continue;
      if (board[i][j] >= 2) {
        board[i][j] -= 2;
        nxt.push_back({ i, j });
      }
    }
  }
  special = nxt;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m;
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      cin >> board[i][j];
  for (int i = n - 2; i < n; i++)
    for (int j = 0;j < 2; j++)
      special.push_back({ i, j });
  while (m--) {
    int d, p;
    cin >> d >> p;
    d--;
    solve(d, p);
  }
  int ans = 0;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      ans += board[i][j];
  cout << ans;
}