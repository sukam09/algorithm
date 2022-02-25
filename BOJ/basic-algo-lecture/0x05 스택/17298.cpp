#include <bits/stdc++.h>
using namespace std;
int a[1000005];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    stack<int> s;
    vector<int> ans;
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && a[i] >= s.top()) s.pop();
        int res = s.empty() ? -1 : s.top();
        ans.push_back(res);
        s.push(a[i]);
    }
    for (int i = n - 1; i >= 0; i--) cout << ans[i] << ' ';
}