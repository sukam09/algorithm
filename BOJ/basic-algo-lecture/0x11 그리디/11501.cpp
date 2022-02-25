#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
#define X first
#define Y second
int n;
int a[1000005];

void solve() {
    ll ans = 0;
    stack<pii> s;
    vector<int> idx(n, -1);
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && a[i] >= s.top().X) s.pop();
        if (!s.empty()) idx[i] = s.top().Y;
        s.push({a[i], i});
    }

    int buy = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        if (idx[i] != -1) {
            buy += a[i];
            cnt++;
        }
        else {
            ans += a[i] * cnt - buy;
            buy = 0; cnt = 0;
        }
    }
    cout << ans << '\n';
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        fill(a, a + n, 0);
        for (int i = 0; i < n; i++) cin >> a[i];
        solve();
    }
}