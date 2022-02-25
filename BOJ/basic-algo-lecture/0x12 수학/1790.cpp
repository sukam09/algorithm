#include <bits/stdc++.h>
using namespace std;
int n, k;
int p10[9];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    p10[0] = 1;
    for (int i = 1; i <= 8; i++) p10[i] = p10[i - 1] * 10;

    int cnt = 1;
    int cur = 1;
    int sz = 1;
    while (cur <= n) {
        if (cnt + sz <= k) {
            cnt += sz;
            cur++;
            if (cur == p10[sz]) sz++;
        }
        else {
            int idx = k - cnt;
            string s = to_string(cur);
            cout << s[idx];
            return 0;
        }
    }
    cout << -1;
}