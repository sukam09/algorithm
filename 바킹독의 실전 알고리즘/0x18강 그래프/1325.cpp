#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> graph[10005];
int hacked[10005];
queue<int> q;

int bfs(int node) {
  vector<bool> vis(n + 5);
  vis[node] = true;
  q.push(node);
  int cnt = 1;
  while (!q.empty()) {
    int cur = q.front();
    q.pop();
    for (int nxt : graph[cur]) {
      if (vis[nxt]) {
        continue;
      }
      vis[nxt] = true;
      q.push(nxt);
      cnt++;
    }
  }
  return cnt;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    graph[b].push_back(a);
  }
  int mx = 0;
  for (int i = 1; i <= n; i++) {
    hacked[i] = bfs(i);
    mx = max(mx, hacked[i]);
  }
  for (int i = 1; i <= n; i++) {
    if (hacked[i] == mx) {
      cout << i << " ";
    }
  }
}