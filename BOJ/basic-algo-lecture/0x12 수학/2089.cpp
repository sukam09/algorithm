#include <bits/stdc++.h>
using namespace std;

#define pb push_back

int n;
vector<int> v;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n;
    if (n == 0) {
        cout << 0;
        return 0;
    }
    while (n) {
        if (n < 0) {
            if (-n % 2 == 0) {
                n = -n / 2;
                v.pb(0);
            }
            else {
                n = -n / 2 + 1;
                v.pb(1);
            }
        }
        else {
            v.pb(n % 2);
            n = -(n / 2);
        }
    }
    reverse(v.begin(), v.end());
    for (int i : v) cout << i;
}