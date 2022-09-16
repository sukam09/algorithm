#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int MX = 15005;
const int ROOT = 1;
int unused = 2;
unordered_map<string, int> nxt[MX];
int depth[MX];
string name[MX];

void insert(vector<string>& route) {
  int cur = ROOT;
  depth[cur] = -1;
  for (auto r : route) {
    int nv = nxt[cur][r];
    if (nv == 0)
      nv = nxt[cur][r] = unused++;
    depth[nv] = depth[cur] + 1;
    name[nv] = r;
    cur = nv;
  }
}

void dfs(int v) {
  if (v != ROOT) {
    for (int i = 0; i < depth[v]; i++)
      cout << "--";
    cout << name[v] << '\n';
  }
  vector<pair<string, int>> m(nxt[v].begin(), nxt[v].end());
  sort(m.begin(), m.end());
  for (auto mm : m) dfs(mm.Y);
}

int main(void) {
  int n;
  cin >> n;
  while (n--) {
    int k;
    cin >> k;
    vector<string> route;
    while (k--) {
      string s;
      cin >> s;
      route.push_back(s);
    }
    insert(route);
  }
  dfs(ROOT);
}