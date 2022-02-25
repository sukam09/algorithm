#include <bits/stdc++.h>
using namespace std;

#ifdef ONLINE_JUDGE
#define fastio() ios::sync_with_stdio(0); cin.tie(0)
#define fileinput() (void)0
#define debug(x) (void)0

#else
#define fastio() (void)0
#define fileinput() freopen("/home/sukam09/algorithm/input.txt", "r", stdin)
#define debug(x) cout << "[Debug] " << #x << " = " << (x) << '\n'
#endif

int d[1000005];

int main(void) {
    fastio(); fileinput();

    int n;
    cin >> n;
    int l = 0;
    for (int i = 1; i <= n; i++) {
        int m;
        cin >> m;
        d[m] = d[m - 1] + 1;
        l = max(l, d[m]);
    }
    cout << n - l;
}