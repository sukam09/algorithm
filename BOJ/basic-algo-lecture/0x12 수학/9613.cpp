#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int t, n;
int a[105];

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ll solve() {
    ll ret = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            ret += gcd(a[i], a[j]);
    return ret;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> t;
    while (t--) {
        fill(a, a + 105, 0);
        cin >> n;
        for (int i = 0; i < n; i++) cin >> a[i];
        cout << solve() << '\n';
    }
}