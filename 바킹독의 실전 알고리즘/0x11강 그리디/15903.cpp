#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll a[1005];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    priority_queue<ll, vector<ll>, greater<ll>> pq;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        pq.push(a[i]);
    }
    ll ans = 0;
    while (m--) {
        ll a = pq.top(); pq.pop();
        ll b = pq.top(); pq.pop();
        pq.push(a + b);
        pq.push(a + b);
    }
    while (!pq.empty()) {
        ans += pq.top(); pq.pop();
    }
    cout << ans;
}