#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> graph[10005];
int hacked[10005];
queue<int> que;

int bfs(int node) {
  vector<bool> visited(n + 5);
  visited[node] = true;
  que.push(node);
  int count = 1;
  while (!que.empty()) {
    int cur = que.front();
    que.pop();
    for (int next : graph[cur]) {
      if (visited[next]) {
        continue;
      }
      visited[next] = true;
      que.push(next);
      count++;
    }
  }
  return count;
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
  int maxval = 0;
  for (int i = 1; i <= n; i++) {
    hacked[i] = bfs(i);
    maxval = max(maxval, hacked[i]);
  }
  for (int i = 1; i <= n; i++) {
    if (hacked[i] == maxval) {
      cout << i << " ";
    }
  }
}