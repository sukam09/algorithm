#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using pii = pair<int, int>;

int n;
int dx[4] = {-1, -1, 1, 1}; // 대각선
int dy[4] = {1, -1, -1, 1};
int board[105][105];
int ans = 0x7f7f7f7f;
vector<int> p;

//int judge(int x1, int y1, int x2, int y2) {
//  if (x1 + y1 == x2 + y2) return 0;
//  else if (x1 - y1 == x2 - y2) return 1;
//  else return 2;
//}

//void solve(int p, int q, int r, int s) {
//  int x1, y1, x2, y2, x3, y3, x4, y4;
//  x1 = p / n, y1 = p % n;
//  x2 = q / n, y2 = q % n;
//  x3 = r / n, y3 = r % n;
//  x4 = s / n, y4 = s % n;
//  int pr = judge(x1, y1, x3, y3);
//  int qs = judge(x2, y2, x4, y4);
//  int pq = judge(x1, y1, x2, y2);
//  int rs = judge(x2, y3, x4, y4);
//  if (!(pr == 1 && qs == 1 && pq == 0 && rs == 0) || (pr == 0 && qs == 0 && pq == 1 && rs == 1))
//    return;
//  vector<int> area(5);
//  for (int i = 0;i < n;i++) {
//    for (int j = 0;j < n;j++) {
//      // 2 ~ 5
//      if (i < x2 && j <= y1) {
//        area[1] += board[i][j];
//      }
//      else if (i <= x3 && j > y1) {
//        area[2] += board[i][j];
//      }
//      else if (i >= x2 && j < y4) {
//        area[3] += board[i][j];
//      }
//      else if (i > x3 && j >= y4) {
//        area[4] += board[i][j];
//      }
//      // 1
//      else {
//        area[0] += board[i][j];
//      }
//    }
//  }
//  int mx = *max_element(area.begin(), area.end());
//  int mn = *min_element(area.begin(), area.end());
//  ans = min(ans, mx - mn);
//  cout << p << ' ' << q << ' ' << r << ' ' << s << '\n';
//  for (auto x : area) cout << x << ' '; cout << '\n';
//}

bool OOB(int x, int y) {
  return x < 0 || x >= n || y < 0 || y >= n;
}

void solve() {
  int x1 = p[0];
  int y1 = p[1];
  int x2 = p[2];
  int y2 = p[3];
  int x3 = p[4];
  int y3 = p[5];
  int x4 = p[6];
  int y4 = p[7];
  vector<int> area(5);
  for (int i = 0;i < n;i++) {
    for (int j = 0;j < n;j++) {
      // 2 ~ 5
      if (i < x2 && j <= y1) {
        area[1] += board[i][j];
      }
      else if (i <= x3 && j > y1) {
        area[2] += board[i][j];
      }
      else if (i >= x2 && j < y4) {
        area[3] += board[i][j];
      }
      else if (i > x3 && j >= y4) {
        area[4] += board[i][j];
      }
      // 1
      else {
        area[0] += board[i][j];
      }
    }
  }
  int mx = *max_element(area.begin(), area.end());
  int mn = *min_element(area.begin(), area.end());
  ans = min(ans, mx - mn);
  for (auto x : p) cout << x << ' '; cout << '\n';
}

void dfs(int x, int y, int cnt) {
  if (cnt == 4) {
    solve();
    return;
  }
  int nx = x + dx[cnt];
  int ny = y + dx[cnt];
  if (OOB(nx, ny)) return;
  p.push_back(nx);
  p.push_back(ny);
  dfs(nx, ny, cnt + 1);
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 0;i < n;i++)
    for (int j = 0;j < n; j++)
      cin >> board[i][j];
  //int num = n * n;
  //for (int i = 0;i < num; i++)
  //  for (int j = i + 1;j < num; j++)
  //    for (int k = j + 1;k < num; k++)
  //      for (int l = k + 1;l < num; l++)
  //        solve(i, j, k, l);
  for (int i = 0;i < n;i++) {
    for (int j = 0;j < n;j++) {
      p.clear();
      dfs(i, j, 0);
    }
  }
  cout << ans;
}