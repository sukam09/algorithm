#include <bits/stdc++.h>
using namespace std;

int a[55];
bool vis[55];

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
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    int ans = 0;
    int i = 0;
    while (i <= n - 2 && a[i] < 0 && a[i + 1] <= 0) {
        ans += a[i] * a[i + 1];
        vis[i] = true;
        vis[i + 1] = true;
        i += 2;
    }
    i = n - 1;
    while (i >= 1 && a[i] > 0 && a[i - 1] > 0 && a[i] * a[i - 1] > a[i] + a[i - 1]) {
        ans += a[i] * a[i - 1];
        vis[i] = true;
        vis[i - 1] = true;
        i -= 2;
    }
    for (int i = 0; i < n; i++)
        if (!vis[i]) ans += a[i];
    for (int i = 0; i < n; i++) debug(a[i]);
    cout << ans;
}