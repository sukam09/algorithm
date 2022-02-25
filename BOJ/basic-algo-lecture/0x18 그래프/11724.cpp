#include <bits/stdc++.h>
using namespace std;
#define pb push_back

vector<int> adj[1005];
bool vis[1005];

void dfs(int v) {
    vis[v] = true;
    for (int nv : adj[v]) {
        if (vis[nv]) continue;
        dfs(nv);
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

#ifdef LOCAL
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;
    while (m--) {
        int u, v;
        cin >> u >> v;
        adj[u].pb(v);
        adj[v].pb(u);
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue;
        ans++;
        dfs(i);
    }
    cout << ans;
}