#include <bits/stdc++.h>
using namespace std;

bool a[1005];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);
    
    int n, k;
    cin >> n >> k;
    int cnt = 0;
    for (int i = 2; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            if (a[j]) continue;
            a[j] = true; cnt++;
            if (cnt == k) {
                cout << j; return 0;
            }
        }
    }
}