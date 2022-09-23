#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, m, x;
vector<pii> adj[1005];
vector<vector<int>> dist(1);
const int INF = 1e9 + 10;

void dijkstra(int st) {
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  vector<int> d(n + 1, INF);
  d[st] = 0;
  pq.push({0, st});
  while (!pq.empty()) {
    auto cur = pq.top(); pq.pop();
    if (d[cur.Y] != cur.X) continue;
    for (auto nxt : adj[cur.Y]) {
      if (d[nxt.Y] <= d[cur.Y] + nxt.X) continue;
      d[nxt.Y] = d[cur.Y] + nxt.X;
      pq.push({d[nxt.Y], nxt.Y});
    }
  }
  dist.push_back(d);
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m >> x;
  while (m--) {
    int u, v, t;
    cin >> u >> v >> t;
    adj[u].push_back({t, v});
  }
  for (int i = 1; i <= n; i++)
    dijkstra(i);
  int ans = 0;
  for (int i = 1; i <= n; i++)
    ans = max(ans, dist[i][x] + dist[x][i]);
  cout << ans;
}