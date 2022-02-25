#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;
#define pb push_back
#define X first
#define Y second

pii a[200005];

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
    for (int i = 0; i < n; i++)
        cin >> a[i].X >> a[i].Y;
    sort(a, a + n);
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(a[0].Y);
    for (int i = 1; i < n; i++) {
        int last = pq.top();
        if (last <= a[i].X) pq.pop();
        pq.push(a[i].Y);
    }
    cout << pq.size();
}