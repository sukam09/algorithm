#include <bits/stdc++.h>
using namespace std;

int t, n;
bool a[105];

int solve() {
    int ret = 0;
    for (int i = 1; i <= n; i++)
        for (int j = i; j <= n; j += i)
            a[j] = (a[j] ? false : true);
    for (int i = 1; i <= n; i++)
        if (!a[i]) ret++;
    return ret;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> t;
    while (t--) {
        cin >> n;
        fill(a, a + 105, true);
        cout << solve() << '\n';
    }
}