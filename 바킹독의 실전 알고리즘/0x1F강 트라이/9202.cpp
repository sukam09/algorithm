#include <bits/stdc++.h>
using namespace std;

const int MX = 300000 * 8 + 5;
const int ROOT = 1;
int unused = 2;
int nxt[MX][26];
bool chk[MX];

unordered_set<string> word;
int score[9] = {0, 0, 0, 1, 1, 2, 3, 5, 11};
string board[4];
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
bool vis[4][4];

bool OOB(int x, int y) {
  return x < 0 || x >= 4 || y < 0 || y >= 4;
}

int c2i(char c) {
  return c - 'A';
}

void insert(string& s) {
  int cur = ROOT;
  for (auto c : s) {
    if (nxt[cur][c2i(c)] == 0)
      nxt[cur][c2i(c)] = unused++;
    cur = nxt[cur][c2i(c)];
  }
  chk[cur] = true;
}

void dfs(int x, int y, int v, string key) {
  if (chk[v]) word.insert(key);
  for (int i = 0; i < 8; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];
    if (OOB(nx, ny) || vis[nx][ny]) continue;
    int nv = nxt[v][c2i(board[nx][ny])];
    if (nv == 0) continue;
    vis[nx][ny] = true;
    dfs(nx, ny, nv, key + board[nx][ny]);
    vis[nx][ny] = false;
  }
}

void solve() {
  word.clear();
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++)
        fill(vis[k], vis[k] + 4, false);
      vis[i][j] = true;
      string st = "";
      st += board[i][j];
      dfs(i, j, nxt[ROOT][c2i(board[i][j])], st);
    }
  }

  int sum = 0;
  int mx = 0;
  vector<string> longest;
  int cnt = word.size();
  for (auto w : word) {
    int sz = w.size();
    sum += score[sz];
    if (sz > mx) {
      mx = sz;
      longest = {w};
    } else if (sz == mx) {
      longest.push_back(w);
    }
  }
  sort(longest.begin(), longest.end());
  cout << sum << ' ' << longest[0] << ' ' << cnt << '\n';
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int w, b;
  cin >> w;
  while (w--) {
    string s;
    cin >> s;
    insert(s);
  }
  cin >> b;
  for (int i = 0; i < b; i++) {
    for (int j = 0; j < 4; j++)
      cin >> board[j];
    solve();
  }
}