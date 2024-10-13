#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
vector<int> adj[MX];
int indegree[MX];
int outdegree[MX];
int vis[MX];
int cur;
int ret[3];

void dfs(int v) {
  if (indegree[v] >= 2 && outdegree[v] == 2) {
    cur = 2;
    return;
  }

  for (auto nv : adj[v]) {
    if (vis[nv]) {
      cur = 1;
      return;
    }
    vis[nv] = 1;
    dfs(nv);
  }
}

vector<int> solution(vector<vector<int>> edges) {
  int st = 0;
  for (auto edge : edges) {
    adj[edge[0]].push_back(edge[1]);
    outdegree[edge[0]]++;
    indegree[edge[1]]++;
  }

  for (int i = 1; i <= 1000000; i++) {
    if (indegree[i] == 0 && outdegree[i] >= 2) {
      st = i;
      break;
    }
  }

  for (auto tg : adj[st]) {
    vis[tg] = 1;
    cur = 0;
    dfs(tg);
    ret[cur]++;
  }

  return {st, ret[1], ret[0], ret[2]};
}