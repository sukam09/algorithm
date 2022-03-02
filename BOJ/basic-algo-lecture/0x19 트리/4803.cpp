#include <bits/stdc++.h>
using namespace std;

vector<int> adj[505];
bool vis[505];
int p[505];
bool cycle;
int n;

void dfs(int v) {
    if (vis[v]) {
        cycle = true;
        return;
    }
    vis[v] = true;
    for (int nv : adj[v]) {
        if (nv == p[v]) continue;
        p[nv] = v;
        dfs(nv);
    }
}

int solve() {
    int ret = 0;
    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue;
        cycle = false;
        dfs(i);
        if (!cycle) ret++;
    }
    return ret;
}

int main(void) {
    int tc = 1;
    while (true) {
        int m;
        cin >> n >> m;
        if (n == 0 && m == 0) return 0;
        for (int i = 1; i <= n; i++) adj[i].clear();
        fill(vis, vis + n + 1, false);
        fill(p, p + n + 1, 0);
        while (m--) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int ans = solve();
        cout << "Case " << tc << ": ";
        if (ans == 0) cout << "No trees.\n";
        else if (ans == 1) cout << "There is one tree.\n";
        else cout << "A forest of " << ans << " trees.\n";
        tc++;
    }
}