#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m, c;
int board[25][25];
int x, y;
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
pii goal[405];

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

// 가장 가까운 출발점의 거리와 좌표 계산
ti3 bfs1() {
  vector<ti3> nxt;
  vector<vector<int>> dist(n, vector<int>(n, -1));
  queue<pii> q;
  dist[x][y] = 0;
  q.push({ x, y });
  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    if (board[cur.X][cur.Y] > 1000)
      nxt.push_back({ dist[cur.X][cur.Y], cur.X, cur.Y });
    for (int dir = 0;dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (OOB(nx, ny) || dist[nx][ny] != -1 || board[nx][ny] == 1) continue;
      dist[nx][ny] = dist[cur.X][cur.Y] + 1;
      q.push({ nx, ny });
    }
  }
  // 출발점까지 도달할 수 없을 경우
  if (nxt.empty()) return {-1, -1, -1};
  sort(nxt.begin(), nxt.end());
  return nxt[0];
}

// 도착점까지의 거리 계산
int bfs2(int xe, int ye) {
  vector<vector<int>> dist(n, vector<int>(n, -1));
  queue<pii> q;
  dist[x][y] = 0;
  q.push({ x, y });
  while (!q.empty()) {
    auto cur = q.front(); q.pop();
    if (cur.X == xe && cur.Y == ye)
      return dist[cur.X][cur.Y];
    for (int dir = 0;dir < 4; dir++) {
      int nx = cur.X + dx[dir];
      int ny = cur.Y + dy[dir];
      if (OOB(nx, ny) || dist[nx][ny] != -1 || board[nx][ny] == 1) continue;
      dist[nx][ny] = dist[cur.X][cur.Y] + 1;
      q.push({ nx, ny });
    }
  }
  // 도착점까지 도달할 수 없을 경우
  return -1;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m >> c;
  for (int i = 0;i < n; i++)
    for (int j = 0;j < n; j++)
      cin >> board[i][j];
  cin >> x >> y;
  x--; y--;
  for (int i = 1;i <= m;i++) {
    int xs, ys, xe, ye;
    cin >> xs >> ys >> xe >> ye;
    xs--; ys--; xe--; ye--;
    board[xs][ys] = i + 1000; // 1000보다 크면 승객의 출발위치를 의미
    goal[i] = { xe, ye };
  }
  while (true) {
    int d1, xs, ys, xe, ye;
    tie(d1, xs, ys) = bfs1();
    if (d1 == -1 || c < d1) {
      cout << -1;
      return 0;
    }
    int p = board[xs][ys] - 1000;
    tie(xe, ye) = goal[p];
    // 출발점으로 이동
    c -= d1;
    x = xs, y = ys;
    board[x][y] = 0;
    int d2 = bfs2(xe, ye);
    if (d2 == -1 || c < d2) {
      cout << -1;
      return 0;
    }
    // 도착점으로 이동
    x = xe, y = ye;
    c += d2; // d2만큼 빼고 2*d2만큼 더함
    m--;
    if (m == 0) {
      cout << c;
      return 0;
    }
  }
}