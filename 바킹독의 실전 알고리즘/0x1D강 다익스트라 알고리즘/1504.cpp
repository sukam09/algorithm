#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

int n, e;
int v1, v2;
vector<pii> adj[805];
vector<vector<int>> dist;
const int INF = 300000000;

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
  cin >> n >> e;
  while (e--) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a].push_back({c, b});
    adj[b].push_back({c, a});
  }
  cin >> v1 >> v2;
  int st[3] = {1, v1, v2};
  for (auto v : st) dijkstra(v);
  // int overflow에 주의
  int ans1 = dist[0][v1] + dist[1][v2] + dist[2][n];
  int ans2 = dist[0][v2] + dist[2][v1] + dist[1][n];
  int ans = min(ans1, ans2);
  if (ans >= INF) ans = -1;
  cout << ans;
}