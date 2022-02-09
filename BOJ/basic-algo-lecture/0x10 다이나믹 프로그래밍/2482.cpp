#include <bits/stdc++.h>
using namespace std;

int d[1005][1005];
int mod = 1000000003;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i++) d[i][1] = i;
    for (int i = 4; i <= n; i++) {
        for (int j = 2; j <= k; j++) {
            if (j > i / 2) continue;
            d[i][j] = (d[i - 1][j] + d[i - 2][j - 1]) % mod;
        }
    }
    cout << d[n][k];
}