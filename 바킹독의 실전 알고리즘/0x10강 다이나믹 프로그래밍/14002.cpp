#include <bits/stdc++.h>
using namespace std;

int a[1005];
int d[1005];
int pre[1005];
int ans[1005];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    fill(d, d + n + 1, 1);
    fill(pre, pre + n + 1, -1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j < i; j++)
            if (a[i] > a[j]) {
                if (d[j] + 1 > d[i]) {
                    d[i] = d[j] + 1;
                    pre[i] = j;
                }
            }
    }
    
    cout << *max_element(d + 1, d + n + 1) << '\n';

    int mi = 1, md = d[1];
    for (int i = 2; i <= n; i++) {
        if (d[i] > md) {
            md = d[i];
            mi = i;
        }
    }

    int cur = mi;
    int idx = 0;
    while (cur != -1) {
        ans[idx++] = a[cur];
        cur = pre[cur];
    }
    for (int i = idx - 1; i >= 0; i--) cout << ans[i] << ' ';
}