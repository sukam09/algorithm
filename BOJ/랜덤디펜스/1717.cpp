#include <bits/stdc++.h>
using namespace std;

vector<int> p(1000005, -1);

int find(int x) {
  if (p[x] < 0) return x;
  return p[x] = find(p[x]);
}

void merge(int u, int v) {
  u = find(u); v = find(v);
  if (u == v) return;
  if (p[u] == p[v]) p[u]--;
  if (p[u] < p[v]) p[v] = u;
  else p[u] = v;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  while (m--) {
    int x, a, b;
    cin >> x >> a >> b;
    if (x == 0) merge(a, b);
    else cout << (find(a) == find(b) ? "YES\n" : "NO\n");
  }
}