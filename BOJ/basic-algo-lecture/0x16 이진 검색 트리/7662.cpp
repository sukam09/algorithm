#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    multiset<int> s;
    while (n--) {
        char op;
        cin >> op;
        if (op == 'I') {
            int m;
            cin >> m;
            s.insert(m);
        }
        else {
            int m;
            cin >> m;
            if (s.empty()) continue;
            if (m == 1) s.erase(prev(s.end()));
            else s.erase(s.begin());
        }
    }
    if (s.empty()) cout << "EMPTY" << '\n';
    else cout << *prev(s.end()) << ' ' << *s.begin() << '\n';
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) solve();
}