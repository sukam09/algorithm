#include <bits/stdc++.h>
using namespace std;
int t, n;
vector<bool> p(1000001, true);

void sieve() {
    p[0] = p[1] = false;
    for (int i = 2; i * i <= 1000000; i++) {
        if (!p[i]) continue;
        for (int j = i * i; j <= 1000000; j += i)
            p[j] = false;
    }
}

void solve() {
    int ans = 0;
    for (int i = 2; i <= n / 2; i++)
        if (p[i] && p[n - i]) ans++;
    cout << ans << '\n';
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> t;
    sieve();
    while (t--) {
        cin >> n;
        solve();
    }
}