#include <bits/stdc++.h>
using namespace std;

vector<int> adj[101005];
int dist[101005];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, k, m;
  cin >> n >> k >> m;
  int h = 100001;
  while (m--) {
    for (int i = 0; i < k; i++) {
      int v;
      cin >> v;
      adj[h].push_back(v);
      adj[v].push_back(h);
    }
    h++;
  }
  queue<int> q;
  q.push(1);
  dist[1] = 1;
  while (!q.empty()) {
    int cur = q.front(); q.pop();
    if (cur == n) {
      cout << dist[n];
      return 0;
    }
    for (auto nxt : adj[cur]) {
      if (dist[nxt] > 0) continue;
      dist[nxt] = nxt <= 100000 ? dist[cur] + 1 : dist[cur];
      q.push(nxt);
    }
  }
  cout << -1;
}