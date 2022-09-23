#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

vector<pii> adj[20005];
int d[20005];
const int INF = 1e9 + 10;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int v, e, k;
  cin >> v >> e >> k;
  while (e--) {
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back({w, v});
  }
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  fill(d, d + v + 1, INF);
  d[k] = 0;
  pq.push({0, k});
  while (!pq.empty()) {
    auto cur = pq.top(); pq.pop();
    if (d[cur.Y] != cur.X) continue;
    for (auto nxt : adj[cur.Y]) {
      if (d[nxt.Y] <= d[cur.Y] + nxt.X) continue;
      d[nxt.Y] = d[cur.Y] + nxt.X;
      pq.push({d[nxt.Y], nxt.Y});
    }
  }
  for (int i = 1; i <= v; i++) {
    if (d[i] == INF) cout << "INF\n";
    else cout << d[i] << '\n';
  }
}