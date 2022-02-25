#include <bits/stdc++.h>
using namespace std;

vector<int> v;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("/home/sukam09/algorithm/input.txt", "r", stdin);

    string s;
    cin >> s;
    int sum = 0;
    for (char c : s) {
        v.push_back(c - '0');
        sum += c - '0';
    }
    sort(v.begin(), v.end(), greater<>());
    if (sum % 3 || v.back() != 0) {
        cout << -1;
        return 0;
    }
    for (int i : v) cout << i;
}