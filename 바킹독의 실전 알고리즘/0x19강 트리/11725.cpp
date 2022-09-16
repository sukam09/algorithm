#include <bits/stdc++.h>
using namespace std;
#define pb push_back

#ifdef ONLINE_JUDGE
#define fastio() ios::sync_with_stdio(0); cin.tie(0)
#define fileinput() (void)0
#define debug(x) (void)0

#else
#define fastio() (void)0
#define fileinput() freopen("/home/sukam09/algorithm/input.txt", "r", stdin)
#define debug(x) cout << "[Debug] " << #x << " = " << (x) << '\n'
#endif

vector<int> adj[100005];
int p[100005];

void dfs(int v) {
    for (int nv : adj[v]) {
        if (nv == p[v]) continue;
        p[nv] = v;
        dfs(nv);
    }
}

int main(void) {
    fastio(); fileinput();

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int st, ed;
        cin >> st >> ed;
        adj[st].pb(ed);
        adj[ed].pb(st);
    }
    dfs(1);
    for (int i = 2; i <= n; i++) cout << p[i] << '\n';
}