#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

string board[15];
int n, m;
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int ans;
const int MX = 1000 * 5 * 26 + 5;
const int ROOT = 1;
int unused = 2;
set<string> godstr;
map<string, int> cnt;
vector<string> query;

void dfs(int x, int y, string key) {
  if (key.size() > 5) return;
  if (godstr.find(key) != godstr.end()) cnt[key]++;
  for (int i = 0; i < 8; i++) {
    int nx = (x + n + dx[i]) % n;
    int ny = (y + m + dy[i]) % m;
    dfs(nx, ny, key + board[nx][ny]);
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int k;
  string s;
  cin >> n >> m >> k;
  for (int i = 0; i < n; i++) {
    cin >> s;
    board[i] = s;
  }
  while (k--) {
    cin >> s;
    query.push_back(s);
    godstr.insert(s);
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      string st;
      dfs(i, j, st + board[i][j]);
    }
  }
  for (auto q : query) cout << cnt[q] << '\n';
}