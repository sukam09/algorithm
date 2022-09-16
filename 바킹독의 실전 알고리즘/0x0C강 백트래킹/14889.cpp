#include <bits/stdc++.h>
using namespace std;

int n;
int a[25][25];
int cand[25];
vector<int> p, s, l;
int mx = 0x7f7f7f7f;

void getp() {
    int tmp[n / 2];
    fill(tmp, tmp + n / 2, 1);
    tmp[0] = 0, tmp[1] = 0;
    do {
        for (int i = 0; i < n / 2; i++)
            if (tmp[i] == 0) p.push_back(i);
    } while (next_permutation(tmp, tmp + n / 2));
}

int solve() {
    int ss = 0, ls = 0;
    for (int i = 0; i < p.size(); i += 2) {
        int x = p[i], y = p[i + 1];
        ss += a[s[x]][s[y]] + a[s[y]][s[x]];
        ls += a[l[x]][l[y]] + a[l[y]][l[x]];
    }
    return abs(ss - ls);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> a[i][j];

    getp();
    for (int i = n / 2; i < n; i++) cand[i] = 1;
    int ans = mx;
    
    do {
        s.clear(); l.clear();
        for (int i = 0; i < n; i++) {
            if (cand[i] == 0) s.push_back(i);
            else l.push_back(i);
        }
        int res = solve();
        ans = min(ans, res);
    } while (next_permutation(cand, cand + n));
    
    cout << ans;
}