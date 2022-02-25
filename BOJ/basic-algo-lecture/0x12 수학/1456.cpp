#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll a, b;
vector<bool> p(10000001, true);

void sieve() {
    for (ll i = 2; i * i <= 10000000; i++) {
        if (!p[i]) continue;
        for (ll j = i * i; j <= 10000000; j += i)
            p[j] = false;
    }
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> a >> b;
    sieve();
    int ans = 0;
    for (ll i = 2; i * i <= b; i++) {
        if (!p[i]) continue;
        ll j = i;
        while (i <= b / j) {
            if (i * j >= a) ans++;
            j *= i;
        }
    }
    cout << ans;
}