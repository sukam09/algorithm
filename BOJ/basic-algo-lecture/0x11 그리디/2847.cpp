#include <bits/stdc++.h>
using namespace std;
int a[105];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    int ans = 0;
    int cur = a[n - 1];
    for (int i = n - 1; i >= 0; i--) {
        while (a[i] < cur) cur--;
        ans += a[i] - cur;
        cur--;
    }
    cout << ans;
}