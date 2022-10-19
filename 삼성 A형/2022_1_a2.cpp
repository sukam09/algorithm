#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n;
int board[35][35];
int nxt[35][35]; // 회전용 보드
const int MX = 29 * 29 + 5;
int num[MX]; // num[i]: 그룹 i를 이루는 숫자
int cnt[MX]; // cnt[i]: 그룹 i가 있는 칸 수
bool vis[35][35];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int idx;
int line[MX][MX];
int ans;

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

void bfs(int x, int y, int target) {
  vis[x][y] = true;
  queue<pii> q;
  q.push({ x, y });
  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    cnt[idx]++;
    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (OOB(nx, ny) || vis[nx][ny] || board[nx][ny] != target)
        continue;
      vis[nx][ny] = true;
      q.push({ nx, ny });
    }
  }
}

void rotatesqr(int x1, int x2, int y1, int y2) {
  for (int i = x1; i <= x2; i++)
    for (int j = y1; j <= y2; j++)
      nxt[i][j] = board[y1 + y2 - j][i];
}

void rotate() {
  for (int i = 0;i < n;i++) fill(nxt[i], nxt[i] + n, 0);
  // 정사각형 회전
  rotatesqr(0, n / 2 - 1, 0, n / 2 - 1);
  rotatesqr(0, n / 2 - 1, n / 2 + 1, n - 1);
  rotatesqr(n / 2 + 1, n - 1, 0, n / 2 - 1);
  rotatesqr(n / 2 + 1, n - 1, n / 2 + 1, n - 1);
  // 십자 회전
  for (int i = 0;i < n / 2;i++) nxt[i][n / 2] = board[n / 2][n - 1 - i];
  for (int j = 0;j < n / 2;j++) nxt[n / 2][j] = board[j][n / 2];
  for (int i = n - 1;i > n / 2;i--) nxt[i][n / 2] = board[n / 2][n - 1 - i];
  for (int j = n - 1;j > n / 2;j--) nxt[n / 2][j] = board[j][n / 2];
  // board copy
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n;j++)
      board[i][j] = nxt[i][j];
}

void solve() {
  for (int i = 0;i < MX; i++) fill(num, num + MX, 0);
  for (int i = 0;i < MX; i++) fill(cnt, cnt + MX, 0);
  for (int i = 0;i < n; i++) fill(vis[i], vis[i] + n, false);
  for (int i = 0;i < MX;i++) fill(line[i], line[i] + MX, 0);
  int idx = 0;
  for (int i = 0;i < n;i++) {
    for (int j = 0;j < n;j++) {
      if (vis[i][j]) continue;
      num[idx++] = board[i][j];
      bfs(i, j, board[i][j]);
    }
  }
  for (int i = 0; i < idx; i++)
    for (int j = i + 1; j < idx; j++)
      ans += (cnt[i] + cnt[j]) * num[i] * num[j] * line[i][j];
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n;j++)
      cin >> board[i][j];
  int rotated = 0;
  while (true) {
    for (int i = 0;i < n;i++) {
      for (int j = 0;j < n;j++)
        cout << board[i][j] << ' ';
      cout << '\n';
    }
    cout << "----------------------------------------------------------\n";
    solve();
    if (rotated == 3) {
      cout << ans;
      return 0;
    }
    rotate();
    rotated++;
  }
}