#include <bits/stdc++.h>
using namespace std;
using ti3 = tuple<int, int, int>;
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

vector<ti3> v;
int l[2005];

int main(void) {
    fastio(); fileinput();

    int n, c;
    cin >> n >> c;
    int m;
    cin >> m;
    while (m--) {
        int st, ed, w;
        cin >> st >> ed >> w;
        v.pb({ed, st, w});
    }
    sort(v.begin(), v.end());
    fill(l + 1, l + n + 1, c);
    int ans = 0;
    for (auto cur : v) {
        int ed, st, w;
        tie(ed, st, w) = cur;
        for (int i = st; i < ed; i++) w = min(w, l[i]);
        ans += w;
        for (int i = st; i < ed; i++) l[i] -= w;
    }
    cout << ans;
}