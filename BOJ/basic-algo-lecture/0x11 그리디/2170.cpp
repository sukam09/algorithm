#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define X first
#define Y second

pii a[1000005];

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
        int x, y;
        cin >> x >> y;
        a[i].X = x;
        a[i].Y = y;
    }
    sort(a, a + n);
    int ans = 0;
    int l = a[0].X, r = a[0].Y;
    for (int i = 1; i < n; i++) {
        if (a[i].X <= r && a[i].Y >= r) r = a[i].Y;
        else if (a[i].X > r) {
            ans += r - l;
            l = a[i].X;
            r = a[i].Y;
        }
    }
    ans += r - l;
    cout << ans;
}