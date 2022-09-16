#include <bits/stdc++.h>
using namespace std;

int t, n;
int a[100005];

bool prime(int n) {
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

void solve() {
    int m = n;
    while (m > 1) {
        for (int i = 2; i <= m; i++) {
            if (prime(i) && m % i == 0) {
                a[i]++;
                m /= i;
                break;
            }
        }
    }
    for (int i = 2; i <= n; i++)
        if (a[i]) cout << i << ' ' << a[i] << '\n';
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> t;
    while (t--) {
        fill(a, a + 100005, 0);
        cin >> n;
        solve();
    }
}