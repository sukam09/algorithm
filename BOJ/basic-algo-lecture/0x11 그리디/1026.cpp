#include <bits/stdc++.h>
using namespace std;
int s;
int a[55], b[55];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);

    cin >> s;
    for (int i = 0; i < s; i++) cin >> a[i];
    for (int i = 0; i < s; i++) cin >> b[i];
    sort(a, a + s);
    sort(b, b + s, greater<int>());
    int ans = 0;
    for (int i = 0; i < s; i++) ans += a[i] * b[i];
    cout << ans;
}