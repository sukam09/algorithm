#include <bits/stdc++.h>
using namespace std;

int a[1005];
int d[1005][35];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t, w;
    cin >> t >> w;
    for (int i = 1; i <= t; i++) cin >> a[i];
    
    for (int i = 0; i <= w; i++) d[1][i] = i % 2 ? a[1] - 1 : 2 - a[1];
    int cnt = 0;
    for (int i = 1; i <= t; i++) {
        if (a[i] == 1) cnt++;
        d[i][0] = cnt;
    }

    for (int i = 2; i <= t; i++) {
        for (int j = 1; j <= w; j++) {
            int val = 0;
            for (int k = 0; k <= j; k++) val = max(val, d[i - 1][k]);
            d[i][j] = val + (1 + j % 2 == a[i]);
        }
    }
    cout << *max_element(d[t], d[t] + w + 1);
}