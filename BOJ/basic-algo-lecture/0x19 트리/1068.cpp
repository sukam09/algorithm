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

int p[55];
bool removed[55];
vector<int> adj[55];
int ans = 0;

void remove(int v) {
    removed[v] = true;
    for (int nv : adj[v]) {
        if (nv == p[v]) continue;
        remove(nv);
    }
}

void dfs(int v) {
    int cnt = 0;
    for (int nv : adj[v]) {
        if (nv == p[v] || removed[nv]) continue;
        dfs(nv); cnt++;
    }
    if (cnt == 0) ans++;
}

int main(void) {
    fastio(); fileinput();

    int n, m;
    cin >> n;
    int root;
    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        p[i] = j;
        if (j == -1) {
            root = i;
            continue;
        }
        adj[i].pb(j); adj[j].pb(i);
    }
    cin >> m;
    if (m == root) {
        cout << 0;
        return 0;
    }
    remove(m);
    dfs(root);
    cout << ans;
}