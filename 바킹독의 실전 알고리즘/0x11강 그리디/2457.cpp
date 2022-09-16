#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second
#define pb push_back

vector<pii> v;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

#ifdef ONLINE_JUDGE
#define debug(x) 0
#else
#define debug(x) cout << "[Debug] " << #x << ": " << (x) << '\n'
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);
#endif

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        v.pb({a * 100 + b, c * 100 + d});
    }
    int ans = 0;
    int t = 301;
    while (t <= 1130) {
        int nt = t;
        for (int i = 0; i < (int)v.size(); i++)
            if (v[i].X <= t && v[i].Y > nt) nt = v[i].Y;
        if (nt == t) {
            cout << 0;
            return 0;
        }
        ans++;
        t = nt;
    }
    cout << ans;
}