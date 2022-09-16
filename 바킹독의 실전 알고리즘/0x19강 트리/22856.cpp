#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using ti3 = tuple<int, int, int>;

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
bool OOB(int x, int y, int n, int m) {return x < 0 || x >= n || y < 0 || y >= m;}

#define X first
#define Y second
#define pb push_back

#ifdef ONLINE_JUDGE
#define fastio() ios::sync_with_stdio(0); cin.tie(0)
#define fileinput() (void)0
#define debug(x) (void)0
#define pf0l() (void)0

#else
#define fastio() (void)0
#define fileinput() freopen("/home/sukam09/algorithm/input.txt", "r", stdin)
#define debug(x) cout << #x << ": " << (x) << ' '
#define pf0l() cout << '\n'
#endif

int lc[100005];
int rc[100005];
bool vis[100005];
int p[100005];
vector<int> adj[100005];
int en;
int ans = -1;

void dfs(int v) {
    for (int nv : adj[v]) {
        if (nv == p[v]) continue;
        p[nv] = v;
        dfs(nv);
    }
}

void inorder(int v) {
    if (lc[v] != -1) inorder(lc[v]);
    en = v;
    if (rc[v] != -1) inorder(rc[v]);
}

void solve(int v) {
    vis[v] = true;
    ans++;
    if (lc[v] != -1 && !vis[lc[v]]) solve(lc[v]);
    else if (rc[v] != -1 && !vis[rc[v]]) solve(rc[v]);
    else if (v == en) return;
    else if (p[v]) solve(p[v]);
}

int main(void) {
    fastio(); fileinput();

    int n;
    cin >> n;
    while (n--) {
        int a, b, c;
        cin >> a >> b >> c;
        lc[a] = b;
        rc[a] = c;
        if (b != -1) {
            adj[a].pb(b);
            adj[b].pb(a);
        }
        if (c != -1) {
            adj[a].pb(c);
            adj[c].pb(a);
        }
    }
    dfs(1);
    inorder(1);
    solve(1);
    cout << ans;
}