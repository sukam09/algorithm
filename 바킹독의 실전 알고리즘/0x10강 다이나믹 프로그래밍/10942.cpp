#include <bits/stdc++.h>
using namespace std;

int n, m, s, e;
int a[2005];
int d[2005][2005];

void solve() {
    for (int i = 1; i <= n; i++) d[i][i] = 1;
    for (int i = n; i >= 1; i--) {
        for (int j = i; j <= n; j++) {
            if (a[i] == a[j]) {
                if (j == i + 1) d[i][j] = 1;
                else if (d[i + 1][j - 1]) d[i][j] = 1; 
            }
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];
    cin >> m;
    solve();
    while (m--) {
        cin >> s >> e;
        cout << d[s][e] << '\n';
    }
}