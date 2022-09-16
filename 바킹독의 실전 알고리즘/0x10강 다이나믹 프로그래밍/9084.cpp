#include <bits/stdc++.h>
using namespace std;

int n, m;
int a[25];
int d[10005];

void solve() {
    fill(d, d + 10001, 0);
    d[0] = 1;
    for (int i = 0; i < n; i++) {
        int c = a[i];
        for (int j = 1; j <= m; j++)
            if (j >= c) d[j] += d[j - c];
    }
    cout << d[m] << '\n';
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    d[0] = 1;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> a[i];
        cin >> m;
        solve();
    }
}